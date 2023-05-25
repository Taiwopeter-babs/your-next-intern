-- adds a new column
USE yni_db;
-- ALTER TABLE company_intern
-- MODIFY `date_applied` DATE NOT NULL DEFAULT (CURRENT_DATE());
ALTER TABLE companies
ADD COLUMN `application_open` BOOLEAN DEFAULT 1 AFTER `website`;