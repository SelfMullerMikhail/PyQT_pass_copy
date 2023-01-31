Create table Stock (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50),
count INT(50),
price INT(50),
id_Suppiler INT(50),
FOREIGN KEY (id_Suppiler)  REFERENCES Suppliers (id)
);

-- drop table Stock;