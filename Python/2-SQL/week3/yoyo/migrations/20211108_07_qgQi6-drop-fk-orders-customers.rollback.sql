-- drop fk orders customers
-- depends: 20211108_06_2AU6O-create-orders

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customer_id)
REFERENCES customers(id)
ON DELETE CASCADE;
