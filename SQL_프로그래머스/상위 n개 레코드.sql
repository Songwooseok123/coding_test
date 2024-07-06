-- 코드를 입력하세요
SELECT NAME
FROM animal_ins
WHERE DATETIME =(
    SELECT MIN(DATETIME)
    FROM ANIMAL_INS
)

-- 이것도 정답 
-- 코드를 입력하세요
SELECT NAME
FROM animal_ins
ORDER BY DATETIME
LIMIT 1 
