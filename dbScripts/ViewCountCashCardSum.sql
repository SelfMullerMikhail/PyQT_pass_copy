-- SQLite
CREATE VIEW ViewCountCashCardTotalSum AS
SELECT * 
FROM CloseOrderView
GROUP BY id_table;