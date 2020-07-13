-- lists all records of the table of the database ordered by score >=10 (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
