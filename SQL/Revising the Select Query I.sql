-- Name : Revising the Select Query I
-- Link : https://www.hackerrank.com/challenges/revising-the-select-query/problem
-- Difficulty : Easy
-- Programming language : MySQL

SELECT *
FROM CITY
WHERE COUNTRYCODE = 'USA' and POPULATION > 100000
