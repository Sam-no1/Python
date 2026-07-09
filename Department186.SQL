# Write your MySQL query statement below
WITH filtered_stadium AS(
    SELECT *, 
        id - ROW_NUMBER() OVER (ORDER BY id) AS streak_group
        FROM Stadium
        WHERE people >= 100
),
valid_groups AS (
    SELECT streak_group
    FROM filtered_stadium
    GROUP BY streak_group
    HAVING COUNT(*)>3
)
SELECT * e
FROM filtered_stadium
