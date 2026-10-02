# Write your MySQL query statement below
select a.machine_id,
        ROUND(AVG(ABS(b.timestamp - a.timestamp)),3) AS processing_time from 
        Activity a INNER join Activity b on a.process_id=b.process_id and a.machine_id=b.machine_id where a.activity_type='start' and b.activity_type='end' Group by machine_id;