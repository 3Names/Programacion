public class List {
	private int[] elements;
	private int size;
	private int maxSize;
	private int position;

	public List(int size) {
		this.elements = new int[size];
		this.maxSize = size;
		this.size = 0;
		this.position = 0;
	}

	public int length() {
		return this.size;
	}

	public boolean insert(int value) {
		boolean result = false;
		if (this.size < this.maxSize) {
			this.elements[this.position] = value;
			this.size++;
			result = true;
		}
		return result;
	}

	public boolean append(int value) {
		boolean result = false;

		if (this.size < this.maxSize) {
			this.elements[this.size] = value;
			this.size++;
			result = true;
		}

		return result;
	}

	public int remove() throws Exception {//todo: try catch
		if (this.size == 0) {
			throw new Exception("No hay elementos");
		}
		int element = this.elements[this.position];
		
		for (int i = this.position; i < this.size; i++) {
			if ((i + 1) < this.size) {
				this.elements[i] = this.elements[i + 1];
			}
		}
		
		this.size--;

		return element;
	}

	public boolean isEmpty() {
		return this.size == 0;
	}

	public int getValue() throws Exception {
		if (this.size == 0) {
			throw new Exception("No hay elementos");
		}
		return this.elements[this.position];
	}

	public int currPosition() {
		return this.position;
	}

	public void next() {
		if (this.position < (this.size - 1)) {
			this.position++;	
		}
	}

	public void prev() {
		if (this.position > 0) {
			this.position--;
		}
	}

	public void moveToStart() {
		this.position = 0;
	}

	public void moveToEnd() {
		if (this.size > 0) {
			this.position = this.size - 1;
		}
	}

	public boolean moveTo(int position) {
		boolean result = false;

		if (position < this.size) {
			this.position = position;
			result = true;
		}

		return result;
	}

	public boolean isAtEnd() {
		return this.position == this.size - 1;
	}

	public static void main(String[] args) {
		List myLista = new List(4);
		try {
			myLista.remove();
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		System.out.println(myLista.length());
		myLista.insert(4);
		System.out.println(myLista.length());
		try {
			System.out.println(myLista.getValue());
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		myLista.append(7);
		try {
                        System.out.println(myLista.getValue());
                } catch (Exception e) {
                        System.out.println(e.getMessage());
                }
		myLista.next();
		try {
                        System.out.println(myLista.getValue());
                } catch (Exception e) {
                        System.out.println(e.getMessage());
                }
		myLista.moveToStart();
		try {
                        System.out.println(myLista.getValue());
                } catch (Exception e) {
                        System.out.println(e.getMessage());
                }
		try {
                        myLista.remove();
                } catch (Exception e) {
                        System.out.println(e.getMessage());
                }
		try {
                        System.out.println(myLista.getValue());
                } catch (Exception e) {
                        System.out.println(e.getMessage());
                }
		System.out.println(myLista.length());
		myLista.append(9);
		myLista.append(5);
		myLista.append(8);
		myLista.append(1);
		while (!myLista.isAtEnd()) {
			try {
                        	System.out.println(myLista.getValue());
                	} catch (Exception e) {
                        	System.out.println(e.getMessage());
                	}
			myLista.next();
		}
		try {
                        System.out.println(myLista.getValue());
                } catch (Exception e) {
                        System.out.println(e.getMessage());
                }
	}
}
