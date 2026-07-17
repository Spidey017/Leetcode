SELECT id, num
FROM (
    SELECT id,
           COUNT(*) AS num,
           DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
    FROM (
        SELECT requester_id AS id
        FROM RequestAccepted

        UNION ALL

        SELECT accepter_id
        FROM RequestAccepted
    )
    GROUP BY id
)
WHERE rnk = 1;