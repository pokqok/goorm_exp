create database movie;
use movie;

-- users 테이블 
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    subscription VARCHAR(20)
);

-- movies 테이블
CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(50)
);

-- watch_history 테이블
CREATE TABLE watch_history (
    history_id INT PRIMARY KEY,
    user_id INT,
    movie_id INT,
    watched_at DATETIME,
    duration INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

-- users 데이터
INSERT INTO users (user_id, name, subscription) VALUES
(1, '민수', 'vip'),
(2, '지현', 'premium'),
(3, '철수', 'free'),
(4, '영희', 'vip'),
(5, '나영', 'free');

-- movies 데이터
INSERT INTO movies (movie_id, title, genre) VALUES
(101, '어벤져스', '액션'),
(102, '라라랜드', '로맨스'),
(103, '인사이드 아웃', '애니메이션'),
(104, '기생충', '드라마'),
(105, '인터스텔라', 'SF');

-- watch_history 데이터
INSERT INTO watch_history (history_id, user_id, movie_id, watched_at, duration) VALUES
(1001, 1, 101, '2024-10-01 20:00:00', 120),
(1002, 1, 102, '2024-10-02 21:00:00', 110),
(1003, 2, 103, '2024-10-03 19:30:00', 90),
(1004, 3, 104, '2024-10-04 18:00:00', 130),
(1005, 3, 101, '2024-10-05 17:00:00', 120),
(1006, 4, 101, '2024-10-06 16:00:00', 115),
(1007, 4, 105, '2024-10-07 15:00:00', 140),
(1008, 5, 103, '2024-10-08 14:00:00', 95),
(1009, 2, 101, '2024-10-09 13:00:00', 125),
(1010, 1, 105, '2024-10-10 12:00:00', 130);