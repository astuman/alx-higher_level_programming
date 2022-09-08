-- lists show containd in hbtn_0d_tvshows
SELECT ts.title, g.genre_id FROM tv_shows AS ts LEFT JOIN tv_show_genres AS g ON ts.id = g.show_id WHERE g.genre_id IS NULL ORDER BY ts.title, g.genre_id;
