-- 데이터베이스 생성
CREATE DATABASE GameConnect;
USE GameConnect;

-- User 테이블
CREATE TABLE User (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    join_date DATE NOT NULL
);

-- Game 테이블
CREATE TABLE Game (
    game_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    platform VARCHAR(50) NOT NULL
);

-- PlayLog 테이블
CREATE TABLE PlayLog (
    user_id INT,
    game_id INT,
    play_date DATE NOT NULL,
    play_time_minutes INT NOT NULL,
    PRIMARY KEY (user_id, game_id, play_date),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (game_id) REFERENCES Game(game_id)
);

-- Friendship 테이블
CREATE TABLE Friendship (
    user_id1 INT,
    user_id2 INT,
    since_date DATE NOT NULL,
    PRIMARY KEY (user_id1, user_id2),
    FOREIGN KEY (user_id1) REFERENCES User(user_id),
    FOREIGN KEY (user_id2) REFERENCES User(user_id)
);

-- Review 테이블
CREATE TABLE Review (
    review_id INT PRIMARY KEY,
    user_id INT,
    game_id INT,
    rating INT NOT NULL,
    comment TEXT,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (game_id) REFERENCES Game(game_id)
);

-- GameRecommendation 테이블
CREATE TABLE GameRecommendation (
    from_user INT,
    to_user INT,
    game_id INT,
    rec_date DATE NOT NULL,
    PRIMARY KEY (from_user, to_user, game_id),
    FOREIGN KEY (from_user) REFERENCES User(user_id),
    FOREIGN KEY (to_user) REFERENCES User(user_id),
    FOREIGN KEY (game_id) REFERENCES Game(game_id)
);