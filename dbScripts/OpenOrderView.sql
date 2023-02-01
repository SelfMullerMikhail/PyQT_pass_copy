-- SQLite

CREATE VIEW OpenOrderView AS
SELECT Tables.tables_name as table_name, Tables.id as table_id, Menu.name as menu_name, Menu.id as menu_id FROM Menu, Tables, OpenOrder
WHERE OpenOrder.id_table = Tables.id
AND OpenOrder.id_menu = Menu.id;