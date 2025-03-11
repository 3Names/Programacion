public class Dogo {
	public static void main(String[] args) {
		Dog mydog = new Dog("xd");
		Dog otherdog = new Dog("dx");
		System.out.println(mydog.bark());
		System.out.println(otherdog.bark());
	}
}

class Dog{
	String name;

	public Dog(String name) {
		this.name = name;
	}

	public static String bark() {
		return " says wof wof";
	}
}
