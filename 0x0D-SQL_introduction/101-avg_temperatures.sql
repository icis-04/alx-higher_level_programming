-- Temperature average
IMPORT TABLE
SELECT city, AVG(value) AS 'avg_temp'
FROM temperature
GROUP BY city
ORDER BY value DESC;
