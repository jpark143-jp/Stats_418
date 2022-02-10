-- ProbSet1
-- 5.2

SELECT 
	store
    , SUM(sales) as total_sales
FROM hw1.sales_data
WHERE DAYOFWEEK(sale_date) = 1	
GROUP BY store
ORDER BY SUM(sales) DESC;

-- S2 makes the maximum sales on Sundays


-- 5.3
SELECT 
	store
    , SUM(sales) AS total_sales
FROM hw1.sales_data
WHERE MONTH(sale_date) = 12
GROUP BY store
ORDER BY SUM(sales) ASC;

-- S8, S9, S10 are the stores with total sales in Dec lower than those of S5.


-- 5.4
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

-- S2 recorded the highest number of sales for the largest number of days.


-- 5.5
SELECT 
	WEEK(sale_date) sale_week -- this is out of 52
    , SUM(sales) AS total_sales_all_stores
FROM sales_data
WHERE YEAR(sale_date) = 2019
GROUP BY 1 
ORDER BY 2 DESC;

-- 2019, 37th week has the highest total sales across all the stores. 


















