-- Grant all privileges to flaskuser
GRANT ALL PRIVILEGES ON flaskdb.* TO 'flaskuser'@'%' IDENTIFIED BY 'flaskpassword';
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
