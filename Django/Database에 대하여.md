Django 서버를 배우면서 일단 ORM이 뭘까 궁금했다. 덩달아 나오는 키워드들 DB, SQL Mapper, JPA, DBMS, Hibernate, PostgreSQL, MySQL, MyBatis에 대해서도 공부할 필요가 있어보인다. 그리고 Spring은 어떤 방식으로 DB를 다루는 걸까? C나 Java가 아닌 SQL 쿼리문으로 DB를 관리하는 이유는 뭘까?   
우선 기본기의 기본기로 돌아가 볼 필요가 있을 것 같다.

먼저 DB란 무엇일까? DB(DataBase)란 여러 사람이 공유하여 사용할 목적으로 쳬계화해 통합 및 관리되는 데이터 집합을 의미한다. [wikipedia](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4) DB 모델은 계층형, 네트워크형 등 여러 형태가 제안되었고, 이러한 데이터 베이스 모델을 관리하는 시스템을 DBMS(Database Management System)이라고 한다. DBMS는 사용자 또는 프로그램의 요구를 처리하고 응답하여 데이터를 원활하게 사용하게끔 해준다. 
 관계형 데이터베이스(Relational Database)는 현재 가장 많이 사용되고 있는 데이터베이스의 한 종류로 PostgreSQL, MySQL, ORACLE이 이 RDBMS(Relational DBMS)에 속한다.

DBMS의 역할은 다음과 같으며,
> 1.  사용자의 질의에 대하여 즉각적인 처리와 응답이 이루어집니다.
> 2. 생성, 수정, 삭제를 통하여 항상 최신의 데이터를 유지합니다.
> 3. 사용자들이 원하는 데이터를 동시에 공유할 수 있습니다.
> 4. 사용자가 원하는 데이터를 주소가 아닌 내용에 따라 참조 할 수 있습니다.
> 5. 응용프로그램과 데이터베이스는 독립되어 있으므로, 데이터의 논리적 구조와 응용프로그램은 별개로 동작됩니다.

관계형 데이터베이스의 테이블은 다음 그림처러 구성되어 있다.
![image](https://user-images.githubusercontent.com/59414764/126282517-167fbd70-b2aa-422a-a8e2-45af566bd02f.png)

테이블은 이름을 가지고 있으며, 행과 열 그리고 거기에 대응하는 값을 가진다.

그리고 SQL은 Structured Query Language의 약자로, DB에서 데이터를 정의, 조작, 제어하기 위해 사용하는 언어를 뜻한다. 예전까지는 C언어를 이용하여 데이터를 관리했다고 한다. 그렇다면 왜 DB로 넘어오게 되었을까? DB는 SQL 명령어만으로 기능을 수행할 수 있고, 처리가 빨라 여러 유저가 동시에 안정적으로 자료 처리가 가능하다. 그리고 데이터의 무결성을 보장해주기 때문에 DB를 사용하게 되었다고 한다.

DB 또한 한계점을 가지고 있다. 압축 파일이나 이미지, 문서 등의 바이너리 파일을 다루기 어렵다는 것이다. 바이너리 파일의 크기가 크기 때문에 읽고 쓸 때 오래걸린다. 그렇게 되면 접속 시간이 길어져 여러 사람이 동시에 사용하는 것도 어렵게 된다.

SQL Mapper: RDBMS를 SQL 쿼리문을 매핑하여 데이터를 객체(Object)화하는 기술을 뜻한다. Mybatis가 여기에 속한다.   
ORM(Object-Relational Mapping): RDBMS에서 쓰이는 테이블을 객체화하는 기술이다. SQL Mapper와 다른 점은 SQL문을 사용하지 않아도 된다는 것이다. Hibernate(JPA 표준 구현체)와 Django ORM, Sequelize(Node.js ORM)이 여기에 속한다.

참고:   
http://tcpschool.com/mysql/mysql_intro_relationalDB
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=varkiry05&logNo=221188182244
https://geonlee.tistory.com/207
https://victorydntmd.tistory.com/195
