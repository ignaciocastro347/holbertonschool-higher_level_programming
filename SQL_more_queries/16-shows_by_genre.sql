-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
--   - If a show doesn't have a genre, display NULL in the genre column
--   - Each record should display: tv_shows.title - tv_genres.name
--   - Results must be sorted in ascending order by the show title and genre name
--   - You can use only one SELECT statement
SELECT s.title, g.name FROM tv_shows s
LEFT JOIN tv_show_genres pivot ON s.id = pivot.show_id
LEFT JOIN tv_genres g ON g.id = pivot.genre_id
ORDER BY s.title, g.name ASC;