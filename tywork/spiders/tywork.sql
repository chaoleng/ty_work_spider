create table job(
    id INT UNSIGNED AUTO_INCREMENT,
    job_id int(20),
    job_title varchar(30),
    job_salary varchar(93),
    job_desc varchar(100),
    job_position varchar(100),
    UNIQUE (job_id),
    PRIMARY KEY ( `id` )
    );