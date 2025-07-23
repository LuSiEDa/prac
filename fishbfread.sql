-- CREATE DATABASE fishbread_db;
USE fishbread_db;

CREATE TABLE users (
	user_id int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) UNIQUE,
    is_business BOOLEAN DEFAULT FALSE

);

CREATE TABLE orders(
	oder_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE inventory(
	item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL
);

CREATE TABLE sales(
	sale_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id VARCHAR(255) NOT NULL,
    item_id INT,
    quantity_sold INT NOT NULL,
	FOREIGN KEY (order_id) REFERENCES orders(order_id),
	FOREIGN KEY (item_id) REFERENCES inventory(item_id)
    
);

CREATE TABLE daily_sales(
	date DATE PRIMARY KEY,
    total_sales DECIMAL(10,2) NOT NULL
);


INSERT INTO users (name, age, email)
VALUES 
	('김사람' , '87', '123@'),
	('이사람' , '102', 'dfnjf@'),
    ('박사람' , '4', 'feicj22@');
    
SELECT * FROM users;
SELECT name FROM users;
SELECT * FROM users WHERE age >= 30;

