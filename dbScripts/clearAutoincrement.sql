-- -- SQLite

-- DROP VIEW EditTechnolgyCard;
-- CREATE VIEW EditTechnolgyCard as
-- SELECT Stock.name, TechnologyCard.count, TechnologyCard.id_menu
-- FROM Stock, TechnologyCard
-- WHERE Stock.id = TechnologyCard.id_product;

-- SELECT * FROM EditTechnolgyCard;

-- DELETE FROM TechnologyCard WHERE id = 2;
-- DELETE FROM AddProductTransaction WHERE id =7;



SELECT * FROM SQLITE_SEQUENCE ;
-- UPDATE Stock SET id = 0 WHERE id = 4;
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'Suppliers';
-- DELETE FROM Suppliers;