# Write your MySQL query statement below
select * from Cinema
where Cinema.id%2=1 and Cinema.description !='boring' 
order by Cinema.rating desc