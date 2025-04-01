public class EmpleatPerHores extends Empleat{
	protected int horasTrabajadas;
	protected double tarifaPorHora;

	public EmpleatPerHores(String nom, int horas, double tarifa) {
		super(nom);
		this.horasTrabajadas = horas;
		this.tarifaPorHora = tarifa;
	}

	public void calcularSalari() {
		this.salari = this.horasTrabajadas * this.tarifaPorHora;
	}

	public void imprimirDetalls() {
		calcularSalari();
		System.out.println("Nombre del trabajador: " + this.nom);
		System.out.println("Salario: " + this.salari);
	}
}
