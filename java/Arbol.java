public class IntNodo {
	private int valor;
	private IntNodo izquierda;
	private IntNodo derecha;

	public IntNodo(int valor) {
		this.valor = valor;
	}
	
	public int getValor() {
		return this.valor;
	}

	public Nodo getIzquierda() {
		return this.izquierda;
	}

	public Nodo getDerecha() {
		return this.derecha;
	}

	public void setIzquierda(Nodo nodo) {
		this.izquierda = nodo;
	}

	public void setDerecha(Nodo nodo) {
		this.derecha = nodo;
	}

	public void setValue(int value) {
		
	}
}

public class Tree {
	private IntNodo root;
	private int profundidad;
	private static int instancias = 0;

	public Tree() {
		this.root = null;
	}
}

public class Main{
	public static void main(String args) {
		IntTree
	}
}
