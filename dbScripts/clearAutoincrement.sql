-- -- SQLite


UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'TechnologyCard';
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'Tables';
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'Menu';
UPDATE SQLITE_SEQUENCE SET seq = 1 WHERE name = 'Category';
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'OpenOrder';
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'Stock';
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'AddProductTransaction';
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'Suppliers';
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'SupplyOfProducts';
UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'ClosedOrder';
SELECT * FROM SQLITE_SEQUENCE ;

DELETE FROM TechnologyCard;
DELETE FROM Tables;
DELETE FROM Menu;
DELETE FROM Category;
INSERT INTO Category(name, image) VALUES('Main', 'book.svg');
DELETE FROM OpenOrder;
DELETE FROM Stock;
DELETE FROM AddProductTransaction;
DELETE FROM Suppliers;
DELETE FROM SupplyOfProducts;
DELETE FROM ClosedOrder;