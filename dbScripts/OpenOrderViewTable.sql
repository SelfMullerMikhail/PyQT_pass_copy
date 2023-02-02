-- SQLite
CREATE VIEW OpenOrderViewTable AS
SELECT Menu.name as menu_name, Menu.price as menu_prise, count(count) as count, (Menu.price * count(count)) as summ_position, Menu.id as id_menu, OpenOrder.id_table as id_table
FROM  OpenOrder, Menu
WHERE OpenOrder.id_menu = Menu.id
GROUP BY id_menu;