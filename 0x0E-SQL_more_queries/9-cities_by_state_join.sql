-- LISTS ALL CITIES CONTAINE IN 'hbtn_0d_usa'
USE hbtn_0d_usa;
SELECT c.id, c.name, s.name FROM cities AS c INNER JOIN states AS s ON  c.states_id = s.id ORDER BY c.id;
