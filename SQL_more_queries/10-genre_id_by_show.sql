-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
--   - Each record should display: tv_shows.title - tv_show_genres.genre_id
--   - Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--   - You can use only one SELECT statement
USE hbtn_0d_tvshows;
SELECT s.title, g.id AS genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id;
