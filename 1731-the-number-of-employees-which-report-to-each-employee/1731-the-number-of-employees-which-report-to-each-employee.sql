# Write your MySQL query statement below
select employee_id,name,reports_count,average_age
from Employees
inner join 
(select reports_to,ROUND(avg(age)) as average_age ,count(name) as reports_count
from Employees  
group by reports_to
having reports_to is not null) as Employees2
on Employees.employee_id=Employees2.reports_to
order by employee_id asc
