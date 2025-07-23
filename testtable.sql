-- CREATE DATABASE testdatabase;
-- USE testdatabase;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

INSERT INTO users (user_id, name, age)
VALUES (1, 'Alice', 25),
       (2, 'Bob', 30),
       (3, 'Charlie', 22),
       (4, 'David', 33),
       (5, 'Eve', 28);
       
CREATE TABLE orders(
	order_id INT PRIMARY KEY,
    user_id INT,
    oder_date DATE

);

INSERT INTO orders (order_id, user_id, order_date)
VALUES (101, 1, '2023-01-01'),
       (102, 2, '2023-02-01'),
       (103, 1, '2023-02-15'),
       (104, 3, '2023-03-01'),
       (105, 4, '2023-03-10');

