# 1. 인터페이스와 다형성

## 1. 인터페이스

### 추상 클래스와 인터페이스

![image-20210110233721396](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210110233721396.png)

![image-20210110233755145](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210110233755145.png)

인터페이스는 상수와 추상 메서드 외에 다른 멤버를 갖지 못하게 한다.



![image-20210110233850921](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210110233850921.png)

### 인터페이스를 사용하는 이유

![image-20210110233953953](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210110233953953.png)

![image-20210110234013994](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210110234013994.png)



```java
public interface 인터페이스명 [extends 부모인터페이스며, ...] {
    // 상수 
    // - final 예약어로 멤버 변수를 선언해야 함
    // - 인터페이스는 객체를 생성할 수 없으므로, 상수는 static 예약어로 선언해야 함
    // 추상 메서드
    // 그러나 static final, abstract 생략 가능
}
```





## 2. 인터페이스의 활용

![image-20210110234927195](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210110234927195.png)

![image-20210110235031524](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210110235031524.png)

```java
interface Drawable {
	public int PLAIN_PEN = 1;
	public int BOLD_PEN = 2;
	public int ITALIC_PEN = 3;
	public void draw();				// 추상 메서드
	public void move(int x, int y); // 추상 메서드
}

class Shape {
	int x = 0;
	int y = 0;
	
	Shape(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

class Circle extends Shape implements Drawable {
	int radius;
	
	Circle(int x, int y, int radius) {
		super(x, y);
		this.radius = radius;
	}
	
	public void draw() {
		// Overriding
		System.out.println("(" + x + ", " + y + ") radius = " + radius);
	}
	
	public void move(int x, int y) {
		// Overriding
		System.out.println("(" + (this.x + x) + ", " + (this.y + y) + ") radius = " + radius);
	}
}

class Rectangle extends Shape implements Drawable {
	int width;
	int height;
	
	Rectangle(int x, int y, int width, int height) {
		super(x, y);
		this.width = width;
		
		this.height = height;
	}
	
	public void draw() {
		// Overriding
		System.out.println("(" + x + ", " + y + ") "
				+ "width = " + width + ", height = " + height);
	}
	
	public void move(int x, int y) {
		// Overriding
		System.out.println("(" + (this.x + x) + ", " + (this.y + y) + ") "
				+ "width = " + width + ", height = " + height);
	}
}

public class InterfaceTest1 {
	public static void main(String[] args) {
		Circle c = new Circle(10, 10, 100);
		c.draw();
		c.move(5, 5);
		
		Rectangle r = new Rectangle(20, 20, 50, 50);
		r.draw();
		r.move(5, 10);
	}
}
//	(10, 10) radius = 100
//	(15, 15) radius = 100
//	(20, 20) width = 50, height = 50
//	(25, 30) width = 50, height = 50
```



### 형변환

![image-20210111001937313](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111001937313.png)

```java
public class InterfaceTest1 {
	public static void main(String[] args) {
		// Circle c = new Circle(10, 10, 100);
		Drawble d = new Circle(10, 10, 100);
		// 자식 클래스 객체는 부모 타입 참조 변수에 할당 가능 / 인터페이스도
		d.draw();
		d.move(5, 5);
		
		// Rectangle r = new Rectangle(20, 20, 50, 50);
		d = new Rectangle(20, 20, 50, 50);
		d.draw();
		d.move(5, 10);
	}
}
```



### 인터페이스의 상속

인터페이스도 extends 예약어로 상속 가능

![image-20210111002700825](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111002700825.png)

```java
interface Paintable {
	public void paint();
}

interface Drawable {
	public int PLAIN_PEN = 1;
	public int BOLD_PEN = 2;
	public int ITALIC_PEN = 3;
	public void draw();				// 추상 메서드
	public void move(int x, int y); // 추상 메서드
}

interface Printable extends Paintable, Drawable {
	public void print();
	// Paintable, Drawable로부터 
	// 모든 상수와 추상 메서드를 상속하고 있는 print() 추상 메서드 추가
}

class Shape {
	int x = 0;
	int y = 0;
	
	Shape(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

class Circle implements Printable {
	public void draw() {
		System.out.println("원을 그립니다.");
	}
	
	public void move(int x, int y) {
		System.out.println("원을 이동시킵니다. : (" + x + "," + y + ")");
	}
	
	public void paint() {
		System.out.println("원을 색칠합니다.");
	}
	
	public void print() {
		System.out.println("원을 출력합니다.");
	}
}


public class InterfaceTest2 {
	public static void main(String[] args) {
		Circle c = new Circle();
		c.draw();
		c.move(5, 5);
		c.paint();
		c.print();
	}
}
//	원을 그립니다.
//	원을 이동시킵니다. : (5,5)
//	원을 색칠합니다.
//	원을 출력합니다.
```





# 2. 객체지향 언어의 주요 개념

## 1. 패키지 개요

### 자바 API 패키지

![image-20210111003550119](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111003550119.png)



![image-20210111003636020](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111003636020.png)



### `import` 예약어

![image-20210111003856031](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111003856031.png)



#### 다른 패키지의 클래스 사용하기

![image-20210111004103806](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004103806.png)

![image-20210111004114281](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004114281.png)

![image-20210111004153465](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004153465.png)

![image-20210111004208425](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004208425.png)



#### 여러 패키지에 동일한 이름의 클래스를 import 하는 경우

![image-20210111004240337](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004240337.png)



![image-20210111004319552](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004319552.png)

![image-20210111004332922](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004332922.png)

### 2. 사용자 정의 패키지

#### package의 개념
![](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004507900.png)
![](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004522419.png)

![image-20210111004631176](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004631176.png)



#### package 예약어

![image-20210111004657752](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004657752.png)

![image-20210111004737339](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004737339.png)

![image-20210111004754728](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004754728.png)

![image-20210111004810968](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111004810968.png)

![image-20210111005300747](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005300747.png)



#### 사용자 정의 패키지와 `import`

![image-20210111005347920](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005347920.png)



![image-20210111005414273](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005414273.png)

![image-20210111005422621](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005422621.png)

## 2. 커스텀 라이브러리 사용

#### 커스텀 라이브러리 사용하기

자바는 프로그램 구현에 필요한 중요 클래스들을 API 형태로 JVM에 포함

![image-20210111005514489](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005514489.png)

![image-20210111005536971](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005536971.png)

![image-20210111005603256](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005603256.png)

![image-20210111005624431](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005624431.png)

![image-20210111005639780](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005639780.png)

![image-20210111005717344](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005717344.png)

![image-20210111005919378](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005919378.png)

![image-20210111005940660](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111005940660.png)



### 3. 커스텀 라이브러리 사용

![image-20210111010008870](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111010008870.png)

![image-20210111010020810](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111010020810.png)

![image-20210111010042960](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111010042960.png)

![image-20210111010054058](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111010054058.png)

![image-20210111010102027](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111010102027.png)

![image-20210111010113400](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111010113400.png)

![image-20210111010123388](C:\Users\j828h\Desktop\TIL\Java_basic\images\image-20210111010123388.png)