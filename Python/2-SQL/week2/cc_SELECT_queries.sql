-- my attempt:

SELECT company_name FROM customers
WHERE company_name LIKE 'Q' BETWEEN 'Z'
ORDER BY company_name DESC;

-- solution/answer:

SELECT company_name FROM customers 
WHERE company_name >= 'Q' ORDER BY company_name DESC;

-- makes sense since alphabet is probably mapped to numbers in backend code from
-- 1 - 26, so defining WHERE clause as >= 'Q' sets it from >= 16 .... -> 26 inclusive

-------------------------------------------------------------------------------
-- my attempt:

SELECT first_name, last_name FROM employees
WHERE title = 'Sales Representative'
ORDER BY last_name;

-- solution/answer:

SELECT first_name, last_name FROM employees
WHERE title = 'Sales Representative'
ORDER BY last_name, first_name;

-- Question: "sort by last_name, and within the same last name, sort by first_name"
        --  da fuck does that last part mean?!!

-------------------------------------------------------------------------------

-- my attempt:

SELECT first_name, home_phone FROM employees
WHERE first_name LIKE 'A%', home_phone LIKE '%4%'
ORDER BY employee_id;

-- solution/answer:

SELECT first_name, home_phone FROM employees 
WHERE first_name LIKE 'A%' AND home_phone LIKE '%4%' 
ORDER BY employee_id;

-- makes sense to use logical operator `AND` so that both conditional expressions
-- must evaluate to TRUE for the query to be successful; using a comma would make it
-- a tuple (question?)
 