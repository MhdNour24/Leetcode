-- with cle as (select account_id,
-- (
--     case
--         when income<20000 then 'Low Salary'
--         when income between 20000 and 50000 then 'Average Salary'
--         else 'High Salary'
--     end
-- ) as category
-- from Accounts) 

-- select category,
-- count(account_id)  as accounts_count
-- from cle
-- group by category 
select 'Low Salary' as category,
sum(income<20000) as accounts_count
from Accounts
union 
select 'Average Salary' as category,
sum(income between 20000 and 50000) as accounts_count
from Accounts
union 
select 'High Salary' as category,
sum(income>50000) as accounts_count
from Accounts

