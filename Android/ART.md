먼저 컴퓨터 언어에 대해서 알아보기로 하겠다! 
출처:  
번역기(컴파일러, 인터프리터) - https://imasoftwareengineer.tistory.com/43  
JVM이란? - https://asfirstalways.tistory.com/158  



# 프로그래밍 언어 번역기
### Compiler  
이때동안 배웠던 C/C++언어는 컴파일러를 통해 기계어로 번역이 된다.  
전처리, 링크, 컴파일 등 과정을 통해 칩(CPU나 MCU) 명령어 세트에 맞는 기계어 실행파일이 생성되며, 사용자는 바로 실행파일을 사용하면 되기 때문에, 빠르다는 장점이 있다.
하지만 미리 칩에 맞게 번역되었기 때문에, 다른 기기에서는 사용이 어렵다. 

### Interpreter  
내가 많이 쓰고 있는 파이썬의 경우에는 컴파일러가 아닌 인터프리터를 사용한다.  
인터프리터는 번역해야 할 파일을 한 줄씩 실행시키는 원리다.  
컴파일러는 실행파일을 미리 만들어두는 데에 반해, 인터프리터를 사용하는 언어는 각 기계에 맞는 인터프리터만 있으면, 어느 기계에서든 똑같이 작성된 파일로 실행이 가능하다.  
하지만, 실행할 때마다 인터프리터를 거쳐야하는 만큼 속도가 느리다는 단점이 있다.

### 하이브리드(Compiler-Interpreter-Compiler)
컴파일러와 인터프리터을 합친 하이브리드 형식의 번역기가 존재한다. 대표적으로 이제부터 배울 JAVA, Kotlin이 이러한 방식으로 번역이 된다.  
먼저, 자바, 코틀린 파일을 각자의 컴파일러를 통해 16진수 바이트코드( .class 파일 )로 컴파일한다. 그리고 사용자가 파일을 실행하면, 자바 인터프리터가 바이트코드를 한 줄씩 번역해 CPU에 실행시킨다. 여기에서 쓰이는 인터프리터는 JVM(Java Virtual Machine)의 일부분으로 작동하며, 인터프리터를 거쳐서 바로 실행되는 것이 아닌, JIT(Just-In-Time) 컴파일러를 거쳐서 기계어로 번역이되고 실행되는 것이다. (참고로 코틀린은 코틀린 런타임 라이브러리(Kotlin Runtime Library)가 필요하다.)  

# Virtual Machine  

## JVM (Java Virtual Machine)
JVM의 역할: 자바, 코틀린 Application을 클래스 로더를 통해 읽어들이고 자바 API나 코틀린 런타임 라이브러리(코틀린 API + 확장 자바 API)와 함께 실행하는 것이다.  
그리고 OS와 중개자 역할을 수행하여 자바, 코틀린이 OS에 구애받지 않고 재사용을 가능하게 해준다. 그리고 메모리 관리, Garbage Collection 역할도 수행한다.  
ARM 아키텍처 하드웨어는 레지스터 기반(피연산자가 레지스터에 저장되어있고, 동작이 빠르다. 대신 레지스터 주소가 포함되어있기 때문에 명령어가 길다.)으로 동작하는데 비해 JVM은 스택 기반(피연산자를 stack구조로 저장하여 pop으로만 동작)으로 동작한다.

> GC(garbage collection): 메모리 관리 기법 중 하나로, 프로그램이 동적 할당했던 메모리 영역 중에서 필요없게 된 영역을 해제하는 기능을 한다. 비어있는 메모리에 접근하거나 메모리가 누수됨에 따라 발생하는 버그를 막을 수 있다는 장점이 있으며, 메모리 해제 시점을 추적하므로 메모리 해제 결정 비용이 든다. [wiki](https://ko.wikipedia.org/wiki/%EC%93%B0%EB%A0%88%EA%B8%B0_%EC%88%98%EC%A7%91_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99))  
 
![image](https://user-images.githubusercontent.com/59414764/116506706-c11a1580-a8f8-11eb-8724-2608cc3aa5f4.png)

실행 과정:  
1. 프로그램이 실행되면 OS로부터 필요한 메모리를 할당받고, 용도에 따라 영역을 나눈다.
2. 자바 컴파일러(javac)가 자바 소스코드(.java)를 읽고 바이트코드(.class)로 변환시킨다.
3. Class Loader를 통해 바이트코드 파일을 JVM에 가져오고(Load) 배치(Link)한다.
4. Execution Engine을 통해 .class파일을 번역 및 실행한다. 내부에 인터프리터 또는 JIT컴파일러가 존재한다. 
5. 해석된 class파일은 Runtime Dtat Area에 배치되고, 기계어가 실행된다.


## DVM (Dalvik Virtual Machine)

DVM은 안드로이드 애플리케이션을 실행할 수 있는 가상 머신이다. JVM을 사용하지 않는 이유는, 모바일 기기의 특성상 배터리 수명과 컴퓨팅 파워, 메모리가 Desktop PC 환경보다 열악하기 때문이다.  
![image](https://user-images.githubusercontent.com/59414764/116521385-dbf78480-a90e-11eb-9730-d628e76ffb00.png)  
JVM처럼 .java 파일이 자바 바이트 코드 .class로 변환되고, Dex 컴파일러가 여러 개의 class파일을 모아~~(링크?)~~ dex파일로 변경한다. 이 dex파일에는 리소스(MainActivity, xml, etc)를 포함한 기타 라이브러리(package, .h) 등이 압축되어 APK(Android Application Package, jar나 zip같은 일종의 압축파일)가 완성된다. DVM에서도 JIT 내부 컴파일러를 사용한다.  

특징: JVM 스택 기반 모델과 다르게 레지스터 기반 모델을 사용한다. 그렇게 때문에 JVM보다 빠르게 동작한다.


대망의  
## ART(Android Runtime)  
ART는 안드로이드 애플리케이션 런타임 환경으로 디버깅(시스템 논리적 오류나 비정상적 연산(버그) 검출 및 수정) 기능과 애플리케이션 프로파일링(앱 성능 측정) 기능을 제공한다.  
JIT는 기계어 번역 결과를 캐쉬에 저장하여 메모리 캐시가 필요하다(앱 구동 중 실시간으로 기계어 번역)는 단점이 있다. AOT(Ahead Of Time)은 ART의 내부 컴파일러다. JIT와 달리 애플리케이션이 설치되는 시점에 전체 바이트 코드를 기계어로 번역한다. 그래서 설치 시간이 길다는 점이 있지만, 바이트 코드 해석 시간을 없앰으로써 퍼포먼스(실행 속도)가 좋아지고 배터리 수명이 향상된다. 단점으로는 앱 설치 공간이 많이 든다는 점이다.

- 쉬운 설명 JIT vs AOT  
JIT 이전에는 외국어 매뉴얼을 비행하는 도중에 계속 해석해 가면서 읽고 비행을 했다고 한다면, JIT는 비행 이전에 아 이번에 비행할 때에는 이런이런 부분을 쓰겠구나 하고 적당히 해석하면서 메모한 뒤 비행을 하는 것이고, AOT는 비행 메뉴얼을 받아오는 시점에서 완전히 번역해 놓고 번역본을 원본 매뉴얼과 함께 구비한 뒤에 번역본을 계속 읽으면서 비행하는 식이다. JIT는 책상 위가 항상 어지러울 것이고, AOT는 선반 위의 공간이 부족해지는 사태가 발생할 것이다.  [AOT wiki](https://namu.wiki/w/%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C%20%EB%9F%B0%ED%83%80%EC%9E%84)  
+) 번외로, 안드로이드의 성능 향상을 위한 다른 기법으로는 NDK가 있다. 이는 이 비행기는 특정 언어를 쓰는 파일럿이 조종할 것이라고 상정하고 제조사부터가 해당 언어로 작성된 매뉴얼을 제공하는 것. 번역의 과정을 추가로 거칠 필요가 없고, 해당 언어의 특성을 제대로 활용할 수 있어 성능이나 효율상으로는 꽤 매력적인 옵션이다.  