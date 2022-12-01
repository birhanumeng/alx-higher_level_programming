-- Import the database dump from hbtn_0d_tvshows
SELECT DISTINCT `title`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS t_sg
       ON t_sg.`show_id` = tv.`id`

       LEFT JOIN `tv_genres` AS t_g
       ON t_g.`id` = t_sg.`genre_id`
       WHERE tv.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS tv
	             INNER JOIN `tv_show_genres` AS t_sg
		     ON t_sg.`show_id` = tv.`id`

		     INNER JOIN `tv_genres` AS t_g
		     ON t_g.`id` = t_sg.`genre_id`
		     WHERE g.`name` = "Comedy")
 ORDER BY `title`;
