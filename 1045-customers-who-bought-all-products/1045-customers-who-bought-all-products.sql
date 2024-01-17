-- select tab.customer_id
-- (select customer_id,count(product_key) as count_product
-- from Customer
-- group by customer_id) as tab
-- where tab.count_product=select
select customer_id from 
(select customer_id,count(distinct product_key) as count_product,(select count(product_key) from Product) as toplam
from Customer
group by customer_id) as tab
where count_product=toplam