# Write your MySQL query statement below
select contest_id,
(round(count(Register.user_id)/(select count(*) from Users)*100,2)) as percentage
from Register
left join Users
on Users.user_id=Register.user_id
group by contest_id
order by percentage desc,contest_id asc