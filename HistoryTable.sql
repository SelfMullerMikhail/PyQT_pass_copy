-- SQLite
drop table HistoryTable;
Create table HistoryTable (
id INTEGER PRIMARY KEY AUTOINCREMENT,
id_table int(50),
name_table varchar(100),
client_name int(50),
menu_name varchar(100),
count int(50),
cash int(50),
card int(50),
time_open datetime,
time_close datetime,
menu_price
);

