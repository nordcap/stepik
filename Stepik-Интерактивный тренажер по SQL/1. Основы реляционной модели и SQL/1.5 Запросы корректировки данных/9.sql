/*
Задание
Создать таблицу заказ (ordering), куда включить авторов и названия тех книг, количество экземпляров которых в таблице book меньше среднего количества экземпляров книг в таблице book. В таблицу включить столбец   amount, в котором для всех книг указать одинаковое значение - среднее количество экземпляров книг в таблице book.

Результат
Affected rows: 3
Query result:
+------------------+--------------------+--------+
| author           | title              | amount |
+------------------+--------------------+--------+
| Булгаков М.А.    | Мастер и Маргарита | 7      |
| Булгаков М.А.    | Белая гвардия      | 7      |
| Достоевский Ф.М. | Братья Карамазовы  | 7      |
+------------------+--------------------+--------+
Структура и наполнение таблицы book
+---------+-----------------------+------------------+--------+--------+
| book_id | title                 | author           | price  | amount |
+---------+-----------------------+------------------+--------+--------+
| 1       | Мастер и Маргарита    | Булгаков М.А.    | 670.99 | 3      |
| 2       | Белая гвардия         | Булгаков М.А.    | 540.50 | 5      |
| 3       | Идиот                 | Достоевский Ф.М. | 460.00 | 10     |
| 4       | Братья Карамазовы     | Достоевский Ф.М. | 799.01 | 2      |
| 5       | Стихотворения и поэмы | Есенин С.А.      | 650.00 | 15     |
+---------+-----------------------+------------------+--------+--------+
*/

CREATE TABLE ordering AS
SELECT author, title, (SELECT ROUND(AVG(amount)) FROM book) AS amount
FROM book
WHERE amount < (SELECT ROUND(AVG(amount)) FROM book);

SELECT * FROM ordering;

