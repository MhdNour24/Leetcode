# Write your MySQL query statement below
with cle as (SELECT product_id,
       SUM(unit) AS unit
FROM Orders
WHERE YEAR(order_date) = 2020 AND MONTH(order_date) = 2
GROUP BY product_id)

select product_name,unit from cle 
inner join Products p
on cle.product_id=p.product_id
where unit>=100