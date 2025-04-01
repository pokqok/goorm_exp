INSERT IGNORE INTO customers (name, email, age, city) 
VALUES ('김철수', 'kim@example.com', 28, 'Seoul');

SELECT name, age 
FROM customers 
WHERE age >= 30;

SELECT * 
FROM products 
WHERE price >= 100000 AND stock <= 10;

SELECT email 
FROM customers 
WHERE city = 'Seoul';

SELECT * 
FROM orders 
WHERE order_date >= '2024-01-01';

UPDATE customers 
SET email = 'kimcs@example.com' 
WHERE name = '김철수';

UPDATE products 
SET stock = 25 
WHERE name = 'AirPods Pro';

DELETE FROM customers 
WHERE city = 'Busan';

DELETE FROM products 
WHERE stock = 0;

SELECT * FROM customers;
