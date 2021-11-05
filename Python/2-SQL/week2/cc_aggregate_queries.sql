-- my attempt:
SELECT customer_id, order_date FROM orders 
ORDER BY customer_id;

-- solution/answer:

SELECT customer_id, MIN(order_date) FROM orders 
GROUP BY customer_id 
ORDER BY customer_id;

-- explanation: "list the customer_id and the order_date OF THEIR *FIRST* ORDER" that is,
-- get both columns, but in the order where it starts at the oldest order_date b/c oldest
-- order date = the most first order

