-- settings.sql
CREATE DATABASE codylibrary;
CREATE USER postgres WITH PASSWORD 'codylibrary';
GRANT ALL PRIVILEGES ON DATABASE codylibrary TO postgres;

-- Example
-- CREATE DATABASE books;
-- CREATE USER booksuser WITH PASSWORD 'books';
-- GRANT ALL PRIVILEGES ON DATABASE books TO booksuser;
