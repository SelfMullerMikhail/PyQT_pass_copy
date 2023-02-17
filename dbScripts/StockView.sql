-- SQLite
DROP VIEW StockView;
CREATE VIEW StockView AS SELECT
Stock.name as name, Count, Price, (Count*0.001*Price) as 'Total_money', id_Suppiler, Stock.id as id, Suppliers.name as supplier_name
FROM Stock, Suppliers
WHERE Stock.id_Suppiler = Suppliers.id;