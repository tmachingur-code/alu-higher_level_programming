-- Displays the maximum temperature of each state
-- Calculate maximum temperature and order by state name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
