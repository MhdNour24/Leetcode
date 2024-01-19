with cle as (SELECT 
  * ,
  @cumulative := @cumulative + weight  AS new_weight 
FROM 
  Queue,
  (SELECT @cumulative := 0) AS init
order by turn 
)
select person_name from cle
where new_weight<=1000
order by new_weight desc
limit 1