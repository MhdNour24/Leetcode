# Write your MySQL query statement below
select user_id, group_concat(upper(substring(name,1,1)),lower(substring(name,2))) as name
from Users
group by user_id
order by user_id