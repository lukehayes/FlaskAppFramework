DROP TABLE if exists data;
DROP TABLE if exists users;

CREATE TABLE data(id integer, name text, number integer);

INSERT INTO data(id, name, number) VALUES(1, "Bob", 321);
INSERT INTO data(id, name, number) VALUES(2, "John", 1002);
INSERT INTO data(id, name, number) VALUES(3, "Armando", 564);

CREATE TABLE users(id integer, username text, email integer, password text);
INSERT INTO users(id, username, email, password) VALUES
    (1, "developer", "developer@app.com", "password"),
    (2, "admin", "admin@app.com", "password"),
    (3, "testuser", "testuser@app.com", "password");

