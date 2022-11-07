-- list all Comedy shows in the database hbtn_0d_tvshows.
--   - The tv_genres table contains only one record where name = Comedy (but the id can be different)
--   - Each record should display: tv_shows.title
--   - Results must be sorted in ascending order by the show title
--   - You can use only one SELECT statement
SELECT s.title FROM tv_shows s
JOIN tv_show_genres pivot ON s.id = pivot.show_id
JOIN tv_genres g ON g.id = pivot.genre_id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;