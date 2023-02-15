-- SQLite
DROP TABLE Client;
CREATE TABLE Client(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(100),
birthday date,
password VARCHAR(100),
number INT(50),
access VARCHAR(100)
);

INSERT INTO Client(name, password, access) 
VALUES('Admin', '39dfa55283318d31afe5a3ff4a0e3253e2045e43', 'Manager');

-- CREATE TABLE Access(
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- name VARCHAR(100)
-- );

-- INSERT INTO Access(name) VALUES('Guest'), ('Barista'), ('Manager');