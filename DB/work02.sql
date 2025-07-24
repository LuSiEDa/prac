CREATE TABLE PetOwners(
	owners_id INT AUTO_INCREMENT PRIMARY KEY,
    name CHAR(50) NOT NULL,
    contact INT(10) NOT NULL
);

CREATE TABLE pet(
	pet_id INT AUTO_INCREMENT PRIMARY KEY,
    pet_name VARCHAR(10) NOT NULL,
    species VARCHAR(10) NOT NULL,
    breed VARCHAR(10) NOT NULL
);

CREATE TABLE reserve(
	reserve_id INT AUTO_INCREMENT PRIMARY KEY,
    start DATE NOT NULL,
    end DATE NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pet(pet_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    roomNumber VARCHAR(50) NOT NULL UNIQUE,
    roomType VARCHAR(10), NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    serviceName VARCHAR(10),
    servicePrice VARCHAR(10),
    FOREIGN KEY (reserve_id) REFERENCES reserve(reserve_id)
);
