SET @h := -1; -- 변수 선언 h = -1;

-- FROM으로 칼럼들을 가져오고
-- @h+1먼저 실행 시키고 HOUR로 별칭선언
-- HOUR(DATETIME)이 @h와 같은 COUNT(HOUR(DATETIME))만을 뽑아내 COUNT 별칭 선언
-- @h < 23 을 만족시키면
-- GROUP화, ORDER
SELECT (@h := @h + 1) as HOUR, (SELECT COUNT(HOUR(DATETIME)) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @h) as COUNT
FROM ANIMAL_OUTS
WHERE @h < 23
GROUP BY @h
ORDER BY @h
