-- SQLite

DROP TABLE MoneyStory;
CREATE TABLE MoneyStory(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 time_closed time_close datetime DEFAULT CURRENT_DATE, 
 cash_teory int(50),
 card_teory int(50),
 cash_fact int(50), 
 card_fact int(50));
