CREATE TABLE `book` (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(512) NOT NULL,
    `author` VARCHAR(100),
    `read` BOOLEAN NOT NULL DEFAULT 0,
    `created` DATETIME DEFAULT CURRENT_TIMESTAMP(),
    `updated` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP()
);

INSERT INTO `book` (`title`, `author`, `read`)
VALUES ('Harry Potter - Half Blood Prince', 'JK Rowling', FALSE);
