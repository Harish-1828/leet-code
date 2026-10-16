# Write your MySQL query statement bel
select MAX(num) as num from MyNumbers where num IN (select max(num) from Mynumbers group by num  having count(*)=1) 