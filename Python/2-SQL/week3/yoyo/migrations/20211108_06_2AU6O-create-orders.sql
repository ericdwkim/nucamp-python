-- create orders
-- depends: 20211108_05_XCmKb-customers-dob

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    dollar_amt_spent NUMERIC,
    customer_id INT NOT NULL,
    CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers (id)
        ON DELETE CASCADE
);
