-- 사용자 목록 출력
SELECT username, join_date 
FROM User 
ORDER BY join_date;

-- 플레이 기록 출력
SELECT u.username, g.title as game_title, p.play_time_minutes
FROM User u
JOIN PlayLog p ON u.user_id = p.user_id
JOIN Game g ON p.game_id = g.game_id
ORDER BY u.username, g.title;

-- 평점 5점 리뷰 목록
SELECT u.username, g.title as game_title, r.rating
FROM Review r
JOIN User u ON r.user_id = u.user_id
JOIN Game g ON r.game_id = g.game_id
WHERE r.rating = 5;

-- 장르별 게임 수
SELECT genre, COUNT(*) as game_count
FROM Game
GROUP BY genre
ORDER BY game_count DESC;

-- 사용자별 친구 수
SELECT u.username, COUNT(*) as friend_count
FROM User u
JOIN (
    SELECT user_id1 as user_id FROM Friendship
    UNION ALL
    SELECT user_id2 FROM Friendship
) f ON u.user_id = f.user_id
GROUP BY u.user_id, u.username
ORDER BY friend_count DESC;