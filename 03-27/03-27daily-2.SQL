use movie;
-- 문제 1: 영화를 시청한 사용자와 영화 제목
SELECT DISTINCT u.name AS user_name, m.title AS movie_title
FROM users u
JOIN watch_history wh ON u.user_id = wh.user_id
JOIN movies m ON wh.movie_id = m.movie_id;

-- 문제 2: 장르별 시청 횟수
SELECT m.genre, COUNT(*) AS view_count
FROM watch_history wh
JOIN movies m ON wh.movie_id = m.movie_id
GROUP BY m.genre;

-- 문제 3: 총 시청 시간 1000분 이상인 사용자
SELECT u.name AS user_name, SUM(wh.duration) AS total_duration
FROM users u
JOIN watch_history wh ON u.user_id = wh.user_id
GROUP BY u.name
HAVING total_duration >= 1000;

-- 문제 4: VIP 사용자의 액션 영화 시청 내역
SELECT DISTINCT u.name AS user_name, m.title AS movie_title
FROM users u
JOIN watch_history wh ON u.user_id = wh.user_id
JOIN movies m ON wh.movie_id = m.movie_id
WHERE u.subscription = 'vip' AND m.genre = '액션';

-- 문제 5: 가장 많이 시청된 영화
SELECT m.title AS movie_title, COUNT(*) AS view_count
FROM watch_history wh
JOIN movies m ON wh.movie_id = m.movie_id
GROUP BY m.title
ORDER BY view_count DESC
LIMIT 1;

-- 문제 6: 구독 유형별 평균 시청 시간
SELECT subscription, 
       (SELECT AVG(duration) 
        FROM watch_history 
        WHERE user_id IN (
            SELECT user_id 
            FROM users 
            WHERE subscription = u.subscription
        )) AS avg_duration
FROM users u
GROUP BY subscription;
