public class Stack {

	public Stack(int size) {
		this.stackArray = new int[maxSize];
		this.top = -1;
	}
	
	public void push(int element) {
		if (this.top == this.maxSize - 1) {
			System.out.println("Stack overflow");
			return;
		}

		this.top += 1;
		this.stackArray[this.top] = element;
	}

	public int pop() {
		if (this.top == -1) {
			System.out.println("Stack underflow");
			return -1;
		}
		
		int poppedElement = this.stackArray[this.top];
		this.top -= 1;
		return this.stackArray[this.top];
	}

	public boolean isEmpty() {
		return this.top == -1;
	}

	public int top() {
		if (this.top == -1) {
			System.out.println("Stack is empty");
			return -1;
		}

		return this.stackArray[this.top];
	}

	public static void main(String[] args) {
		Stack stack = new Stack(5);
		stack.push(10);
		stack.push(20);

		System.out.println("Stack top element: " + stack.top());

		stack.pop();
		stack.pop();
		stack.pop();

		System.out.println("Is stack empty? " + stack.isEmpty());
	}
}
