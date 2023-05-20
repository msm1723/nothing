CREATE TABLE data_1 (
   id serial PRIMARY KEY,
   name VARCHAR(255) NOT NULL
);

ALTER SEQUENCE data_1_id_seq RESTART WITH 1 INCREMENT BY 1;

INSERT INTO data_1 (id, name)
VALUES (1, 'Test1'), (2, 'Test2');

CREATE TABLE data_2 (
   id serial PRIMARY KEY,
   name VARCHAR(255) NOT NULL
);

ALTER SEQUENCE data_2_id_seq RESTART WITH 11 INCREMENT BY 1;

INSERT INTO data_2 (id, name)
VALUES (11, 'Test11'), (12, 'Test12');

CREATE TABLE data_3 (
   id serial PRIMARY KEY,
   name VARCHAR(255) NOT NULL
);

ALTER SEQUENCE data_3_id_seq RESTART WITH 21 INCREMENT BY 1;


INSERT INTO data_3 (id, name)
VALUES (21, 'Test21'), (22, 'Test22');