-- Top customers by total transaction volume
SELECT
    c.customer_id,
    c.name,
    SUM(t.amount) AS total_transaction_amount
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
JOIN transactions t ON a.account_id = t.account_id
GROUP BY c.customer_id, c.name
ORDER BY total_transaction_amount DESC
LIMIT 10;



