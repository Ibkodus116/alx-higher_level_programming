-- A script that lists all records of the table
-- Query the DB for all
SELECT score, name FROM second_table WHERE name is not NULL 
GROUP BY score, name
ORDER BY score DESC
