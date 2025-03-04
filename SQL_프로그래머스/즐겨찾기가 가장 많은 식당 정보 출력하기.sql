           
SELECT FOOD_TYPE, REST_ID, REST_NAME,FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE,FAVORITES) IN (SELECT FOOD_TYPE,
                                        MAX(FAVORITES) AS FAVORITES
                                FROM REST_INFO 
                                GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC

 --- 처음엔 이렇게 풀었었음. 
-- GROUP BY의 대상이 아닌 REST_ID,REST_NAME을 SELECT하는데 있어서  오류가 발생함. 이상한애 가져옴... 

  SELECT FOOD_TYPE, REST_ID, REST_NAME, MAX(FAVORITES) AS FAVORITES
FROM REST_INFO 
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC;
