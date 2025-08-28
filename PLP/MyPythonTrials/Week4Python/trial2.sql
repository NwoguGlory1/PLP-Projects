# Write an SQL query to create a table called student with the following columns:

# name (String, maximum length of 100 characters)
# age (Integer)
# gender (String, maximum length of 10 characters)

# Write an SQL query to create an index named IdxAge from Student table.
CREATE TABLE student (
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

CREATE INDEX IdxAge ON student(age);