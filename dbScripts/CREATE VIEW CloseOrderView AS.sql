DROP VIEW CloseOrderView;
CREATE VIEW CloseOrderView AS
SELECT *, (cash + card) as total, menu_price 
FROM ClosedOrder
GROUP BY id_table;
