-- Power users definition:
-- Highest number of purchases in the last one year

SELECT u.username,COUNT(*) as NumOfPurchases from users u 
JOIN purchases p
ON u.user_id = p.user_id
WHERE p.purchase_date > '2020-06-30' and p.purchase_date < '2021-06-30'
GROUP BY u.username
ORDER BY COUNT(*) DESC
LIMIT 10 