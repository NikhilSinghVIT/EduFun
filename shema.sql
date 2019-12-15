create table school(
	school_id integer primary key autoincrement,
	name text not null,
	city text not null,
	pin integer
);

create table students(
	student_id integer primary key autoincrement,
	name text not null,
	password text,
	email text not null,
	contact integer not null,
    class int,
    school_id integer,
    CONSTRAINT fk_school_id
    FOREIGN KEY (school_id)
    REFERENCES school(school_id)
);

create table chapter(
    chapter_id integer primary key autoincrement,
    school_id int,
    subject_id text,
    chapter name text,
    location text,
    CONSTRAINT fk_school_id_1
    FOREIGN KEY (school_id)
    REFERENCES school(school_id)
);

create table records(
    student_id int,
    chapter_id int,
    marks int,
    CONSTRAINT fk_stud_id
    FOREIGN KEY (student_id)
    REFERENCES students(student_id)
    CONSTRAINT fk_chap_id
    FOREIGN KEY (chapter_id)
    REFERENCES students(chapter_id)
)



