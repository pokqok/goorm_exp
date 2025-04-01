-- 1: 나만의 햄버거 추가하기
INSERT INTO burgers (id, name, price, gram, kcal, protein)
VALUES (3, 'cheese Burger', 6500, 350, 650, 40);

-- 2: 고객 테이블 먼저 생성
CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  age INTEGER,
  favorite_burger VARCHAR(50)
);

INSERT INTO customers (id, name, age, favorite_burger)
VALUES (1, '안효서', 24, '.Cheese Burger');

-- 3 : 음료 테이블 생성
CREATE TABLE drinks (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  price INTEGER,
  ml INTEGER
);

INSERT INTO drinks (id, name, price, ml)
VALUES (1, 'water', 3500, 400);

-- 보너스 과제
CREATE TABLE sauces (
  id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  price INTEGER
);

INSERT INTO sauces (id, name, price)
VALUES (1, 'Spicy Sauce', 500);