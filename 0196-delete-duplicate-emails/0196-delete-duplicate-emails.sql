DELETE FROM PERSON
Where id in (select id from(
SELECT id, 
	email, 
    ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) rw  
FROM PERSON ) c where c.rw > 1)