-- customers date_of_birth-default
-- depends: 20211108_03_ZofuV-customers-date-of-birth-non-nullable

ALTER TABLE customers
    ALTER COLUMN date_of_birth SET DEFAULT now();