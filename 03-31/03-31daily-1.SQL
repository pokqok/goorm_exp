CREATE DATABASE IF NOT EXISTS customer_db;
USE customer_db;

-- 테이블 생성 
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NULL,
    email VARCHAR(100) NULL,
    age INT NULL,
    gender VARCHAR(10) NULL,
    city VARCHAR(50) NULL
);

-- 데이터 삽입 
INSERT INTO customers VALUES
(1, '홍길동', 'hong@example.com', 28, '남', '서울'),
(2, '김영희', NULL, NULL, '여', '부산'),
(3, '이철수', 'lee@example.com', 35, NULL, '대구'),
(4, NULL, 'choi@example.com', 42, '남', NULL),
(5, '박민수', NULL, NULL, NULL, '서울');

