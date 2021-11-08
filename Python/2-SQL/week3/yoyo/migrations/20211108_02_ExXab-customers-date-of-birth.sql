-- customers date_of_birth
-- depends: 20211108_01_l0i46-customers-table

ALTER TABLE customers
    ADD COLUMN date_of_birth TIMESTAMP;