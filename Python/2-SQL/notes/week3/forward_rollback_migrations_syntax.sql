        -- SET NOT NULL Migration

-- Forward migration

ALTER TABLE customers
ALTER COLUMN date_of_birth SET NOT NULL;

-- Rollback migration

ALTER TABLE customers
ALTER COLUMN date_of_birth DROP NOT NULL;

--------------------------------------------
        -- SET DEFAULT Migration
-- Forward migration

ALTER TABLE customers
ALTER COLUMN date_of_birth SET DEFAULT now();

-- Rollback migration

ALTER TABLE customers
ALTER COLUMN date_of_birth DROP DEFAULT;


--------------------------------------------
        -- RENAME COLUMN Migration
-- Forward migration

ALTER TABLE customers
RENAME COLUMN date_of_birth TO dob;

-- Rollback migration

ALTER TABLE customers
RENAME COLUMN dob TO date_of_birth;

---------------------------------------------
        -- CREATE TABLE migration

-- Forward migration
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    dollar_amt_spent NUMERIC,
    customer_id INT NOT NULL,
    CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers (id)
        ON DELETE CASCADE
);

-- Rollback migration
DROP TABLE orders;

--------------------------------------------
            -- DROP CONSTRAINT migration

-- Forward migration

ALTER TABLE orders
DROP CONSTRAINT fk_orders_customers;

-- Rollabck migration
ALTER TABLE orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customer_id)
REFERENCES customers(id)
ON DELETE CASCADE;

--------------------------------------------
        -- Multi-statement migration

-- Forward migration
CREATE TABLE table1 (id SERIAL PRIMARY KEY);
CREATE TABLE table2 (id SERIAL PRIMARY KEY);
CREATE TABLE table3 (id SERIAL PRIMARY KEY);

-- Rollabck migration; *NOTE: the tables are dropped in reverse order
DROP TABLE table3;
DROP TABLE table2;
DROP TABLE table1;