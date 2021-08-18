DROP TABLE if exists users;

-- Users Table
CREATE TABLE users(id integer, username text, email integer, password text);

INSERT INTO users(id, username, email, password) VALUES
    (1, "developer", "developer@app.com", "developer"),
    (2, "admin", "admin@app.com", "admin"),
    (3, "testuser", "testuser@app.com", "password");

