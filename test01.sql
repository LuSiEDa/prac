USE testdatabase;

CREATE TABLE users(
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT
)

-- INSERT INTO