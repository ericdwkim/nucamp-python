-- customers date_of_birth-non-nullable
-- depends: 20211108_02_ExXab-customers-date-of-birth

ALTER TABLE customers
    ALTER COLUMN date_of_birth SET NOT NULL;