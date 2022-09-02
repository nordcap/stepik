/*
Задание
Добавьте три последние записи (с ключевыми значениями 6, 7, 8) в таблицу book, первые 5 записей уже добавлены:

book_id	title	author_id	genre_id	price	amount
1	Мастер и Маргарита	1	1	670.99	3
2	Белая гвардия	1	1	540.50	5
3	Идиот	2	1	460.00	10
4	Братья Карамазовы	2	1	799.01	3
5	Игрок	2	1	480.50	10
6	Стихотворения и поэмы	3	2	650.00	15
7	Черный человек	3	2	570.20	6
8	Лирика	4	2	518.99	2
*/

INSERT INTO book(book_id, title, author_id, genre_id, price, amount)
VALUES(6, "Стихотворения и поэмы", 3,2,650.00,15);

INSERT INTO book(book_id, title, author_id, genre_id, price, amount)
VALUES(7, "Черный человек", 3,2,570.20,6);

INSERT INTO book(book_id, title, author_id, genre_id, price, amount)
VALUES(8, "Лирика", 4,2,518.99,2);
