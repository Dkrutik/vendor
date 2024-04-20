1)first  git clone <repository_url>
2)all packege are install pip install -r requirements.txt
3) database setup
CREATE DATABASE users;
USE users;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255),
    role VARCHAR(255)
);
4) run application python app.py 
