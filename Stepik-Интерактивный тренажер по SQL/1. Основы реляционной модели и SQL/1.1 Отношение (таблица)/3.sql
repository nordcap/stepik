/*
Задание
Занесите три последние записи в таблицу book,  первая запись уже добавлена на предыдущем шаге:
*/

INSERT INTO book(title, author, price, amount) VALUES ('Белая гвардия','Булгаков М.А.',540.50, 5);

INSERT INTO book(title, author, price, amount) VALUES ('Идиот','Достоевский Ф.М.',460.00, 10);

INSERT INTO book(title, author, price, amount) VALUES ('Братья Карамазовы','Достоевский Ф.М.',799.01, 2);

SELECT * FROM book;