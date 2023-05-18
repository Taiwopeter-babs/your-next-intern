-- adds a new column
USE yni_db;
-- ALTER TABLE company_intern
-- MODIFY `date_applied` DATE NOT NULL DEFAULT (CURRENT_DATE());
ALTER TABLE interns
ADD COLUMN `gender` VARCHAR(10) NOT NULL AFTER `last_name`;