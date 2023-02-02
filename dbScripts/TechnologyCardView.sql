-- SQLite
-- DROP VIEW TechnologyCardView;
-- CREATE VIEW TechnologyCardView AS
-- SELECT Stock.name as name_product, Suppliers.name as supplier, TechnologyCard.count, Stock.price, (Stock.price*0.001*TechnologyCard.count) as cost_ingridient, TechnologyCard.id_menu as id_menu
-- FROM TechnologyCard, Stock, Suppliers
-- WHERE TechnologyCard.id_product = Stock.id
-- AND Suppliers.id = Stock.id_Suppiler;

SELECT * FROM Suppliers;
SELECT * FROM TechnologyCard;
SELECT * FROM Stock;
INSERT INTO Stock