-- Import the database hbtn_0d_tvshows_rate dump
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS tv
       INNER JOIN `tv_show_ratings` AS tv_r
       ON tv.`id` = tv.r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;

