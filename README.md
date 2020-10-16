# Practice
#### 추상클래스란 무엇인가? / What is an Abstract Class?
  * 미완성인 클래스이다. 미완성 메소드를 하나 이상 포함하고 있기때문에 상속을 통해서 자손클래스에서 모두 완성시켜야만 사용할 수 있다.
  * An abstract class is an unfinished class. It includes more than one abstract method which is declared without an implementation. When an abstract class is subclassed, the subclass usually implements all of the abstract methods from the superclass otherwise the subclass must also be declared abstract.

#### 자바의 메모리 구조 / Memory structure of Java
Time of Assignment | Territory | Usage
------------------ | --------- | ------
At complie | CODE | 함수, 제어문, 상수
At complie | DATA | 초기화된 전역변수
At complie | BSS | 초기화 안된 전역변수
At complie | STACK | 지역변수
At runtime | HEAP | 동적할당

#### 오버로딩과 오버라이딩 / Overloading and Overriding
  1. Overloading
  * 메소드 이름은 같지만 매개변수의 개수나 데이터 형식을 다르게 정의하는 것
  * 동일한 기능을 수행하는 메소드를 하나로 정의함으로써 메모리를 아낄 수 있다
  * ex) println()
  
  2. Overriding
  * 기존에 있는 메소드를 재정의하는 것으로 매개변수의 개수나 데이터형식이 같아야 한다
  
### 프로세스와 쓰레드의 차이점 / Difference between Process and Thread
https://juyoung-1008.tistory.com/47

### 동기화 / Synchronized
https://12bme.tistory.com/68 - blog reference
1. https://github.com/NikkieS/ClassPractice/blob/master/Java/chapter15%2616/src/ex15_Thread/ThreadMain.java - 메인
2. https://github.com/NikkieS/ClassPractice/blob/8568e4a5d08cb3e066c02c796eea0e7f65357b52/Java/chapter15%2616/src/ex15_Thread/TwoNum.java#L3 - 전역변수 역할
3. https://github.com/NikkieS/ClassPractice/blob/8568e4a5d08cb3e066c02c796eea0e7f65357b52/Java/chapter15%2616/src/ex15_Thread/AccessThread.java#L3 - 쓰레드
