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
