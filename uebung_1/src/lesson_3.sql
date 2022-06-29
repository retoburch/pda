SELECT
    c.name city,
    f.name country,
    c.population population
FROM facts f
INNER JOIN (
            SELECT * FROM cities
            WHERE capital = 0
            AND population > 10000000
           ) c ON c.facts_id = f.id
ORDER BY 3 DESC;