select CONCAT(YEAR(trans_date), '-', LPAD(MONTH(trans_date), 2, '0')) as month,
country,
count(amount) as trans_count,
count(if(state='approved',1,null)) as approved_count,
sum(amount) as trans_total_amount,
sum(if(state='approved',amount,0)) as approved_total_amount
from Transactions 
group by date_format(trans_date,'%y-%m'),country
