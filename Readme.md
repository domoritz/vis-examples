# Vis examples

## Consumer complaints

```bash
csvsql --db sqlite:///complaints.db Consumer_Complaints.csv -y 1000 --insert
```

```sql
select "Date received", "Product", "Sub-product", "Company", "State", "ZIP code", "Consumer consent provided?", "Submitted via", "Company response to consumer", "Timely response?", "Consumer disputed?"
from Consumer_Complaints
where ("Date received" like '2012%' or "Date received" like '2013%' or "Date received" like '2014%' or "Date received" like '2015%' or "Date received" like '2016%') and ("Product" = 'Mortgage' or "Product" = 'Credit reporting' or "Product" = 'Debt collection' or "Product" = 'Credit card' or "Product" like 'Bank account%')
order by random()
limit 20000;
```

```bash
sqlite3 complaints.db -header -csv < query.sql > complaints.cs
```

## CO2 and Temperature data

https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2017
http://data.okfn.org/data/core/co2-ppm
