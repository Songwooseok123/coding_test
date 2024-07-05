### DATE_FOMAT(A, '날짜 어떻게 표시할지')
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE

-- select date_format('2022-07-16 19', '%Y%m%d%H');
-- "2022071619"
-- y: 두자리연도

### JOIN
FROM USED_GOODS_REPLY R
    LEFT JOIN USED_GOODS_BOARD B
    ON B.BOARD_ID = R.BOARD_ID

-- USED_GOODS_REPLY를 R로 취급 , USED_GOODS_BOARD를 B로 취급
-- R+B 순서로 JOIN 하는 거임.  
-- ON 뭐를 기준으로 JOIN할건지 

### 오름차순 -- 이중 오름 차순 
ORDER BY R.CREATED_DATE, B.TITLE;

### 내림차순  
ORDER BY CREATED_DATE DESC
### A는 내림, B는 오름
ORDER BY A DESC, B

### WHERE 조건문 
WHERE MONTH(DATE_OF_BIRTH) = 03 AND GENDER = 'W' AND TLNO IS NOT NULL

-- AND로 계속 이어쓸 수 있음
-- IS NOT NULL 문법 

### WHERE OR 이나 WHERE IN이랑 같음     
WHERE MCDP_CD = 'CS' OR MCDP_CD ='GS' 
WHERE MCDP_CD in ('CS', 'GS')
