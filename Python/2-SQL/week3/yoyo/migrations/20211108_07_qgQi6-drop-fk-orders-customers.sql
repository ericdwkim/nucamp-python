-- drop fk orders customers
-- depends: 20211108_06_2AU6O-create-orders

ALTER TABLE orders
DROP CONSTRAINT fk_orders_customers;
