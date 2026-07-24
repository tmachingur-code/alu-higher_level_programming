-- Displays average temperature by city
-- Calculate average temperature and order by highest average
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
