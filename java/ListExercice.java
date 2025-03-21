class Elem {
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

	public void setNext(Elem next) {
		this.next = next;
	}
}

public class ListExercice {
	private Elem firstElement;
	private Elem element;
	private int position;
	private int length;
	/*operaciones*/
	public ListExercice() {
		this.position = -1;
		this.length = 0;
		this.element = null;
		this.firstElement = null;
	}

	public int length() {
		return this.length;
	}

	public void insert(int value) {
		Elem nextElement = new Elem(value);
		if (this.length == 0) {
			this.element = nextElement;
			this.position = 0;
			this.firstElement = this.element;
		} else {
			nextElement.setNext(this.element.getNext());
			this.element.setNext(nextElement);
		}
		this.length++;
	}

	public void append(int value) {
		Elem nextElement = new Elem(value);
		if (this.length == 0) {
			this.element = nextElement;
			this.position = 0;
			this.firstElement = this.element;
		} else {
			int i = this.position;
			Elem temporary = this.element;

			while (i < this.length - 1) {
				temporary = temporary.getNext();
				i++;
			}

			temporary.setNext(nextElement);
		}

		this.length++;
	}

	public int remove() {
		Elem copiaCurrent = this.element;
		this.element = this.element.getNext();
		copiaCurrent.setNext(null);
		Elem copiaFirst = this.firstElement;
		int i = 0;
		while (i < this.position) {
			copiaFirst = copiaFirst.getNext();
			i++;
		}
		copiaFirst.setNext(this.element);
		this.length--;

		return copiaCurrent.getValue();
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
		this.element = this.element.getNext();
		this.position = this.position + 1;
	}

	public void prev() {
		
	}

	public void moveToStart() {
		this.element = this.firstElement;
		this.position = 0;	
	}

	public void moveToEnd() {
	
	}

	public void moveToPos(int pos) {
		
	}

	public boolean isAtEnd() {
		return this.position == (this.length - 1);
	}

	public static void main(String[] args) {
		ListExercice myLista = new ListExercice();
		System.out.println(myLista.length());
		myLista.append(9);
		myLista.append(5);
		myLista.append(8);
		myLista.append(1);
		myLista.remove();
		System.out.println(myLista.length());
		System.out.println(myLista.getValue());
	}
}
