-- use the hbtn_0d_tvshows database to lists all genres of the show Dexter.
--  - The tv_shows table contains only one record where title = Dexter (but the id can be different)
--  - Each record should display: tv_genres.name
--  - Results must be sorted in ascending order by the genre name
--  - You can use only one SELECT statement
SELECT g.name FROM tv_genres g
JOIN tv_show_genres pivot ON g.id = pivot.genre_id
JOIN tv_shows s ON s.id = pivot.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;