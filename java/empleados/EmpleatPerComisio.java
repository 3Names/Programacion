public class EmpleatPerComisio extends Empleat {
	protected double ventasRealizadas;
	protected double comisionPorVenta;

	public EmpleatPerComisio(String nom,double ventas, double comision) {
		super(nom);
		this.ventasRealizadas = ventas;
		this.comisionPorVenta = comision;
	}

	public void calcularSalari() {
		this.salari = this.ventasRealizadas * this.comisionPorVenta;
	}

	public void imprimirDetalls() {
		calcularSalari();
		System.out.println("Nombre del trabajor: " + this.nom);
		System.out.println("Salario: " + this.salari);
	}
}
