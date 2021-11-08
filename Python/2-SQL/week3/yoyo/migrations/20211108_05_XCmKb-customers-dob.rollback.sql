-- customers dob
-- depends: 20211108_04_gojIQ-customers-date-of-birth-default

ALTER TABLE customers
    RENAME COLUMN dob TO date_of_birth;