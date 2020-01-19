CREATE USER pdf_parser_user WITH password 'pdf_parser_password';
CREATE DATABASE pdf_parser_db;
GRANT ALL PRIVILEGES ON DATABASE pdf_parser_db TO pdf_parser_user;