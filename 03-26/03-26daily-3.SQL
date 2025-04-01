-- Users 데이터 삽입
INSERT INTO users (id, username, age, join_date) VALUES
(1, 'alice', 25, '2024-01-10'),
(2, 'bob', 32, '2024-01-15'),
(3, 'charlie', 41, '2024-02-01');

-- Posts 데이터 삽입
INSERT INTO posts (id, user_id, content, view_count, ad_revenue, is_public, created_at) VALUES
(101, 1, 'Hello world!', 120, 15.50, TRUE, '2025-03-20 09:00'),
(102, 2, 'Good morning', 300, 42.75, TRUE, '2025-03-20 10:30'),
(103, 3, 'SQL is fun!', 80, 0.00, FALSE, '2025-03-21 14:00'),
(104, 1, '광고 테스트', 50, 5.00, TRUE, '2025-03-22 11:00');