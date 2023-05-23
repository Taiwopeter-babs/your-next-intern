-- creates the database and tables for the backend
CREATE DATABASE IF NOT EXISTS yni_db;
USE yni_db;

CREATE TABLE IF NOT EXISTS schools (
    `id` VARCHAR(50) NOT NULL PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS yni_db.interns (
  `id` VARCHAR(50) NOT NULL PRIMARY KEY,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `birthday` DATE NOT NULL,
  `institution` VARCHAR(128) NOT NULL,
  `course_of_study` VARCHAR(128) NOT NULL,
  `email` VARCHAR(128) NOT NULL UNIQUE,
  `address` VARCHAR(256) NOT NULL,
  `phone_number` VARCHAR(15) NOT NULL,
  `preferred_organization` VARCHAR(256),
  `school_id` VARCHAR(256),
  FOREIGN KEY (school_id) REFERENCES schools(id)
);

CREATE TABLE IF NOT EXISTS companies (
    id VARCHAR(50) NOT NULL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `name` VARCHAR(256) NOT NULL UNIQUE,
    `address` VARCHAR(256) NOT NULL,
    specialization VARCHAR(256) NOT NULL,
    available_slots INTEGER NOT NULL DEFAULT 0,
    email VARCHAR(128) NOT NULL UNIQUE,
    website VARCHAR(256) NOT NULL UNIQUE
);



CREATE TABLE IF NOT EXISTS company_intern (
    intern_id VARCHAR(50) NOT NULL PRIMARY KEY,
    company_id VARCHAR(50) NOT NULL PRIMARY KEY,
    `date_applied` DATE NOT NULL DEFAULT (CURRENT_DATE());
    CONSTRAINT intern_id_fk
        FOREIGN KEY (intern_id) REFERENCES interns(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT company_id_fk
        FOREIGN KEY (company_id) REFERENCES companies(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

