-- 1. 이름이 NULL인 경우 '이름없음'으로 대체
SELECT 
    customer_id, 
    COALESCE(name, '이름없음') AS name, 
    email, 
    age, 
    gender, 
    city
FROM customers;

-- 2. 나이 정보 전처리 (NULL인 경우 평균 나이로 대체)
SELECT 
    customer_id, 
    name, 
    email, 
    COALESCE(age, ROUND((SELECT AVG(age) FROM customers WHERE age IS NOT NULL), 1)) AS age, 
    gender, 
    city
FROM customers;

-- 3. 이메일이 없는 고객 수 구하기
SELECT COUNT(*) as null_email_count
FROM customers 
WHERE email IS NULL;

-- 4. 서울 거주 && 성별이 NULL인 고객 ID 조회
SELECT customer_id
FROM customers
WHERE city = '서울' AND gender IS NULL;

-- 5. NULL 값이 하나라도 있는 고객 행 조회
SELECT *
FROM customers
WHERE name IS NULL 
   OR email IS NULL 
   OR age IS NULL 
   OR gender IS NULL 
   OR city IS NULL;