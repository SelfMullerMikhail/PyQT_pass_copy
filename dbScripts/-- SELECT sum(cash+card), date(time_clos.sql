-- SELECT sum(cash+card), date(time_close) FROM ClosedOrder GROUP BY date(time_close);
SELECT sum(cash), sum(card), date(time_close) 
FROM ClosedOrder WHERE time_close 
BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime')
GROUP BY strftime("%YYYY-%mm-%dd", time_close);