DROP TABLE Books Cascade constraints;
DROP TABLE Book_Copies Cascade constraints;

CREATE TABLE Books (
    ISBN VARCHAR(14) PRIMARY KEY,
    Title VARCHAR(255),
    Edition VARCHAR(50),
    Category VARCHAR(50),
    Price DECIMAL(10, 2)
);

CREATE TABLE Book_Copies (
    ISBN VARCHAR(14),
    Copy# INT,
    Status VARCHAR(20),
    PRIMARY KEY (ISBN, Copy#),
    FOREIGN KEY (ISBN) REFERENCES Books(ISBN)
);

INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0131101630', 'The C Programming Language', '2nd', 'Programming', 45.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0321751041', 'Effective Java', '3rd', 'Programming', 49.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0134093413', 'Clean Code', '1st', 'Programming', 39.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0135957059', 'Python Crash Course', '2nd', 'Programming', 38.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0201616224', 'Design Patterns', '1st', 'Software Engineering', 58.00);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0201835953', 'Code Complete', '2nd', 'Software Engineering', 59.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0132350884', 'The Pragmatic Programmer', '20th Anniversary', 'Software Engineering', 42.50);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0596009205', 'Head First Java', '2nd', 'Programming', 34.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0131103627', 'Introduction to Algorithms', '3rd', 'Algorithms', 89.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0262033848', 'Artificial Intelligence: A Modern Approach', '3rd', 'Artificial Intelligence', 109.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0199535569', 'The Art of Computer Programming', '4th', 'Algorithms', 199.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0262033849', 'Artificial Intelligence: A Modern Approach', '3rd', 'AI', 109.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0132875527', 'Operating System Concepts', '9th', 'Systems', 79.00);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0321154955', 'Refactoring', '2nd', 'Software Engineering', 55.00);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0134190440', 'Data Science for Business', '1st', 'Data Science', 44.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0133157456', 'Python for Data Analysis', '1st', 'Data Science', 42.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0134285190', 'Machine Learning Yearning', '1st', 'Machine Learning', 12.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-1491950357', 'Learning SQL', '2nd', 'Database', 40.00);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-0596517748', 'HTML and CSS: Design and Build Websites', '1st', 'Web Development', 32.99);
INSERT INTO Books (ISBN, Title, Edition, Category, Price) VALUES
('978-1491948971', 'JavaScript: The Good Parts', '1st', 'Web Development', 23.99);

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131101630', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131101630', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131101630', 3, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131101630', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131101630', 5, 'Checked out');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321751041', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321751041', 2, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321751041', 3, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321751041', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321751041', 5, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321751041', 6, 'Available');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134093413', 1, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134093413', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134093413', 3, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134093413', 4, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134093413', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134093413', 6, 'Damaged');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0135957059', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0135957059', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0135957059', 3, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0135957059', 4, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0135957059', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0135957059', 6, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0135957059', 7, 'Damaged');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201616224', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201616224', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201616224', 3, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201616224', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201616224', 5, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201616224', 6, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201616224', 7, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201616224', 8, 'Damaged');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201835953', 1, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201835953', 2, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201835953', 3, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201835953', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201835953', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201835953', 6, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0201835953', 7, 'Damaged');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132350884', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132350884', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132350884', 3, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132350884', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132350884', 5, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132350884', 6, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132350884', 7, 'Damaged');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596009205', 1, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596009205', 2, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596009205', 3, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596009205', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596009205', 5, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596009205', 6, 'Available');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131103627', 1, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131103627', 2, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131103627', 3, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131103627', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131103627', 5, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131103627', 6, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0131103627', 7, 'Available');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033848', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033848', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033848', 3, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033848', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033848', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033848', 6, 'Damaged');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0199535569', 1, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0199535569', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0199535569', 3, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0199535569', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0199535569', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0199535569', 6, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0199535569', 7, 'Damaged');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033849', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033849', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033849', 3, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033849', 4, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033849', 5, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0262033849', 6, 'Available');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132875527', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132875527', 2, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132875527', 3, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132875527', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132875527', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0132875527', 6, 'Available');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321154955', 1, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321154955', 2, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321154955', 3, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321154955', 4, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321154955', 5, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0321154955', 6, 'Checked out');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134190440', 1, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134190440', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134190440', 3, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134190440', 4, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134190440', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134190440', 6, 'Checked out');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0133157456', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0133157456', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0133157456', 3, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0133157456', 4, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0133157456', 5, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0133157456', 6, 'Checked out');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134285190', 1, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134285190', 2, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134285190', 3, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134285190', 4, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134285190', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0134285190', 6, 'Available');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491950357', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491950357', 2, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491950357', 3, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491950357', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491950357', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491950357', 6, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491950357', 7, 'Damaged');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596517748', 1, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596517748', 2, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596517748', 3, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596517748', 4, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596517748', 5, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596517748', 6, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-0596517748', 7, 'Available');

INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491948971', 1, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491948971', 2, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491948971', 3, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491948971', 4, 'Damaged');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491948971', 5, 'Available');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491948971', 6, 'Checked out');
INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES
('978-1491948971', 7, 'Available');
