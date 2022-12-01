-- Import the database dump from hbtn_0d_tvshows
SELECT DISTINCT `name`
  FROM `tv_genres` As t_g
       INNER JOIN `tv_show_genres` AS t_sg
       ON t_g.`id` = t_sg.`genre_id`

       INNER JOIN `tv_shows` AS t_s
       ON t_sg.`show_id` = t_s.`id`
       WHERE tv_genres.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` As t_g
	             INNER JOIN `tv_show_genres` AS t_g
		     ON t_g.`id` = t_sg.`genre_id`

		     INNER JOIN `tv_shows` AS tv
		     ON t_sg.`show_id` = tv.`id`
		     WHERE tv.`title` = "Dexter")
 ORDER BY t_g.`name`;
