/*
Для каждого автора из таблицы author вывести количество книг, написанных им в каждом жанре.

Вывод: ФИО автора, жанр, количество. Отсортировать по фамилии, затем - по убыванию количества написанных книг.
*/

SELECT name_author, name_genre, SUM(amount) AS Количество
FROM author
    INNER JOIN book ON author.author_id=book.author_id
    INNER JOIN genre ON genre.genre_id=book.genre_id
GROUP BY name_author, name_genre
ORDER BY name_author, Количество DESC