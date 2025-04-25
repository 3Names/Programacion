public class Arbol {
	private IntNodo root;
	private int profundidad;
	private int nbNodes;
	private static int instancias = 0;

	public Arbol() {
		this.root = null;
		this.profundidad = 0;
		instancias++;
	}

	public Arbol(int prof) {
		this.profundidad = prof;
	}

	public static int getCurrentInstances() {
		return instancias;
	}

	public int getProfundidad() {
		return this.profundidad;
	}

	public void add(int valor) {
		int aux = this.profundidad;
		this.root = addRecursive(this.root, valor, aux);
	}

	private IntNodo addRecursive(IntNode actual, int valor, int prof) {
		if (actual == null) {
			actual = new IntNode(valor);
			this.nbNodos++;
			if (((2^prof) - 1) < this.nbNodes) {
				this.depth++;
			}
		} else {
			if (this.nbNodes < ((2^prof) - 1) / 2) {
				IntNode left = current.getLeft();
				actual = this.addRecursive(left, valor, prof - 1);
			}
			else {	
				IntNode right = current.getLeft();
				actual = this.addRecursive(right, valor, prof - 1);
			}
		}

		return current;
	}
}

public class Main{
	public static void main(String args) {
		IntTree
	}
}
