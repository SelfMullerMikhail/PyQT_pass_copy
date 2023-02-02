-- DROP VIEW MenuView;
-- DROP VIEW ViewCountCashCardTotalSum;
-- CREATE VIEW MenuView AS 
-- SELECT Menu.Image as name, Menu.name as name_menu, Category.name as name_category , price as price_menu, Menu.id as id_menu
-- FROM Menu, Category 
-- WHERE Menu.category = Category.id;

-- DROP VIEW ViewCountCashCardTotalSum;
-- CREATE VIEW ViewCountCashCardTotalSum AS
-- SELECT Menu.image as menu_image,
--         Menu.name as menu_name,
--         Menu.id as menu_id,
--         Menu.price as menu_price,
--         Category.name as category_name,
--         Category.id as category_id,
--         sum(Stock.price * 0.001 * TechnologyCard.count) as cost_menu,
--         (Stock.price *0.001 * Stock.count) as stocks_money
-- FROM Stock, TechnologyCard, Menu, Category
-- WHERE TechnologyCard.id_menu = Menu.id
-- AND
-- Menu.category = Category.id
-- AND Stock.id = TechnologyCard.id_product
-- GROUP BY TechnologyCard.id_menu;

CREATE VIEW ViewCountCashCardTotalSumCost AS
SELECT *,
(ViewCountCashCardTotalSum.cost_menu / ViewCountCashCardTotalSum.menu_price *100) as cost_procent
FROM ViewCountCashCardTotalSum;


-- SELECT *, ViewCountCashCardTotalSum.name:1 FROM ViewCountCashCardTotalSum;
-- WHERE MenuView.id_menu = ViewCountCashCardTotalSum.;

-- SELECT * FROM

-- SELECT * FROM ViewCountCashCardTotalSum;

