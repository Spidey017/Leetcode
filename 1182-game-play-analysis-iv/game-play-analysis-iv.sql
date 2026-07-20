# Write your MySQL query statement below
SELECT
    ROUND(
        COUNT(DISTINCT a.player_id) /
        COUNT(DISTINCT b.player_id),
        2
    ) AS fraction
FROM Activity b
LEFT JOIN Activity a
ON b.player_id = a.player_id
AND a.event_date = DATE_ADD(
    (
        SELECT MIN(event_date)
        FROM Activity
        WHERE player_id = b.player_id
    ),
    INTERVAL 1 DAY
);