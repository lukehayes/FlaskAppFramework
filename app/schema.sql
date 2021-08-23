DROP TABLE if exists users;

-- Users Table
CREATE TABLE users(id integer PRIMARY KEY, username text, email integer, password text);

INSERT INTO users(id, username, email, password) VALUES
    (1, "developer", "developer@app.com", "pbkdf2:sha256:260000$FfYLQKXio9dkssIi$57a00682fe12f78fe040f2ff7afe23201331328d6be54b30ec5468826a0fafce");
    -- (2, "admin", "admin@app.com", "admin"),
    -- (3, "testuser", "testuser@app.com", "password");

