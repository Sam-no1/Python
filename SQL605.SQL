# Write your MySQL query statement below
WITH checks as (
    SELECT *,
        id - ROW_NUMBER() OVER (order by id) as seq
    FROM 
        Stadium
        WHERE people >= 100
),
valid as (
    SELECT 
        seq
    FROM
        checks
        GROUP BY seq
        HAVING count(*)>=3
)
SELECT
    id, visit_date, people
FROM
    checks 
    where seq IN (SELECT seq FROM valid)
    ORDER BY 3 asc;