-- creates the database and tables for the backend
CREATE DATABASE IF NOT EXISTS yni_db;
USE yni_db;

CREATE TABLE IF NOT EXISTS schools (
    `id` VARCHAR(60) NOT NULL PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS interns (
  `id` VARCHAR(60) NOT NULL PRIMARY KEY,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `email` VARCHAR(128) NOT NULL UNIQUE,
  `password` VARCHAR(256) NOT NULL,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `gender` VARCHAR(10),
  `birthday` DATE NOT NULL,
  `school` VARCHAR(128) NOT NULL,
  `course` VARCHAR(128) NOT NULL,
  `image_path` VARCHAR(128),
  `address` VARCHAR(256) NOT NULL,
  `phone` VARCHAR(15) NOT NULL UNIQUE,
  `preferred_organization` VARCHAR(256),
  is_administrator TINYINT DEFAULT 0,
  `school_id` VARCHAR(256),
  FOREIGN KEY (school_id) REFERENCES schools(id)
  
);

CREATE TABLE IF NOT EXISTS companies (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    email VARCHAR(128) NOT NULL UNIQUE,
    `password` VARCHAR(256) NOT NULL,
    `name` VARCHAR(256) NOT NULL UNIQUE,
    `address` VARCHAR(256) NOT NULL,
    specialization VARCHAR(256) NOT NULL,
    available_slots INTEGER NOT NULL DEFAULT 0,
    website VARCHAR(256) NOT NULL UNIQUE,
    is_administrator TINYINT DEFAULT 0
   
);
-- create indices
CREATE INDEX ix_interns_email ON interns(email);
CREATE INDEX ix_companies_email ON companies(email);

CREATE TABLE IF NOT EXISTS company_intern (
    intern_id VARCHAR(60) NOT NULL,
    company_id VARCHAR(60) NOT NULL,
    `date_applied` DATE NOT NULL DEFAULT (CURRENT_DATE()),
    CONSTRAINT intern_id_fk
        FOREIGN KEY (intern_id) REFERENCES interns(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT company_id_fk
        FOREIGN KEY (company_id) REFERENCES companies(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

