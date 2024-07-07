### DATE_FOMAT(A, '날짜 어떻게 표시할지')
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE

-- select date_format('2022-07-16 19', '%Y%m%d%H');
-- "2022071619"
-- y: 두자리연도
-- H: 24시간

### JOIN
FROM USED_GOODS_REPLY R
    LEFT JOIN USED_GOODS_BOARD B
    ON B.BOARD_ID = R.BOARD_ID

-- USED_GOODS_REPLY를 R로 취급 , USED_GOODS_BOARD를 B로 취급
-- LEFT JOIN : 왼쪽 테이블을 중심으로 오른쪽 테이블을 매치시킨다. 
-- RIGHT JOIN : 오른쪽 테이블을 중심으로 왼쪽 테이블을 매치시킨다. 
-- JOIN : 교집합     

FROM FIRST_HALF
    INNER JOIN
    (
        SELECT FLAVOR
        FROM ICECREAM_INFO
        WHERE INGREDIENT_TYPE = 'fruit_based'
    )  I
    ON FIRST_HALF.FLAVOR = I.FLAVOR
-- 서브 쿼리 날려서 I로 취급 하고 (SELCT~) I 해도 되고, (SELCT~) AS I도 됨. 
-- INNER JOIN : 기준 테이블과 조인 테이블 모두 데이터가 존재해야 조회됨
-- OUTER JOIN : 기준 테이블에만 데이터가 존재하면 조회됨
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
-- 참고로 IS NULL도 있

### WHERE OR 이나 WHERE IN이랑 같음     
WHERE MCDP_CD = 'CS' OR MCDP_CD ='GS' 
WHERE MCDP_CD in ('CS', 'GS')

### WHERE OR WHERE IN 순서 반대로도 됨(요소가 컬럼에 있는지: 밑에 두개 같은 코드임 )
WHERE SKILL_1 ='Python' OR SKILL_3 ='Python' OR SKILL_2 ='Python'
WHERE 'Python' IN (SKILL_1,SKILL_2,SKILL_3)


### 평균 구하기 
SELECT AVG(DAILY_FEE) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';

### 반올림 
SELECT ROUND(AVG(DAILY_FEE), 0) AS AVERAGE_FEE
 -- 소수 첫째자리 반올림 

### "ADDRESS 컬럼에서 강원도로 시작하는 데이터 찾기"
WHERE ADDRESS LIKE "강원도%"

### TLNO 컬럼 값이 없으면,(즉 NULL이면) 'NONE'으로 출력하기
SELECT IFNULL(TLNO,'NONE') AS TLNO

### GROUP BY , HAVING 
-- REST_ID 별로 평균 REVIEW SCORE를 구해야됨
SELECT R.REST_ID,	
       I.REST_NAME,
       I.FOOD_TYPE,
       I.FAVORITES,
       I.ADDRESS,
       ROUND(AVG(R.REVIEW_SCORE),2) AS SCORE
FROM REST_REVIEW AS R  
     JOIN REST_INFO AS I
     ON R.REST_ID = I.REST_ID
GROUP BY R.REST_ID
HAVING ADDRESS LIKE "서울%"

-- R이랑 A랑 REST_ID 대상으로 JOIN을 해서 교집합을 구한다.
-- GROUP BY로 REST_ID 별로 묶임. 그다음에 REST_ID 끼리 평균 계산 
-- 그 중에서 서울 인거 뽑기 

### GROUP BY ,HAVING, COUNT 

SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(PRODUCT_ID) > 1

-- GROUP BY 절: USER_ID와 PRODUCT_ID별로 데이터를 그룹화합니다. 즉, 각 사용자-제품 조합에 대해 한 번씩 그룹을 만듭니다.
-- HAVING 절: 각 그룹에 대해 PRODUCT_ID의 개수를 계산합니다. 이 개수가 1보다 큰 그룹만을 선택합니다. 이는 특정 사용자가 동일한 제품을 두 번 이상 구매한 경우를 의미합니다.

### 없는 컬럼 NULL로 채워서 SELECT 하기
SELECT NULL AS USER_ID

### 없는 컬럼 1로 채워서 SELECT하기(즉, COULMN만들기)
SELECT 1 AS DLFAJLD

### UNION ALL -- 중복 제거 없이 합처서 결과, UNION -- 중복 제거 결과

### DATETIME 상위 한개 
SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME =
      (SELECT MIN(DATETIME)
       FROM ANIMAL_INS    
      )
-- 위에거랑 밑에꺼랑 같은 거임. 
SELECT NAME
FROM animal_ins
ORDER BY DATETIME
LIMIT 1 

### SELECT하고 갯수 세기 
SELECT COUNT(USER_ID)

### JOIN 2번 
FROM A AS A
     JOIN B AS B
     ON A.ID = B.ID
JOIN A AS AA  
ON B.IID = AA.ID 
-- A와 B를 ID로 조인하고 다시 그 테이블(AB)을 A와 조인하는데, A의 ID와 AB의 IID로 조인  

### WHERE SKILL_CODE & 4 의 의미
-- SKILL_CODE가 이진수로 4을 포함하고 있나 
SKILL_CODE가 만약에 6이라면 b'110'이고 4는 b'100'라서 참이됨. 

### 중복 제거 
SELECT DISTINCT NAME 

### CONCAT
SELECT CONCAT(MAX(LENGTH),'cm') AS MAX_LENGTH
FROM FISH_INFO
-- 50.00cm 로 출력하기 


    
SELECT
    -- 대장균들의 자식 수 구하기 부터 다시 풀기 

SUM.MAX.MIN 
    -- 물고기 종류 별 대어 찾기
    -- 연도별 대장균 크기의 편차 구하기

