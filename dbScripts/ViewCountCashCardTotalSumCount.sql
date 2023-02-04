SELECT (cost_ingridient)/price * 100 as cost_procent,
sum(cost_ingridient) as cost_product
FROM TechnologyCardView
WHERE id_menu = 7;