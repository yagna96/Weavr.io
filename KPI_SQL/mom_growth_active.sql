 with active_user_per_month as (select count(distinct user_profile.user_id )as active_user_count,
 user_state.user_state_id as state_id, 
 user_state.user_state as state_name , Month(CREATION_TIMETSAMP) as month, YEAR(CREATION_TIMESTAMP) as year
 from user_profile
 left  join user_state on user_profile.user_state_id = user_state.user_id
 where YEAR(CREATION_TIMESTAMP)== 2024 & user_state.user_state=='active'
 group by Month(CREATION_TIMETSAMP) ),


growth_calculation as  (
    select month, active_user_count , LAG(active_user_count)over(order by month) as previous_month_active_users,
    from active_user_per_month  
),

select month, active_users,previous_month_active_users,
    case
        when previous_month_active_users = then NULL
        else round(((active_users - previous_month_active_users) * 100.0) / previous_month_active_users, 2)
    end as  month_on_month_growth_percentage
from growth_calculation
order by month;
