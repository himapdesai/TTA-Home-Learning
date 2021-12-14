
use Student_info;

CREATE TABLE student_details (
    student_id INT AUTO_INCREMENT,
    student_name VARCHAR(20) NOT NULL,
    student_address VARCHAR(20),
    student_phoneno INT(10) NOT NULL,
    student_result VARCHAR(20) NOT NULL,
    PRIMARY KEY (student_id),
    UNIQUE (student_name)
);

alter table student_details
modify student_address varchar(20) not null;

Insert into student_details
(student_name, student_address, student_phoneno, student_result)
values
('Sarah', 'Sharkhill', 078345678, 'pass'),
('Jeni', 'Sendlyhill', 079856342, 'fail'),
('Johan', 'Hallgreen', 764538622, 'pass'),
('Rohan', 'Sparkbrook', 854637289, 'fail'),
('Rajan', 'Victoria', 764578322, 'pass');

select * from student_details;




