CREATE DATABASE sns;
USE sns;

CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    age INT,
    join_date DATE
);

CREATE TABLE posts (
    id INT PRIMARY KEY,
    user_id INT,
    content TEXT,
    view_count INT,
    ad_revenue DECIMAL(10, 2),
    is_public BOOLEAN,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
