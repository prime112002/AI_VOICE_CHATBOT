CREATE DATABASE  voice_bot_db;
USE voice_bot_db;

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    account_number VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS queries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_query TEXT,
    response TEXT,
    response_time FLOAT
);