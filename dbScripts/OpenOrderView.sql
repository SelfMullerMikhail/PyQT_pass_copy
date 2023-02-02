-- SQLite
DROP VIEW OpenOrderView;
CREATE VIEW OpenOrderView AS
SELECT Tables.tables_name, Tables.id as table_id, Menu.name as menu_name, OpenOrder.id_menu
FROM Tables, Menu, OpenOrder
WHERE Tables.id = OpenOrder.id_table
AND
Menu.id = OpenOrder.id_menu; 