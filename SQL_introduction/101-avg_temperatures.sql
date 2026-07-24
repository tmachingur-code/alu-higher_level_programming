-- Displays the average temperature by city
-- Calculate average values and order by highest average
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
