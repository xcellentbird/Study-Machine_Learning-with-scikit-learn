-- JOIN을 안 쓴 경우
-- SELECT ANIMAL_ID, NAME FROM ANIMAL_OUTS WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_INS)

-- ANIMAL_OUTS을 왼쪽에 가져오되, ANIMAL_INS를 ID 맞는 것끼리 매칭하고 JOIN한 상태로 가져온다
-- 그렇게 JOIN된 테이블에서 ID가 없는 열만 골라 SELECT한다.
SELECT OUTS.ANIMAL_ID, OUTS.NAME 
FROM ANIMAL_OUTS OUTS
LEFT JOIN ANIMAL_INS INS ON OUTS.ANIMAL_ID = INS.ANIMAL_ID 
WHERE INS.ANIMAL_ID IS NULL 
ORDER BY OUTS.ANIMAL_ID

-- INNER JOIN은 교집합만을 가져온다
-- SELECT * FROM ANIMAL_OUTS OUTS INNER JOIN ANIMAL_INS INS ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
