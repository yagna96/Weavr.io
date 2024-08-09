with user_state_count as ( select user_state.state,
        count(distinct us.user_id) as user_count
    from
        user_state  
        right join user_profile on user_profile.user_state_id = user_state.user_id
    group by
        user_state.state
),
total_users as (
    select  
        sum(user_count) AS total_user_count
    from user_state_count
)
select
    usc.state,
    usc.user_count,
    tu.total_user_count,
    ROUND((usc.user_count * 100.0) / tu.total_user_count, 2) AS percentage_of_users
FROM 
    user_state_count usc
CROSS JOIN 
    total_users tu
ORDER BY 
    usc.state;
