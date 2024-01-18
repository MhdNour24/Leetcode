with t2 as (
    select accepter_id as requester_id,
    requester_id as accepter_id ,
    accept_date 
    from RequestAccepted
)

select requester_id as id,
count(accepter_id) as num
from 
(select * from RequestAccepted 
union 
select * from t2) as tab
group by requester_id
order by num desc
limit 1