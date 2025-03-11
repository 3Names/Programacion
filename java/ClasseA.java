public class ClasseA {
	private int valorPrimari;
	private int valorSecondari;
	public ClasseA() {
		this.valorPrimari = 5;
		this.valorSecondari = 10;
	}

	public ClasseA(int vp) {
		this.valorPrimari = vp;
		this.valorSecondari = 10;
	}

	public ClasseA(int vp, int vs) {
		this.valorPrimari = vp;
		this.valorSecondari = vs;
	}

	public int getPrimari() {
		return this.valorPrimari;
	}

	public int getSecundari() {
		return this.valorSecondari;
	}
}

class instancia {
	public static final void main (String[]args) {
                ClasseA a = new ClasseA();
                ClasseA b = new ClasseA(20);
                ClasseA c = new ClasseA(20,40);
                System.out.println("El objeto _a:_ contiene: " + a.getPrimari() + ", " + a.getSecundari());
                System.out.println("El objeto _b:_ contiene: " + b.getPrimari() + ", " + b.getSecundari());
                System.out.println("El objeto _c:_ contiene: " + c.getPrimari() + ", " + c.getSecundari());
       }
}
