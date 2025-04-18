-- 코드를 입력하세요
SELECT B.USER_ID,B.NICKNAME, SUM(A.PRICE) AS TOTAL_SALES
FROM (SELECT * FROM USED_GOODS_BOARD WHERE STATUS = 'DONE' )AS A 
LEFT JOIN USED_GOODS_USER AS B 
ON A.WRITER_ID = B.USER_ID
GROUP BY A.WRITER_ID
HAVING TOTAL_SALES >= 700000 
ORDER BY TOTAL_SALES 


-- GROUP BY를 하기 전에 WHERE를 쓰면 됨. 
-- 코드를 입력하세요
SELECT B.USER_ID,B.NICKNAME, SUM(A.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS A
LEFT JOIN USED_GOODS_USER AS B 
ON A.WRITER_ID = B.USER_ID

WHERE STATUS = 'DONE'
GROUP BY A.WRITER_ID
HAVING TOTAL_SALES >= 700000 
ORDER BY TOTAL_SALES 
