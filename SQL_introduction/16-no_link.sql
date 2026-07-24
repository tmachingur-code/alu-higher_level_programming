-- Lists records from second_table that have a name value
-- Display score and name ordered by highest score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
