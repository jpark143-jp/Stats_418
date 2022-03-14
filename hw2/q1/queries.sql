-- ProbSet2
-- Question 1

SELECT COUNT(*), rating_bin
FROM (SELECT round(rating, 0) AS rating_bin FROM movieratings)
GROUP BY Rating
HAVING Number_of_votes > 1000
