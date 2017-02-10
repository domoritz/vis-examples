# Vis examples

## Consumer complaints

```bash
csvsql --db sqlite:///complaints.db Consumer_Complaints.csv -y 1000 --insert
```

```sql
select "Date received", "Product", "Sub-product", "Company", "State", "ZIP code", "Consumer consent provided?", "Submitted via", "Timely response?", "Consumer disputed?"
from Consumer_Complaints
where "Date received" like '2012%' or "Date received" like '2013%' or "Date received" like '2014%' or "Date received" like '2015%' or "Date received" like '2016%'
order by random()
limit 100000
```