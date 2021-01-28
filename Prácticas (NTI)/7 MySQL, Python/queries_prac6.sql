-- 2)
select * from meterlogs.logs;
-- 3)
select time,date,kwh from meterlogs.logs;
-- 4)
select time,date,kwh 
from meterlogs.logs 
where meterlogs.logs.date = str_to_date('2019-02-26','%Y-%m-%d')
	and meterlogs.logs.time between cast(('21:00:00') as time(0))
    and cast(('22:00:00') as time(0))