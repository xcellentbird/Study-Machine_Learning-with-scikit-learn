SELECT ANIMAL_TYPE, IF(NAME IS NULL,'No name',NAME), SEX_UPON_INTAKE FROM ANIMAL_INS

-- 아래 코드도 가능
-- SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE FROM ANIMAL_INS
