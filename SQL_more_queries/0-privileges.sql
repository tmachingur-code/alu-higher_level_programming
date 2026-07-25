-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost
-- Handles the cases where either or both users may not exist
DELIMITER $$

CREATE PROCEDURE show_privileges_0d()
BEGIN
    DECLARE user1_exists INT;
    DECLARE user2_exists INT;

    SELECT COUNT(*) INTO user1_exists
        FROM mysql.user
        WHERE User = 'user_0d_1' AND Host = 'localhost';

    SELECT COUNT(*) INTO user2_exists
        FROM mysql.user
        WHERE User = 'user_0d_2' AND Host = 'localhost';

    IF user1_exists = 0 AND user2_exists = 0 THEN
        SELECT "Users don't exist";
    ELSEIF user1_exists = 1 AND user2_exists = 0 THEN
        SHOW GRANTS FOR 'user_0d_1'@'localhost';
    ELSEIF user1_exists = 0 AND user2_exists = 1 THEN
        SHOW GRANTS FOR 'user_0d_2'@'localhost';
    ELSE
        SHOW GRANTS FOR 'user_0d_1'@'localhost';
        SHOW GRANTS FOR 'user_0d_2'@'localhost';
    END IF;
END$$

DELIMITER ;

CALL show_privileges_0d();

DROP PROCEDURE show_privileges_0d;
