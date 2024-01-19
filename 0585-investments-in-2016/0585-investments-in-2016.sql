select 
    round(sum(tiv_2016),2) as tiv_2016
from 
    Insurance
where 
    tiv_2015 in (
        select tiv_2015 from Insurance
        group by tiv_2015
        having count(tiv_2015)>1

    )
    and 
        concat(lat,lon) in (
            select concat(lat,lon) as can  from Insurance
            group by can
            having count(pid)=1
        ) 
