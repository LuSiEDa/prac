USE practice01;

-- pm 연봉 10퍼 인상
UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM'; 

-- 백엔드 연봉 5퍼 인상
UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';