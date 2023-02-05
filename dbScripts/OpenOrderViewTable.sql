-- SQLite
-- DROP VIEW OpenOrderViewTable;
-- CREATE VIEW OpenOrderViewTable AS
-- SELECT Menu.name as menu_name, 
-- Menu.price as menu_prise, 
-- count(count) as count, 
-- (Menu.price * count(count)) as summ_position, Menu.id as id_menu,
--  OpenOrder.id_table as id_table,
--  OpenOrder.id_client
-- FROM  OpenOrder, Menu
-- WHERE OpenOrder.id_menu = Menu.id AND id_client = 1
-- GROUP BY id_menu;

SELECT *, sum(Menu.price * OpenOrder.count)
FROM  OpenOrder, Menu
WHERE OpenOrder.id_menu = Menu.id 
AND
OpenOrder.id_table = 7
GROUP BY Menu.id;