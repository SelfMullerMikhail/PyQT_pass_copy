-- SQLite

DROP VIEW MenuView;
CREATE VIEW MenuView AS 
SELECT Menu.Image as image_name, Menu.name as name_menu, Category.name as name_category , price as price_menu, Menu.id as id_menu
FROM Menu, Category 
WHERE Menu.category = Category.id;