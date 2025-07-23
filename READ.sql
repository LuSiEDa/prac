USE practice01;

SELECT name, salary FROM practice01.employees;

-- Frontend 직챙 중 연봉 90000 이하

SELECT name, salary FROM employees 
WHERE position = 'Frontend' and salary <=90000;

SELECT * FROM employees WHERE position = 'PM'

-- 모든 직원의 포지션 별 평균 연

SELECT position, AVG(salary) FROM employees
GROUP BY position; 