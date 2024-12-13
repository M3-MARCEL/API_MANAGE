CREATE DATABASE IF NOT EXISTS api_manage CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

USE api_manage;

-- Tabla albums
CREATE TABLE IF NOT EXISTS albums (
    id INT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL
);

-- Tabla photos
CREATE TABLE IF NOT EXISTS photos (
    id INT PRIMARY KEY,
    album_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    thumbnail_url VARCHAR(255) NOT NULL,
    FOREIGN KEY (album_id) REFERENCES albums(id)
);