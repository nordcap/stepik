/*
Задание
Есть список городов, хранящийся в таблице city:

city_id	name_city
1	Москва
2	Санкт-Петербург
3	Владивосток
Необходимо в каждом городе провести выставку книг каждого автора в течение 2020 года. Дату проведения выставки выбрать случайным образом. Создать запрос, который выведет город, автора и дату проведения выставки. Последний столбец назвать Дата. Информацию вывести, отсортировав сначала в алфавитном порядке по названиям городов, а потом по убыванию дат проведения выставок.

Результат
Примечание: даты при каждом запуске получаются разными, и не должны совпадать с приведенными значениями.

+-----------------+------------------+------------+
| name_city       | name_author      | Дата       |
+-----------------+------------------+------------+
| Владивосток     | Достоевский Ф.М. | 2020-12-04 |
| Владивосток     | Лермонтов М.Ю.   | 2020-10-21 |
| Владивосток     | Пастернак Б.Л.   | 2020-08-23 |
| Владивосток     | Есенин С.А.      | 2020-08-14 |
| Владивосток     | Булгаков М.А.    | 2020-01-08 |
| Москва          | Лермонтов М.Ю.   | 2020-09-30 |
| Москва          | Достоевский Ф.М. | 2020-07-21 |
| Москва          | Есенин С.А.      | 2020-06-23 |
| Москва          | Булгаков М.А.    | 2020-05-28 |
| Москва          | Пастернак Б.Л.   | 2020-04-08 |
| Санкт-Петербург | Булгаков М.А.    | 2020-11-05 |
| Санкт-Петербург | Лермонтов М.Ю.   | 2020-10-22 |
| Санкт-Петербург | Достоевский Ф.М. | 2020-09-19 |
| Санкт-Петербург | Есенин С.А.      | 2020-08-11 |
| Санкт-Петербург | Пастернак Б.Л.   | 2020-06-28 |
+-----------------+------------------+------------+

Таблица genre:
+----------+-------------+
| genre_id | name_genre  |
+----------+-------------+
| 1        | Роман       |
| 2        | Поэзия      |
| 3        | Приключения |
+----------+-------------+

Таблица author:
+-----------+------------------+
| author_id | name_author      |
+-----------+------------------+
| 1         | Булгаков М.А.    |
| 2         | Достоевский Ф.М. |
| 3         | Есенин С.А.      |
| 4         | Пастернак Б.Л.   |
| 5         | Лермонтов М.Ю.   |
+-----------+------------------+

Таблица city:
+---------+-----------------+
| city_id | name_city       |
+---------+-----------------+
| 1       | Москва          |
| 2       | Санкт-Петербург |
| 3       | Владивосток     |
+---------+-----------------+

*/

SELECT  name_city,
        name_author,
        DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND()*365) DAY) AS Дата
FROM
    city, author
ORDER BY
    name_city ASC, Дата DESC