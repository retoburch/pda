SELECT
    f.name country,
    c.name capital_city
FROM cities c
INNER JOIN facts f ON f.id = c.facts_id
WHERE c.capital = 1
LIMIT 10;
