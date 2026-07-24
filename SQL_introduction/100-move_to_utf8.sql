-- Converts hbtn_0c_0 database and first_table to UTF8
-- Change charset and collation to utf8mb4_unicode_ci

ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
