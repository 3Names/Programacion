private class Elem {
	private int value;
	private Elem next;

	public Elem(int value) {
		this.value = value;
	}

	public int getValue() {
		return this.value;
	}

	public Elem getNext() {
		return this.next;
	}

	public Elem setNext(Elem next) {
		this.next = next
	}
}

public class List {
	
	private Elem element;
	private int position;
	private int length;
	/*operaciones*/
	public List() {
		this.position = -1;
		this.length = 0;
		this.element = null;
	}

	public int length() {
		return this.length;
	}

	public void insert(int value) {
		
	}

	public void append(int value) {
		
	}

	public int remove() {
		return 0;
	}

	public boolean isEmpty() {
		return this.length() == 0;
	}

	public int getValue() {
		return this.element.getValue();
	}

	public int currentPosition() {
		return this.position;
	}

	public void next() {
		this.element = this.element.next();
		this.position = this.position + 1;
	}

	public void prev() {
		
	}

	public void moveToStart() {
		
	}

	public void moveToEnd() {
	
	}

	public void moveToPos(int pos) {
		
	}

	public boolean isAtEnd() {
		return true;
	}
}
