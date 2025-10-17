-- script that creates a trigger that decreases the quantity of an item after adding a new order.
-- column names must be: band_name and lifespan (in years)
DELIMITER $$

CREATE TRIGGER decrease_quantity_items_after_insert_orders
AFTER INSERT 
ON orders
FOR EACH ROW -- trigger will be executed for each insertion
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
