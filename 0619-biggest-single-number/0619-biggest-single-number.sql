select max(num) as num
from 
(select mn1.num
from MyNumbers mn1
inner join MyNumbers mn2
on mn1.num=mn2.num
group by mn2.num
having count(mn2.num)=1) as tab
;
