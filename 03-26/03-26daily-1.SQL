-- 3
SELECT 
    COUNT(*) AS total_posts,
    SUM(view_count) AS total_views,
    SUM(ad_revenue) AS total_ad_revenue
FROM posts;

-- 4
SELECT 
    ROUND(AVG(ad_revenue), 2) AS avg_ad_revenue
FROM posts
WHERE ad_revenue > 0;

-- 5
SELECT 
    user_id, 
    SUM(ad_revenue) AS total_ad_revenue
FROM posts
GROUP BY user_id;

-- 6
SELECT 
    id, 
    ad_revenue
FROM posts
WHERE ad_revenue = (SELECT MAX(ad_revenue) FROM posts);

-- 7
SELECT 
    id, 
    view_count, 
    ad_revenue, 
    ROUND(ad_revenue / view_count, 4) AS revenue_per_view
FROM posts
WHERE ad_revenue > 0
ORDER BY revenue_per_view DESC
LIMIT 1;

-- 8
SELECT 
    ROUND(AVG(view_count), 2) AS avg_views,
    ROUND(AVG(ad_revenue), 2) AS avg_ad_revenue
FROM posts
WHERE is_public = TRUE;