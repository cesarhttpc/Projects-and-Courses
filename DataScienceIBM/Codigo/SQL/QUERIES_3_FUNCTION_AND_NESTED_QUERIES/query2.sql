-- Sub - queries and Nested Selects
-- Try the following code: (Illegal use of group function)
SELECT * FROM EMPLOYEES WHERE salary < AVG(salary);

-- SELECT *
FROM EMPLOYEES WHERE SALARY < 
    (
        SELECT AVG(SALARY)
        FROM EMPLOYEES
    );

SELECT EMP_ID, SALARY, (
        SELECT MAX(SALARY)
        FROM EMPLOYEES
    ) AS MAX_SALARY
FROM EMPLOYEES;

SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE
    B_DATE = (
        SELECT MIN(B_DATE)
        FROM EMPLOYEES
    );

-- You may also use sub-queries to create derived tables, which can then be used to query specific information. Say you want to know the average salary of the top 5 earners in the company. You will first have to extract a table of the top five salaries as a table. From that table, you can query the average value of the salary. The query can be written as follows:


SELECT AVG(SALARY)
FROM (
        SELECT SALARY
        FROM EMPLOYEES
        ORDER BY SALARY DESC
        LIMIT 5
    ) AS SALARY_TABLE;

-- 
-- 
-- 
-- 
-- Excercise 2
SELECT * FROM EMPLOYEES WHERE B_DATE < (SELECT AVG(B_DATE) FROM EMPLOYEES) ;