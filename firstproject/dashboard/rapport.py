import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:@localhost:3306/pfe')

sql="select category_name from dashboard_category;"
df= pd.read_sql(sql, engine)
#df.head()
file = 'rapport.xlsx'
df.to_excel(file, index=False)
engine.dispose()