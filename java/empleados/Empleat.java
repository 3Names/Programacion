public abstract class Empleat {
	protected String nom;
	protected double salari;

	public Empleat(String nom) {
		this.nom = nom;
	}

	public abstract void imprimirDetalls();
}
