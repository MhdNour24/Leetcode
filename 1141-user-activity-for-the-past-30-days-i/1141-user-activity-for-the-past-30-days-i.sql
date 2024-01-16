select activity_date as day,
count(DISTINCT user_id) as active_users
from Activity
group by activity_date
having activity_date<='2019-07-27' and date_add(activity_date,interval 30 day)>'2019-07-27';
