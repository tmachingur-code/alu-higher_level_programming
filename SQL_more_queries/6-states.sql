-- Creates the hbtn_0d_usa database and states table

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create states table if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
