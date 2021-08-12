DROP TABLE if exists data;
DROP TABLE if exists users;

-- Data Table
CREATE TABLE data(id integer, name text, number integer);

INSERT INTO data(id, name, number) VALUES
    (1, "Bob", 321),
    (2, "John", 1002),
    (3, "Armando", 564);


-- Users Table
CREATE TABLE users(id integer, username text, email integer, password text);

INSERT INTO users(id, username, email, password) VALUES
    (1, "developer", "developer@app.com", "developer"),
    (2, "admin", "admin@app.com", "admin"),
    (3, "testuser", "testuser@app.com", "password");

