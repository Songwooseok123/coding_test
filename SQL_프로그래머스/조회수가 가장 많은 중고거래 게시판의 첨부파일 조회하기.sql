-- 조회수가 가장 높은 중고 거래 게시물에 대한 경로 
WITH A AS (SELECT BOARD_ID
FROM USED_GOODS_BOARD 
ORDER BY VIEWS DESC
LIMIT 1 )

SELECT CONCAT('/home/grep/src/',BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT)
FROM USED_GOODS_FILE 
WHERE BOARD_ID IN (SELECT BOARD_ID FROM A )
ORDER BY FILE_ID DESC

-- 밑에는 다른 답안 
SELECT CONCAT('/home/grep/src/', A.BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE AS A
    LEFT JOIN USED_GOODS_BOARD B
    ON A.BOARD_ID = B.BOARD_ID
WHERE VIEWS = (
    SELECT MAX(VIEWS)
    FROM USED_GOODS_BOARD
    )
ORDER BY FILE_ID DESC

