-- p. 5.1
-- 1. Creating a db
CREATE DATABASE hw1;

-- 2. Creating tables
-- Creating a table just like the csv.file
CREATE TABLE hw1.sales_test (
	'Date' as DATE
    , 'S1' INT
    , 'S2' INT
    , 'S3' INT
    , 'S4' INT
    , 'S5' INT 
    , 'S6' INT
    , 'S7' INT
    , 'S8' INT
    , 'S9' INT
    , 'S10' INT
	, PRIMARY KEY ('Date')
);

-- Transforming sales_test table structure to create sales_data table 
CREATE TABLE hw1.sales_data (
	'sale_date' as DATE
    , 'store_ID' STRING
    , 'sales' INT
	, PRIMARY KEY ('sale_date')
    , FOREIGN KEY ('store_ID')
);

-- Creating a store table (Since we don't have store information, we will leave it blank.)
CREATE TABLE hw1.store_info (
	'store_ID' STRING
    , 'store_name' VARCHAR(255)
    , 'store_address' VARCHAR(255)
    , 'store_city' VARCHAR(255)
    , 'store_zip' VARCHAR(255)
    , 'store_phone' VARCHAR(15)
    , PRIMARY KEY ('store_ID')
);

-- 2. Import TV_Sales.csv
LOAD DATA INFILE 'c:/TV_Sales.csv' 
INTO TABLE sales_test
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

-- 3. Importing values from sales_test to sales_data
-- 3.1 s1
CREATE TABLE hw1.sales_data AS
SELECT date	AS sale_date
	, 's1' AS store
    , s1 AS sales
FROM hw1.store_sales
-- 3.2 s2
UNION 
SELECT date	AS sale_date
	, 's2' AS store
    , s2 AS sales
FROM hw1.store_sales
-- 3.3 s3
UNION 
SELECT date	AS sale_date
	, 's3' AS store
    , s3 AS sales
FROM hw1.store_sales
-- 3.4 s.4
UNION 
SELECT date	AS sale_date
	, 's4' AS store
    , s4 AS sales
FROM hw1.store_sales
-- 3.5 s.5
UNION 
SELECT date	AS sale_date
	, 's5' AS store
    , s5 AS sales
FROM hw1.store_sales
-- 3.6 s.6
UNION 
SELECT date	AS sale_date
	, 's6' AS store
    , s6 AS sales
FROM hw1.store_sales
-- 3.7 s.7
UNION
SELECT date	AS sale_date
	, 's7' AS store
    , s7 AS sales
FROM hw1.store_sales
-- 3.8 s.8
UNION 
SELECT date	AS sale_date
	, 's8' AS store
    , s8 AS sales
FROM hw1.store_sales
-- 3.9 s.9
UNION 
SELECT date	AS sale_date
	, 's9' AS store
    , s9 AS sales
FROM hw1.store_sales
-- 3.10 s.10
UNION 
SELECT date	AS sale_date
	, 's10' AS store
    , s10 AS sales
FROM hw1.store_sales
;