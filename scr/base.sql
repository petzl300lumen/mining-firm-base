DROP TABLE users;
DROP TABLE orders;
DROP TABLE products;
DROP TABLE employee;
DROP TABLE manufacturers;
DROP TABLE delivery;
DROP TABLE transportation;
DROP TABLE storages;
DROP TABLE projects;
DROP TABLE capital;

CREATE TABLE users(
id_user INT PRIMARY KEY, 
login VARCHAR(100),
password VARCHAR(100),
phone_number VARCHAR (100),
email_adress VARCHAR(100),
verified INT(1)
);

CREATE TABLE orders(
id_order INT PRIMARY KEY,
id_user INT NOT NULL,
id_product INT NOT NULL,
id_employee INT NOT NULL,
date VARCHAR(10),
FOREIGN KEY (id_user) REFERENCES users(id_user)
ON DELETE CASCADE ON UPDATE NO ACTION,
FOREIGN KEY (id_product) REFERENCES products(id_product)
ON DELETE CASCADE ON UPDATE NO ACTION,
FOREIGN KEY (id_employee) REFERENCES employees(id_employee)
ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE products(
id_product INT PRIMARY KEY,
id_manufacturer NOT NULL,
product_name VARCHAR(100),
type_product VARCHAR(100),
quantity INT(100),
unit VARCHAR(100),
price INT(100),
FOREIGN KEY (id_manufacturer) REFERENCES manufacturers(id_manufacturer)
);

CREATE TABLE employee(
id_emloyee INT PRIMARY KEY,
FIO VARCHAR(100),
position VARCHAR(100),
email_adress_emp VARCHAR(100)
);

CREATE TABLE manufacturers(
id_manufacturer INT PRIMARY KEY,
company_name VARCHAR(100),
requisites INT(10),
adress VARCHAR(100),
contacts VARCHAR(100)
);

CREATE TABLE delivery(
id_delivery INT PRIMARY KEY,
date VARCHAR(10),
id_order NOT NULL,
id_transport NOT NULL,
FOREIGN KEY (id_order) REFERENCES orders(id_order),
FOREIGN KEY (id_transport) REFERENCES tranportation(id_transport)
);

CREATE TABLE transportation(
id_transport INT PRIMARY KEY,
type VARCHAR(100),
quantity INT(50),
price_transparency INT(50)
);

CREATE TABLE storages(
id_storage INT PRIMARY KEY,
location VARCHAR(100),
id_product NOT NULL,
FOREIGN KEY (id_product) REFERENCES products(id_product)
);

CREATE TABLE projects(
id_project INT PRIMARY KEY,
project_name VARCHAR(100),
minimg_location VARCHAR(100)
);

CREATE TABLE capital(
id_capital INT PRIMARY KEY,
income INT(50),
expenses INT(50),
id_order NOT NULL,
id_project NOT NULL,
FOREIGN KEY (id_order) REFERENCES orders(id_order),
FOREIGN KEY (id_project) REFERENCES projects(id_project)
);