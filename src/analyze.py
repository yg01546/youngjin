import json,pathlib,re
import pandas as pd

raw=pathlib.Path('data/raw')
def num(x):
    if x is None or str(x).strip() in ('','-'): return None
    try: return float(re.sub(r'[^0-9.-]','',str(x).replace(',','')))
    except: return None

def load_year(y):
    d=json.loads((raw/f'financials_{y}.json').read_text(encoding='utf-8')); rows=d.get('list',[])
    aliases={'revenue':['매출액','수익(매출액)'],'operating_profit':['영업이익','영업이익(손실)'],'net_income':['당기순이익','당기순이익(손실)'],'assets':['자산총계'],'liabilities':['부채총계'],'equity':['자본총계'],'cash':['현금및현금성자산'],'cfo':['영업활동현금흐름']}
    out={'year':y}
    for k,names in aliases.items():
        out[k]=None
        for row in rows:
            if (row.get('account_nm') or '').strip() in names:
                out[k]=num(row.get('thstrm_amount')); break
    return out

df=pd.DataFrame([load_year(y) for y in range(2021,2026)])
df['revenue_growth']=df.revenue.pct_change()*100
df['operating_margin']=df.operating_profit/df.revenue*100
df['net_margin']=df.net_income/df.revenue*100
df['debt_ratio']=df.liabilities/df.equity*100
df['equity_ratio']=df.equity/df.assets*100
df['cfo_net_income']=df.cfo/df.net_income
df['net_debt']=df.liabilities-df.cash
pathlib.Path('data/processed').mkdir(parents=True,exist_ok=True)
df.to_csv('data/processed/financial_analysis.csv',index=False,encoding='utf-8-sig')
pathlib.Path('dashboard').mkdir(exist_ok=True)
df.to_json('dashboard/data.json',orient='records',force_ascii=False,indent=2)
