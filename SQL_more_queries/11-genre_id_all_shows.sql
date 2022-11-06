-- list all shows contained in the database hbtn_0d_tvshows.
--   - Each record should display: tv_shows.title - tv_show_genres.genre_id
--   - Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--   - If a show doesn’t have a genre, display NULL
--   - You can use only one SELECT statement
SELECT s.title, pivot.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres pivot
ON s.id = pivot.show_id
ORDER BY s.title, pivot.genre_id ASC;