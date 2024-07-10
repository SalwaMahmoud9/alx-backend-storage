  
-- Task : 5 vaild email
DELIMITER |
CREATE TRIGGER email_bool BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
    END IF;
END;
|