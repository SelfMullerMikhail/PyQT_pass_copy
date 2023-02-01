
CREATE VIEW MenuView AS 
SELECT Menu.Image as image, Menu.name as name, Category.name as category, 0 as cost , price as price, 0 as markup, Menu.id 
FROM Menu, Category 
WHERE Menu.category = Category.id;