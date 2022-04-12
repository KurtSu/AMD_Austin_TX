/**
  * Coding excrcises written for the position of 
  * https://jobs.amd.com/job/Austin-Software-Development-Engineer-1-Texa/853677600/
  * author: Tianwen Su
  */
  
/* task 1 */
SELECT Brand, Name, Price,
            RANK() OVER(
				PARTITION BY Brand ORDER BY Price DESC) AS r
FROM product_price;

/* task 2 */
SELECT Brand, Name, Price, r
FROM
(
	SELECT Brand, Name, Price,
            RANK() OVER(
				PARTITION BY Brand ORDER BY Price DESC) AS r
	FROM product_price
) AS t
WHERE r = 2;
