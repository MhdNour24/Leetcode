# انا ابو عبدو الوحش 
select s1.id,
(
    case
        when s1.id is not null and s2.id is not null 
            then s2.student
        else
            s1.student
    end
) as student
from Seat s1
left join Seat s2 
on s1.id=if(s2.id%2=1,s2.id+1,s2.id-1)
