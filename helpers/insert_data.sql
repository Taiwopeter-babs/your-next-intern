-- creates the database and tables for the backend
USE yni_db;

-- INSERT INTO `companies`(id, name, address, specialization, available_slots, email, website) 
-- VALUES
--     ('75a225e0-ce88-404d-bd1b-e9c9305a84c6', 'Eskrit', '10, allen avenue', 'software and data', 3, 'eskrit@gmail.com', 'wwwe.eskrit.com'),
--     ('b1c079b4-c0a7-400c-bdb3-2df4a1d973fd', 'Sapeir', '13, allen avenue', 'financial analysis', 12, 'sapeir@gmail.com', 'wwwe.sapeir.com');
-- ALTER TABLE `companies` MODIFY `password` VARCHAR(256) NOT NULL;
-- ALTER TABLE `interns` MODIFY `password` VARCHAR(256) NOT NULL;
-- ALTER TABLE `companies` ADD NOT NULL (password);
-- ALTER TABLE `interns` ADD NOT NULL (password);
-- UPDATE `companies`
-- SET password = '710723e52b169429d447717e66cf1491d2e72b27239f33e2fecebb0178e1b702'
-- WHERE `name` = 'Eskrit';

-- UPDATE `companies`
-- SET password = '1567b95f0acf1076235e2465d35bd12c0f704e1adf13d3f2c5997174c309d7f6'

-- WHERE `name` = 'Sapeir'; 

USE yni_db;

-- INSERT INTO `admins`(id, name, email, password, 1) 
-- VALUES
--     ('b1c079b4-c0a7-400c-bdb3-2df4a1d973fd', 'Taiwo Babalola', 'babalolataiwop@gmail.com', '8022ebab28efd4ea4c0d29cc6d1c33380e1910e99d5c0f5e8a177599340bacd6');
UPDATE admins
SET created_at = CURRENT_TIMESTAMP, updated_at = CURRENT_TIMESTAMP WHERE name = 'Taiwo Babalola';