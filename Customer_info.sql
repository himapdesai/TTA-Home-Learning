USE Customer_info;

CREATE TABLE Customer(
   Customer_id INT NOT NULL AUTO_INCREMENT,
   Customer_name VARCHAR(200) NOT NULL,
   Customer_birthdate VARCHAR(200) NOT NULL,
   Customer_email VARCHAR(100) NOT NULL,
   Customer_phoneno INT NOT NULL,
   Customer_address VARCHAR(100) NOT NULL,
   space VARCHAR(200) NOT NULL,
   PRIMARY KEY (Customer_id),
   UNIQUE (Customer_name)
 );
TRUNCATE TABLE Customer; 
 
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Sarah', '01/01/1981', 'a@a.com', '123456789', 'Address1, Address 2 city', '2');
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Vinit', '02/03/1956', 'fhfd@gmail.com', '434534555', 'add1,add2,city', '2');
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Alisha', '08/03/1967', 'dfds@gmail.com', '343433545', 'Birmingham', '3');
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Hima', '03/02/1956', 'dfd@gmail.com', '534534546', 'Address1', '4');
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Sophiya', '05/04/1956', 'ytyj@gmail.com', '745767668', 'Solihull', '3');
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Lukash', '04/07/1967', 'jjgj@gmail.com', '546456464', 'Sohoroad', '3');
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Mark', '04/03/1967', 'gdfg@gamil.com', '343453453', 'add1,add2', '4');
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Stive', '06/08/1945', 'gffj@gmail.com', '342343424', 'Suttonroad', '2');
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Diya', '03/02/1967', 'gjjk@gmail.com', '234545656', 'add1,city', '4');
INSERT INTO Customer (Customer_name, Customer_birthdate, Customer_email, Customer_phoneno, Customer_address, space)
VALUES
('Sruti', '-3/06/1967', 'dfd@gmail.com', '235656567', 'Coventry', '5');

SELECT * FROM Customer;

TRUNCATE TABLE address;  

CREATE TABLE address (
   Address_id INT AUTO_INCREMENT NOT NULL,
   Address_no INT NOT NULL,
   Address_street VARCHAR(100) NOT NULL,
   Address_city VARCHAR(100) NOT NULL,
   Address_postcode VARCHAR(100) NOT NULL,
   Customer_id INT NOT NULL,
   Address_country VARCHAR(20) NOT NULL,
   PRIMARY KEY (Address_id),
   UNIQUE (Address_no)
   );

SET @CustomerId = -1;

SELECT @CustomerId:= Customer_id from Customer where Customer_name = 'Sarah';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('2', 'Villay', 'Solihull', 'B89 5GU', @CustomerId, "UK");
SELECT @CustomerId:= Customer_id from Customer where Customer_name = 'Vinit';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('3', 'Sandy', 'Soho ', 'B78 5GU', @CustomerId, "Canada");
SELECT  @CustomerId:= Customer_id  from Customer where Customer_name = 'Alisha';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('4', 'Candyhill', 'Coventry', 'C67 5RF', @CustomerId, "Spain");
SELECT @CustomerId:= Customer_id  from Customer where Customer_name = 'Hima';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('5', 'Widney', 'Samerroad', 'S78 5HJ', @CustomerId, "India");
SELECT @CustomerId:= Customer_id  from Customer where Customer_name = 'Sophiya';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('6', 'Halifax', 'Birmingham', 'B67 5JK', @CustomerId, "Itlay");
SELECT @CustomerId:= Customer_id  from Customer where Customer_name = 'Lukash';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('7', 'Dawnton', 'Nottingham', 'N76 8HJ', @CustomerId, "England");
SELECT @CustomerId:= Customer_id  from Customer where Customer_name = 'Mark';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('8', 'Abbey', 'Birmingham', 'B78 5GJ', @CustomerId, "Paris");
SELECT @CustomerId:= Customer_id  from Customer where Customer_name = 'Stive';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('9', 'Berkley', 'London', 'L67 5FH', @CustomerId, "Barma");
SELECT @CustomerId:= Customer_id  from Customer where Customer_name = 'Diya';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('10', 'Broadway', 'London', 'L56 3HJ', @CustomerId, "Chin");
SELECT @CustomerId:= Customer_id  from Customer where Customer_name = 'Sruti';
SELECT @CustomerId;

INSERT INTO address (Address_no, Address_street, Address_city, Address_postcode, Customer_id, Address_country)
VALUES
('11', 'Clarence', 'Nottingham', 'ND6 6DJ', @CustomerId, "India");

SELECT * FROM address;

UPDATE Customer SET Customer_name = 'Hinal'
Where Customer_id = '4';

SELECT * FROM Customer;

ALTER TABLE address
DROP COLUMN Address_country;

SELECT * FROM address;

SELECT * FROM address
WHERE Customer_id = 4;

SELECT Customer_phoneno, Customer_address FROM Customer
ORDER BY Customer_phoneno, Customer_address;

SELECT * FROM Customer WHERE space = 3;

SELECT * FROM Customer INNER JOIN address
WHERE Customer.Customer_id = address.Customer_id AND address.Address_no = 3;