select
    user_id
    ,max(consec_days) as max_consec_days
from
(
    select
        user_id
        ,bdate
        ,count(1) as consec_days
    from
    (
        select
            user_id
            ,fdate
            ,date_sub(fdate, interval rk day) as bdate
        from
        (
            select
                user_id
                ,fdate
                ,ROW_NUMBER() OVER(PARTITION BY user_id order by fdate) as rk
            from tb_dau
        )t1
    )t1
    group by user_id,bdate
)t1
group by user_id