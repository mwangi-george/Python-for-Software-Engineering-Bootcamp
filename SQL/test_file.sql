-- Creating a database
CREATE DATABASE Learning_FastAPI;

-- Creating a schema
CREATE SCHEMA my_tables_schema;

-- Creating table user_info if it does not exist
CREATE TABLE IF NOT EXISTS user_info (
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(25),
    join_date DATE,
    email TEXT
);

CREATE TABLE IF NOT EXISTS event_info (
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(25)
);

-- Creating table event_log if it does not exist
CREATE TABLE IF NOT EXISTS event_log (
    event_key SERIAL PRIMARY KEY NOT NULL,
    event_id INT NOT NULL,
    time TIMESTAMP,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_info (id),
    FOREIGN KEY (event_id) REFERENCES event_info (id)
);

-- Specifying schema during table creation (Great when dealing with multiple schemas)
CREATE TABLE IF NOT EXISTS public.event_info (
    id INT PRIMARY KEY NOT NULL,
    name TEXT
);

-- Deleting the created table
DROP TABLE public.event_info;

-- Deleting a schema.
-- DROP SCHEMA my_tables_schema; -- This will cause an error if there are tables inside

-- To clean dependencies inside the schema
-- DROP SCHEMA my_tables_schema CASCADE;


-- Altering table structure e.g. add or remove columns
ALTER TABLE user_info ADD COLUMN region VARCHAR(30);

-- ALTER TABLE user_info DROP COLUMN region;

-- Say we realise our userbase is growing and we need to update id column of user_info table to bigint type
ALTER TABLE user_info ALTER COLUMN id TYPE bigint;


-- Enumerated Data types e.g. days of the week.
-- Contain hierarchical ordering between different instances
CREATE TYPE day_of_week AS ENUM (
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
);

-- If we need to change the type
-- ALTER TYPE day_of_week RENAME VALUE 'Sunday' TO 'new_value'

-- We can now use the above enumerated type to create a table
CREATE TABLE student_attendance (
    student_id INT,
    week_day day_of_week,
    key SERIAL PRIMARY KEY -- we don't need to provide a value while inserting values
);

-- Inserting Data into tables
INSERT INTO student_attendance VALUES (1, 'Monday');

-- Changing ordering of columns while inserting values
INSERT INTO student_attendance (week_day, student_id) VALUES ('Tuesday', 1);

-- NB Use double quotation marks when specifying column names



















