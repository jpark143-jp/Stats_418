-- p. 5.2
-- Answer: S2
SELECT 
	store
    , SUM(sales) as total_sales
FROM hw1.sales_data
WHERE DAYOFWEEK(sale_date) = 1	
GROUP BY store
ORDER BY SUM(sales) DESC;

-- p. 5.3
-- Answer: S8, S9, S10
SELECT 
	store
    , SUM(sales) AS total_sales
FROM hw1.sales_data
WHERE MONTH(sale_date) = 12
GROUP BY store
ORDER BY SUM(sales) ASC;

-- p. 5.4
-- Answer: S2
SELECT 
	store
    , COUNT(DISTINCT sale_date) fr_top_sales
FROM	(
	SELECT 
		*
		, ROW_NUMBER() OVER(PARTITION BY sale_date ORDER BY sales DESC) AS rn
	FROM hw1.sales_data
	) top_sale
WHERE top_sale.rn = 1
GROUP BY store
ORDER BY COUNT(DISTINCT sale_date) DESC;

-- p. 5.5
-- Answer: 37th Week in 2019
SELECT 
	WEEK(sale_date) sale_week -- this is out of 52
    , SUM(sales) AS total_sales_all_stores
FROM sales_data
WHERE YEAR(sale_date) = 2019
GROUP BY 1 
ORDER BY 2 DESC;




















