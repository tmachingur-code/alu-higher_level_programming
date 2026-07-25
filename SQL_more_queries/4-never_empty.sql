-- Creates id_not_null table with a default value for id

-- Create id_not_null table if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
