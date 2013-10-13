-- Turns out that this script is probably completely unnecessary
-- Instead, use Python model objects to create these rows

-- Run this script from the "sql" directory like so:
-- sqlite3 -init create_data.sql ../django/studybuddy/studyBuddy.db

-- This is probably best run against a clean database i.e. "rm studyBuddy.db" and then "python manage.py syncdb"

--- auth_user (Django)
INSERT INTO auth_user (id, username, password, first_name, last_name, email, last_login, is_superuser, is_staff, is_active, date_joined)
VALUES (2, 'user1', 'user1', 'John', 'Smith', 'john.smith@gmail.com', '10-12-2013 08:15:16', 0, 0, 1, '10-10-2013');

-- StudyBuddy user
INSERT INTO profilePage_studybuddyuser (user_id, phone, school_name, year) VALUES (2, '3525551212', 'University of Florida', 2);

-- Semester table
INSERT INTO profilePage_semester (semester, startDate, endDate) VALUES ('Spring 2013', '01-01-2013', '05-31-2013');
INSERT INTO profilePage_semester (semester, startDate, endDate) VALUES ('Summer 2013', '06-01-2013', '07-31-2013');
INSERT INTO profilePage_semester (semester, startDate, endDate) VALUES ('Fall 2013', '08-01-2013', '12-31-2013');

-- Schedule table
INSERT INTO profilePage_schedule (scheduleID, mondayStart, mondayEnd, wednesdayStart, wednesdayEnd, fridayStart, fridayEnd)
VALUES (1, '09:35', '10:25', '09:35', '10:25', '09:35', '10:25');
INSERT INTO profilePage_schedule (scheduleID, thursdayStart, thursdayEnd)
VALUES (2, '11:45', '12:35');

-- Course name table
INSERT INTO profilePage_coursename (courseID, courseName) VALUES ('CDA3101', 'Computer Organization');

-- Course section table
INSERT INTO profilePage_coursesection (courseID_id, semester_id, sectionNumber, regularScheduleID_id, discussionScheduleID_id)
VALUES ('CDA3101', 'Fall 2013', 5716, 1, 2);

-- User schedule
INSERT INTO profilePage_userschedule (userID_id, scheduleID_id) VALUES (2, 1);
INSERT INTO profilePage_userschedule (userID_id, scheduleID_id) VALUES (2, 2);
