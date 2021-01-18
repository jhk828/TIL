# 1. 객체지향 개념

## 1. 객체지향의 개념

- 1960년 말, 소프트웨어 위기론의 등장
- hw 발전 속도를 sw가 따라가지 못함
- 하드웨어처럼 모듈화되어 재사용, 유지보수가 용이하게끔 객체지향 개발론 대두

### 절차지향

- 실행되는 순서가 위에서부터 아래로 순차적으로 진행되는 형태
- 함수 : 자주 사용되는 특정 코드를 하나의 모듈(묶음)으로 묶어두어
  - 프로그래머가 사용하고 싶을 때마다 호출하여 코드가 실행되게 함
  - 그러나, 데이터와 함수 간에 유기적인 관계성을 갖지 못함

### 객체지향

- 보다 높은 유지보수 유지가 가능해짐
- 객체와 갹체 간 자유로운 데이터 이동이 가능해짐
- 변수, 메소드 in 객체

## 2. 객체, 클래스, 인스턴스

1. 객체 (Object)
   - <u>현실 세계에 존재하는 유무형의 모든 것</u>, 사람들이 의미를 부여하고 분류하는 논리적인 단위
   - ex) 자동차라는 객체 
- 정적인 요소 : 변수 (Variable)
   - 동적인 요소 : Method
   
2. 클래스 (Class)
      - <u>현실 세계의 객체를 컴퓨터 메모리에 생성할 수 있는 템플릿</u>, 자바 응용 프로그램을 구성하는 가장 
      - ex) class Car 

3. 인스턴스 (Instance)

   - <u>객체가 컴퓨터 메모리에 올라간 것, 메모리 상의 객체</u>
   - ex) Blue Car, Red Car, Orange Car
   - 다양한 자동차 인스턴스를 메모리에 생성 가능
   - 편의상 생성된 인스턴스와 객체를 동일한 용어로 이해할 수 있다.



```java
// Car.java
public class Car {
	
	// 멤버 변수 선언 - 객체의 속성을 나타냄
	String name;
	int currentSpeed;
	int currentGear;
	
	// 메서드 선언 - 변수를 이용하여 구체적인 행위를 제공
	void strartEngine() {
		System.out.println("-> " + name + "의 시동을 켠다.");
		currentSpeed = 1;
	}
	
	void changeGear(int gear) {
		System.out.println("-> 기어를" + gear + "단으로 변경한다.");
		currentGear = gear;
	}
	
	int getCurrentSpeed() {
		currentSpeed = currentSpeed + (currentGear * 10);
		return currentSpeed;
	}
	
	void stopEngine() {
		System.out.println("-> " + name + "의 시동을 끈다.");
		currentSpeed = 0;
		currentGear = 0;
	}
	
	String getCurrentState() {
		return name + "의 현재 속도 : " + getCurrentSpeed();
	}
}
```



```java
// CarTest.java

public class CarTest {

	public static void main(String[] args) {
		// Car 객체 (Instance) 생성
		Car myCar = new Car();
		
		// 초기 값 설정
		myCar.name = "Red";
		myCar.currentGear = 0;
		myCar.currentSpeed = 0;
		
		// 메서드 호출
		myCar.strartEngine();
		System.out.println(myCar.getCurrentState());
		
		myCar.changeGear(2);
		System.out.println(myCar.getCurrentState());
		
		myCar.changeGear(3);
		System.out.println(myCar.getCurrentState());
		
		myCar.stopEngine();
		System.out.println(myCar.getCurrentState());
		
//		-> Red의 시동을 켠다.
//		Red의 현재 속도 : 1
//		-> 기어를2단으로 변경한다.
//		Red의 현재 속도 : 21
//		-> 기어를3단으로 변경한다.
//		Red의 현재 속도 : 51
//		-> Red의 시동을 끈다.
//		Red의 현재 속도 : 0
	}
}
```



# 2. 객체지향 언어의 주요 개념

## 1. 상속과 다형성

### 상속 (Inheritance)

- 코드의 재사용성을 높인다.
- 상속을 통해 <u>객체들 사이의 계층 구조</u>를 이룰 수 있다.
  - 상위 형태로 갈 수록 일반화, 보편화 <=> 특수화

```java
// Taxi.java
public class Taxi extends Car {
	
	int fare; // 요금
	boolean passengerYn; // 승객 유무
}
```

```java
// CarTest.java
public class CarTest {

	public static void main(String[] args) {		
		// Car 객체 (Instance) 생성
		Taxi myTaxi = new Taxi();
		
		// 초기 값 설정
		myTaxi.name = "대현 운수 308";
		myTaxi.currentGear = 2;
		myTaxi.fare = 3400;
		myTaxi.passengerYn = true;
		System.out.println(myTaxi.getCurrentState());
		// 대현 운수 308의 현재 속도 : 20
	}
}
```



### 상속의 논리적 관계

- 부모 클래스 - 자식 클래스의 관계가 논리적으로 **일반화, 특별화 관계 IS-A**에 있어야 한다.



### 상속의 종류

- 클래스의 상속은 1 하위 클래스 -> 1 상위 클래스인 단일 상속이 일반적
- 두 개 이상의 상위 클래스를 갖는 다중 상속 (Multiple Inheritance) 
- 자바는 단일 상속만을 지원



### 다형성 (Polymorphism)

- **one interface, multiple implementation**
- 하나의 인터페이스를 이용해 서로 다른 구현을 제공한다.
- 다형성은 메서드 오버로딩과 메서드 오버라이딩을 통해 지원된다.

#### Overloading

- 한 클래스 안에 같은 이름의 메서드를 여러 개 정의
- 인자의 개수느 유형을 다르게

#### Overriding

- 상속 관계에 있는 하위 클래스가 상위 클래스가 가지고 있는 메서드를 **재정의**하는 것
- 재정의된 메서드가 선언된 형태는 상위 클래스에서 선언된 것과 같음



## 2. 추상화, 캡슐화, 정보 은닉, 메시지

### 추상화 (Abstraction)

- 구체적인 사실들을 일반화시켜 기술하는 것
- 현실 세계에 존재하는 다양한 객체들의 <u>공통된 특성을 모아 일반화</u>해 놓는 것
  - 클래스 정의에 중요한 역할
- 비행기, 자동차, 열차, 배 등 운송수단의 동일한 특징 - 화물이나 승객을 운반한다
  - 이를 운송수단이라는 클래스로 정의한다.

### 캡슐화 (Encapsulation)

- 변수와 메소드을 하나의 **추상화된 클래스로 묶는 과정**
  - 변수와 메서드를 하나로 묶어 독립적으로 동작하지 않도록 한다.
- 객체가 제공하는 메서드를 통해 객체를 이용하고, 데이터가 실제로 어떻게 처리되는지 알 필요가 없음

### 정보 은닉 (Information Hiding)

- 객체지향 언어에서는 캡슐화된 변수나 메서드를 선택적으로 공개 (Public)하거나 숨길 수 있음 (Private)

```java
// Car.java
public class Car {
	
	// 멤버 변수 선언 
	public String name; 
	private int currentSpeed;
	public int currentGear;
	
	// 메서드 선언 
	public void strartEngine() {
		System.out.println("-> " + name + "의 시동을 켠다.");
		currentSpeed = 1;
	}
	
	public void changeGear(int gear) {
		System.out.println("-> 기어를" + gear + "단으로 변경한다.");
		currentGear = gear;
	}
	
	private int getCurrentSpeed() {
		currentSpeed = currentSpeed + (currentGear * 10);
		return currentSpeed;
	}
	
	public void stopEngine() {
		System.out.println("-> " + name + "의 시동을 끈다.");
		currentSpeed = 0;
		currentGear = 0;
	}
	
	public String getCurrentState() {
		return name + "의 현재 속도 : " + getCurrentSpeed();
	}
}
```



### 메시지 (Message)

- 객체 간에 서로 통신하는 방법
- 객체 간에 메시지를 주고받기 때문에 여러 객체는 동일한 프로세스를 가질 필요 없다.
- 서로 메시지를 주고받는 데 객체가 존재하는 위치는 제약이 되지 않음.

- 메시지를 전달할 대상 객체인 `car`, 전달할 메시지인 `changeGear()`, 메시지를 통해 전달하고 싶은 부과 정보가 있다면 해당 정보인 `lowerGear`
  - 홍길동의 자동차 객체 : car <-- `car.changeGear(lowerGear)`--- 홍길동: Hong

```java
// Driver.java
public class Driver {
	String name;
	
	void driving() {
		Car myCar = new Car();
		
		myCar.name = "Red";
		myCar.currentGear = 0;
		myCar.currentSpeed = 0;
		
		// 메서드 호출
		myCar.strartEngine();
		System.out.println(myCar.getCurrentState());
		
		myCar.changeGear(2);
		System.out.println(myCar.getCurrentState());
		
		myCar.changeGear(3);
		System.out.println(myCar.getCurrentState());
		
		myCar.stopEngine();
		System.out.println(myCar.getCurrentState());
	}
}
```



```java
// CarTest.java
public class CarTest {

	public static void main(String[] args) {

		// 운전자 객체 생성
		Driver kim = new Driver();
		kim.name = "성나정";
		
		System.out.println(kim.name + "이 운전합니다.");
		kim.driving();
		
//		성나정이 운전합니다.
//		-> Red의 시동을 켠다.
//		Red의 현재 속도 : 1
//		-> 기어를2단으로 변경한다.
//		Red의 현재 속도 : 21
//		-> 기어를3단으로 변경한다.
//		Red의 현재 속도 : 51
//		-> Red의 시동을 끈다.
//		Red의 현재 속도 : 0
	}
}
```

