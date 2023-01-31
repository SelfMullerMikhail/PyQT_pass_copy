-- SQLite
CREATE TABLE SupplyOfProducts(
id INTEGER PRIMARY KEY AUTOINCREMENT,
id_supplyer varchar(50),
price int(50),
count int(50),
date_supply TEXT
);

-- DROP TABLE SupplyOfProducts;

-- INSERT INTO SupplyOfProducts(name_supplyer, count, date_supply)
-- VALUES("Susha", 1000, date('2023-01-02'));

-- SELECT * FROM SupplyOfProducts;