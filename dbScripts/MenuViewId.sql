-- SQLite

DROP VIEW MenuViewId;
CREATE VIEW MenuViewId as
SELECT Menu.id as id_menu, Menu.name as name_menu, Menu.category as id_category 
FROM TechnologyCard, Menu
WHERE TechnologyCard.id_menu = Menu.id;