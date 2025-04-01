public class EmpleatAsalariat extends Empleat{
	public EmpleatAsalariat(String nom, double salari) {
		super(nom);
		this.salari = salari;
	}

	public void imprimirDetalls() {
		System.out.println("Nombre del trabajador: " + this.nom);
		System.out.println("Salario: " + this.salari);
	}
}
