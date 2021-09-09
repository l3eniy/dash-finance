import pandas
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "privKey.json"

sql = '''select geld1.id, geld1.label, geld1.datum, geld1.betrag, SUM(geld2.betrag) as sum
from `dash-finance-app.bens_daten.geld` geld1
inner join `dash-finance-app.bens_daten.geld` geld2 on geld1.id >= geld2.id
group by geld1.id, geld1.label, geld1.datum, geld1.betrag
order by geld1.datum'''

project_id = 'dash-finance-app'
df = pandas.read_gbq(sql, project_id=project_id, dialect='standard')
print(df)
