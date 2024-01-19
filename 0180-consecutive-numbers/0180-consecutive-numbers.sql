with cle as (select *,
lead(num,1,null) over(order by id) as lead_num,
lag(num,1,null) over(order by id) as lag_num
from Logs)

 select distinct num as ConsecutiveNums from cle
 where num=lead_num and num=lag_num