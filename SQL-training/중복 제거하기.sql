-- 서브 쿼리를 이용 ver. 서브 쿼리는 as로 별칭을 지어줘야한다.
-- 모든 것을 세어라 별칭은 'count' (NAME을 선택하라. ANIMAL_INS 중에. NAME이 NULL이 아닌 것을 골라. NAME기준으로 집합)로부터. 'usb'라는 별칭을 가진.
-- SELECT COUNT(*) as count FROM (SELECT NAME FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME) as sub

-- DISTINCT 사용 ver.
-- 이제서야 안 것이지만, 문법을 소문자로도 사용 가능하다...
-- NAME을 구별하여. 숫자를 세어. 선택하라. ANIMAL_INS로부터.
-- GROUP BY는 집합시키고, DISTINCT는 구별한다는 데에서 언뜻 비슷해보이지만 다르다.
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
