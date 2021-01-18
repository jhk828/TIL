# 1. 자바의 Modifier

* `static` + 변수 => 인스턴스 변수가 아닌 클래스 변수 - 모든 객체가 공유
* `static` + 메서드 => 클래스 메서드 - 인스턴스를 생성하지 않고도 메서드 사용 가능
* `final` + 변수 => 상수
* `final `+ 메서드 => Overriding 금지
* `final` + 클래스 => 상속 금지



## 1. `static` 예약어

### `static` + 변수 => 클래스 변수

| 인스턴스 변수 (static x)                                     | 클래스 변수 (static)                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - 생성된 인스턴스마다 그 안에서 클래스의 인스턴스 변수들이 포함된다.<br />- 일반적인 멤버 변수 => 인스턴스 변수<br />- 한 객체의 값이 변경되어도, 다른 객체의 값에 영향을주지 않음 | - 클래스로부터 생성된 모든 객체들이 하나의 클래스 변수를 공유<br />- 객체가 생성될 때 마다 메모리 영역을 할당하지 않고, **클래스가 로딩되는 과정에서 메모리에 한번만 할당**되는 멤버임<br /><br />- 클래스 변수의 값이 변경 => 클래스로부터 생성된 모든 객체에서 변경된 값 사용 가능<br />- 객체를 생성하지 않고도 접근 가능 |

```java
// EmployeeTest.java

class Employee {
	String name;
	int employeeNo;
	int age;
	static String companyName = "S전자"; // 클래스 변수 선언
}

public class EmployeeTest {
	public static void main(String[] args) {
		Employee kim = new Employee();
		System.out.println("kim의 회사명 : " + kim.companyName);
		
		Employee lee = new Employee();
		lee.companyName = "A전자"; // 클래스 변수 수정
		System.out.println("lee의 회사명 : " + lee.companyName); 
		
		Employee park = new Employee();
		System.out.println("park의 회사명 : " + park.companyName); 
		// lee 참조 변수에 의해서 변경된 회사명을 그대로 출력함
		
		// kim의 회사명 : S전자
		// lee의 회사명 : A전자
		// park의 회사명 : A전자
	}
}
```



#### 클래스 변수의 접근

- 클래스 변수는 일반적으로 객체 참조 변수 이름으로 접근하기 보다는 클래스 이름을 통해서 접근함
  - 객체를 생성하지 않고도 클래스 변수에 접근 가능함
- 지금까지 사용했던 자바 출력문은 모두 `System` 클래스의 `out` 클래스 변수다.

![image-20210104015601155](C:\Users\j828h\Desktop\TIL\images\image-20210104015601155.png)



### 클래스 메서드

- 메서드에서도 static 예약어 사용 가능함
- 인스턴스를 생성하지 않고도 메서드 사용 가능
- `Integer` 클래스의 `parseInt()` 메서드가 대표적인 클래스 메서드다.
  - `int age = Integer.parseInt("36");`  // 문자열을 정수로 변환



- 클래스 메서드 -- X --> 인스턴스 변수
  - 인스턴스 변수는 인스턴스를 생성해야만 메모리가 잡히기 때문에 클래스 메서드에서 사용이 불가하다.
- 클래스 메서드 --------> 클래스 메서드
  - **클래스 메서드는 클래스 메서드만 호출 가능하다.**

```java
// StaticMethodTest1.java
class Dice {
	public static int dotCount = 5; // 클래스 변수
	public int rollingCount = 0;    // 인스턴스 변수
	
	public static void playGame() { // 클래스 메서드
		dotCount++; // 클래스 변수 => playGame()에서 접근 가능
		rollingCount++; // 인스턴스 변수 => 클래스 변수 접근 불가
		System.out.println("생성된 숫자 : " + rollingDice()); 
		// 일반 메서드 rollingDice() => 클래스 메서드 playGame()에서 호출 불가
	}
	
	public int rollingDice() { 
		int generatedNum = (int)(Math.random() * 6) + 1;
		return generatedNum;
	}
}

public class StaticMethodTest1 {
	public static void main(String[] args) {
		Dice.playGame();
	}
}
```

```java
// StaticMethodTest2

class Dice {
	public static int dotCount = 5;
	public static int rollingCount = 0; 
	// 클래스 변수 rollingCount는 클래스 메서드 playGame()에서 접근 가능
	
	public static void playGame() {
		dotCount++;
		rollingCount++;
		System.out.println("생성된 숫자 : " + rollingDice());
		// 클래스 메서드 rollingDice() => playGame()에서 접근 가능
	}
	
	public static int rollingDice() {
		int generatedNum = (int)(Math.random() * 6) + 1;
		return generatedNum;	
	}
}

public class StaticMethodTest2 {
	public static void main(String[] args) {
		Dice.playGame(); // 생성된 숫자 : 6
	}
}
```



## 2. `final` 예약어

> `final` + 변수 => 상수, `final `+ 메서드 => Overriding 금지, `final` + 클래스 => 상속 금지

### `final` + 변수

- `final` + 변수 단 한번 초기화 가능, 값 변경 불가
- `static` + `final` + 변수
  - 클래스 변수는, 클래스로부터 생성된 모든 객체들이 동일한 값을 가지는 경우이다.
  - 클래스 변수의 값을 변경할 수 있도록 허용하면 `static` 예약어 의미가 상실되므로 `final` 예약어와 결합하여 사용한다.
- 상수의 이름은 이름은 일반 인스턴스 변수와 구분하기 위해 **모두 대문자로 선언**
  - 여러 단어가 결합된 경우라면 '_' 이용
    - ex) `companyName` => `COMPANY_NAME`

```java
// EmployeeTest.java
class Employee {
	String name;
	int employeeNo;
	int age;
	// static String companyName = "S전자";
	final static String COMPANY_NAME = "S전자"; // 상수 형태의 클래스 변수 선언
}

public class EmployeeTest {
	public static void main(String[] args) {
		Employee kim = new Employee();
		System.out.println("kim의 회사명 : " + kim.COMPANY_NAME);
		
		Employee lee = new Employee();
//		lee.companyName = "A전자";	// 수정 시 문제 발생
		System.out.println("lee의 회사명 : " + lee.COMPANY_NAME); 
	}
}
```



## `final` + 메서드

- 자식 클래스에서 메서드 재정의 금지

![image-20210104150404593](C:\Users\j828h\Desktop\TIL\images\image-20210104150404593.png)



## `final` + 클래스

- 상속 금지

![image-20210104150443910](C:\Users\j828h\Desktop\TIL\images\image-20210104150443910.png)



## 3. `abstract` 예약어

- 클래스 선언시 abstract => 추상 클래스
- 메서드 선언시 abstrct => 추상 메서드

### 추상 메서드

- **메서드의 시그니처 (리턴 타입, 메서드명, 매개변수)**만 정의되고 구체적인 행위 (블록 부분)은 정의되지 않는 메서드
- `abstract int sum(int num1, int num2);`



### 추상 클래스

- 추상 메서드를 포함하는 클래스는 추상 클래스로 선언되어야 한다.
- 추상 클래스가 추상 메서드를 포함하지 않을 수도 있다.

```java
// 추상 메서드를 포함한 추상 클리스
abstract class AbstractClass {
    public abstract void methodA() {...}
    public abstract void methodB() {...}
}
```



```java
abstract class SuperClass {
    // 부모 클래스인 SuperClass에 methodA(), methodB() 두 개의 메서드가 정의됨
    public void methodA() {
        System.out.println("methodA() 실행");
    }
    public abstract void methodB();
}

class SubClass extends SuperClass {
    // 자식 클래스가 상속
    // 상속은 부모 클래스의 모든 변수와 메서드가 자식 클래스로 상속되어 들어오는 개념이다.
    // => SubClass에는 구현되지 않는 methodB()가 추상 메서드로 있는 것과 동일하다.
    // => SubClass를 추상 클래스로 선언하면 객체를 생성할 수 없게 된다.
    // => 따라서 methodB()를 재정의해야 한다.
    public void methodB() {
        System.out.println("methodB() 실행");
    }
}
```



# 2. 생성자

## 1. 생성자 개요

- Constructor는 클래스로부터 객체를 생성할 때 호출되며, 객체의 멤버 변수를 초기화하는 메서드다.
- 클래스와 같은 이름을 가진 메서드다.
- 일반 메서드와 달리 반환형 (Return Type)이 없으며 void도 허용되지 않는다.
- 생성자는 이름은 같지만 매개변수를 달리하여 여러 개를 중복정의 (Overloading)할 수 있다.
- 생성자는 객체를 생성할 때 new 생성자() 구문으로 호출된다.
- 명시적으로 작성하지 않을 경우 기본 생성자가 제공된다.



### 기본 생성자 (Default Constructor)

- 클래스에 생성자가 하나도 정의되지 않은 경우, 컴파일러에 의해 자동으로 생성되는 생성자

- 매개변수가 없는 생성자

  ![image-20210104152904732](C:\Users\j828h\Desktop\TIL\images\image-20210104152904732.png)



```java
class Employee {
	// 생성자를 가지고 있지 않은 클래스 => 기본 생성자 자동 추가
	String name;
	int number;
	int age;
	String title;
	String dept;
	String grade;
}

public class DefaultConstructorTest {
	public static void main(String[] args) {
		Employee kim  = new Employee(); // 기본 생성자로 초기화됨
		System.out.println("이름 : " + kim.name);
		System.out.println("사번 : " + kim.number);
		System.out.println("나이 : " + kim.age);
		System.out.println("직함 : " + kim.title);
		System.out.println("근무 부서 : " + kim.dept);
		System.out.println("등급 : " + kim.grade);
		
//		이름 : null
//		사번 : 0
//		나이 : 0
//		직함 : null
//		근무 부서 : null
//		등급 : null
	}
}
```


### Constructor 생성

- 생성자 자동 생성 : Alt + Shift + S => Generate Constructor using Fields 

```java
class Employee {
	String name;
	int number;
	int age;
	String title;
	String dept;
	String grade;

	// 사원의 이름과 나이를 초기화하는 생성자
	// public Employee(String n, int a) {
	//	name = n;
	//	age = a;
	// }
    
    // Alt + Shift + S => Generate Constructor using Fields
	public Employee(String name, int number, int age, String title, String dept, String grade) {
		super();
		this.name = name;
		this.number = number;
		this.age = age;
		this.title = title;
		this.dept = dept;
		this.grade = grade;
	}
}

public class EmployeeTest {
	public static void main(String[] args) {
		Employee sung = new Employee("성나정", 25); // 매개변수 두 개로 생성자 호출, 객체 생성, 초기화
		System.out.print(sung.name + " 사원의 나이 : " + sung.age);
//		성나정 사원의 나이 : 25
	}
}
```





## 2. `this`의 의미와 사용법

- 생성자나 메서드의 매개변수 이름이 객체 변수의 이름과 같다면, 객체 변수 이름 앞에 `this`를 사용해서 구별한다.
- 일반 메소드에서도 `this` 사용

```java
class Employee {
	String name;
	int age;
	
	public void setName(String name) {
        this.name = name;
    }
    public void setAge(int age) {
        this.age = age;
    }
}
```

