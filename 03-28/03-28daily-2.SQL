-- User 데이터
INSERT INTO User (user_id, username, join_date) VALUES
(1, 'alice', '2023-01-10'),
(2, 'bob', '2023-02-15'),
(3, 'charlie', '2023-03-01'),
(4, 'diana', '2023-03-10'),
(5, 'eric', '2023-04-05');

-- Game 데이터
INSERT INTO Game (game_id, title, genre, platform) VALUES
(101, 'Apex Legends', 'FPS', 'PC'),
(102, 'Zelda: Breath of the Wild', 'Adventure', 'Switch'),
(103, 'Stardew Valley', 'Simulation', 'PC'),
(104, 'Overwatch 2', 'FPS', 'PC'),
(105, 'Hollow Knight', 'Metroidvania', 'PC');

-- PlayLog 데이터
INSERT INTO PlayLog (user_id, game_id, play_date, play_time_minutes) VALUES
(1, 101, '2023-05-01', 120),
(2, 101, '2023-05-02', 200),
(3, 101, '2023-05-03', 180),
(1, 102, '2023-05-04', 90),
(4, 103, '2023-05-05', 240),
(5, 104, '2023-05-06', 60),
(3, 105, '2023-05-07', 150),
(3, 103, '2023-05-08', 100);

-- Friendship 데이터
INSERT INTO Friendship (user_id1, user_id2, since_date) VALUES
(1, 2, '2023-04-01'),
(1, 3, '2023-04-02'),
(2, 4, '2023-04-03'),
(2, 5, '2023-04-04'),
(3, 4, '2023-04-05');

-- Review 데이터
INSERT INTO Review (review_id, user_id, game_id, rating, comment) VALUES
(201, 1, 101, 5, 'Awesome game'),
(202, 2, 101, 4, 'Fast paced'),
(203, 3, 101, 5, 'Very competitive'),
(204, 1, 102, 4, 'Beautiful world'),
(205, 3, 103, 5, 'Very relaxing'),
(206, 4, 103, 4, 'Charming'),
(207, 3, 105, 4, 'Challenging'),
(208, 2, 105, 3, 'Too hard');

-- GameRecommendation 데이터
INSERT INTO GameRecommendation (from_user, to_user, game_id, rec_date) VALUES
(1, 3, 101, '2023-06-01'),
(2, 3, 105, '2023-06-02'),
(4, 3, 103, '2023-06-03'),
(3, 1, 105, '2023-06-04');