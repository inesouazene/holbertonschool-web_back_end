-- script that creates a trigger that resets the attribute valid_email only when the email has been changed.
-- If the email is updated to a different value, valid_email should be changed.
DELIMITER $$

CREATE TRIGGER reset_valid_email_after_update_users
BEFORE UPDATE
ON users
FOR EACH ROW -- trigger will be executed for each insertion
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
