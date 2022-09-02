/*
Задание
Заполнить таблицу author. В нее включить следующих авторов:

Булгаков М.А.
Достоевский Ф.М.
Есенин С.А.
Пастернак Б.Л.
Результат
Affected rows: 1
Affected rows: 1
Affected rows: 1
Affected rows: 1

Query result:
+-----------+------------------+
| author_id | name_author      |
+-----------+------------------+
| 1         | Булгаков М.А.    |
| 2         | Достоевский Ф.М. |
| 3         | Есенин С.А.      |
| 4         | Пастернак Б.Л.   |
+-----------+------------------+
*/

INSERT INTO author (name_author) VALUES("Булгаков М.А.");
INSERT INTO author (name_author) VALUES("Достоевский Ф.М.");
INSERT INTO author (name_author) VALUES("Есенин С.А.");
INSERT INTO author (name_author) VALUES("Пастернак Б.Л.");

SELECT * FROM author;