# Practice
#### 추상클래스란 무엇인가? / What is an Abstract Class?
  * 미완성인 클래스이다. 미완성 메소드를 하나 이상 포함하고 있기때문에 상속을 통해서 자손클래스에서 모두 완성시켜야만 사용할 수 있다.
  * An abstract class is an unfinished class. It includes more than one abstract method which is declared without an implementation. When an abstract class is subclassed, the subclass usually implements all of the abstract methods from the superclass otherwise the subclass must also be declared abstract.

#### 자바의 메모리 구조 / Memory structure of Java
Memory | Desc
------ | ------
CODE | 함수, 제어문, 상수
DATA | 초기화된 전역변수
BSS | 초기화 안된 전역변수
STACK | 지역변수
HEAP | 동적할당
