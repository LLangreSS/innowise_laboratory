--1.Create tables
    CREATE TABLE IF NOT EXISTS students(
        id integer PRIMARY KEY,
        full_name text,
        birth_year integer
    );

    CREATE TABLE IF NOT EXISTS grades(
        id integer PRIMARY KEY,
        student_id integer,
        subject text,
        grade integer check (grade between 1 and 100),
        foreign key (student_id) references students(id)
    );

--2.Insert data
    INSERT INTO students(full_name, birth_year) VALUES
        ('Alice Johnson', 2005),
        ('Brian Smith', 2004),
        ('Carla Reyes', 2006),
        ('Daniel Kim', 2005),
        ('Eva Thompson', 2003),
        ('Felix Nguyen', 2007),
        ('Grace Patel', 2005),
        ('Henry Lopez', 2004),
        ('Isabella Martinez', 2006);

    INSERT INTO grades(student_id, subject, grade) VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);

--3.Find all grades for a specific student(Alice Johnson)
    SELECT g.grade
    FROM students AS s
    INNER JOIN grades AS g
    ON s.id = g.student_id
    WHERE s.full_name = 'Alice Johnson';

--4.Calculate the average grade per student
    SELECT
        s.full_name,
        ROUND(AVG(g.grade), 2) AS average_grade_per_student
    FROM students AS s
    INNER JOIN grades AS g ON s.id = g.student_id
    GROUP BY s.id;

--5.List all students born after 2004
    SELECT s.full_name, s.birth_year
    FROM students as s
    WHERE s.birth_year > 2004;

--6.Create a query that lists all subjects and their average grades
    SELECT
        g.subject,
        ROUND(AVG(g.grade), 2) AS average_per_subject
    FROM grades AS g
    GROUP BY g.subject
    ORDER BY average_per_subject DESC, g.subject;

--7.Find top 3 students with the highest average grades
    SELECT
        s.full_name,
        ROUND(AVG(g.grade), 2) AS average_per_student
    FROM students AS s
    INNER JOIN grades AS g ON g.student_id = s.id
    GROUP BY s.id, s.full_name
    ORDER BY average_per_student DESC
    LIMIT 3;

--8.Show all students who have scored below 80 in any subject
    SELECT DISTINCT s.full_name
    FROM students AS s
    INNER JOIN grades AS g ON s.id = g.student_id
    where g.grade < 80;