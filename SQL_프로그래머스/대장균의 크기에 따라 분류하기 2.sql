WITH A AS (SELECT ID,
       PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PER
FROM ECOLI_DATA)

SELECT  E.ID,  
       CASE 
            WHEN PER <=0.25 THEN 'CRITICAL'
            WHEN PER <=0.50 THEN 'HIGH'
            WHEN PER <=0.75 THEN 'MEDIUM'
            
            ELSE 'LOW'
            
       END AS COLONY_NAME
FROM ECOLI_DATA AS E 
     LEFT JOIN A 
     ON E.ID = A.ID
ORDER BY ID 

-- 밑에가 더 간략함 
SELECT  A.ID,  
       CASE 
            WHEN A.PER <=0.25 THEN 'CRITICAL'
            WHEN A.PER <=0.50 THEN 'HIGH'
            WHEN A.PER <=0.75 THEN 'MEDIUM'
            
            ELSE 'LOW'
            
       END AS COLONY_NAME
FROM (SELECT ID,
             PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PER
      FROM ECOLI_DATA) AS A 
ORDER BY A.ID 
     
     
     
     
