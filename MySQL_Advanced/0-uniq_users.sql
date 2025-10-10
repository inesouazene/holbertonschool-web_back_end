-- script that creates a table users following some requirements
-- query that creates a table users with the following columns:
    -- id, integer, never null, auto increment and primary key
    -- email, string (255 characters), never null and unique
    -- name, string (255 characters)

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
