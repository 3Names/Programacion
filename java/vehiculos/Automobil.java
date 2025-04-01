public class Automobil implements Vehicle{
	protected int velocidad;
	protected String marca;

	public Automobil(String marca) {
		this.marca = marca;
		this.velocidad = 0;
	}

	public void accelerar(int velocidad) {
		this.velocidad = this.velocidad + velocidad;
	}

	public void frenar() {
		if (this.velocidad <= 0) {
			this.velocidad = 0;
			System.out.println("El coche esta parado");
		} 
		else {
			this.velocidad -= 20;
		}
	}

	public void obtenerVelocidadActual() {
		System.out.println("Velocidad actual: " + this.velocidad + "km/h");
	}
}
