CREATE TABLE student (
STU_NUM varchar(6) NOT NULL,  
STU_SNAME varchar(15),  
STU_FNAME varchar(15),  
STU_INITIAL varchar(1),  
STU_STARTDATE date,  
COURSE_CODE varchar(3),  
PROJ_NUM int(2), 
PRIMARY KEY (STU_NUM)
);

.mode column
.headers ON

INSERT INTO student
    VALUES  (01, 'Snow', 'Jon', 'E', '2014-04-05', '201', 6),
            (02, 'Stark', 'Arya', 'C', '2017-07-12', '305', 11),
            (03, 'Lannister', 'Jamie', 'C', '2012-09-05', '101', 2),
            (04, 'Lannister', 'Cersei', 'J', '2012-09-05', '101', 2),
            (05, 'Greyjoy', 'Theon', 'R', '2015-12-09', '402', 14),
            (06, 'Tyrell', 'Margaery', 'Y', '2017-07-12', '305', 10),
            (07, 'Baratheon', 'Tommen', 'R', '2019-06-13', '201', 5);

SELECT * FROM student
WHERE COURSE_CODE='305';

UPDATE student
SET COURSE_CODE='304'
WHERE STU_NUM=07;

DELETE FROM student
WHERE
    STU_SNAME='Lannister'
    AND STU_FNAME='Jamie'
    AND STU_STARTDATE='2012-09-05'
    AND COURSE_CODE='101'
    AND PROJ_NUM=2;

UPDATE student
SET PROJ_NUM=14
WHERE STU_STARTDATE<'2016-01-01' AND COURSE_CODE>='201';

DROP TABLE student;
