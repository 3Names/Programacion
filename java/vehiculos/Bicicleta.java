public class Bicicleta implements Vehicle{
	protected int velocidad;
	protected String tipo;

	public Bicicleta(String tipo) {
		this.tipo = tipo;
		this.velocidad = 0;
	}

	public void accelerar(int velocidad) {
		this.velocidad = this.velocidad + velocidad;
	}

	public void frenar() {
		if (this.velocidad <= 0) {
                        this.velocidad = 0;
                        System.out.println("El vehiculo esta parado");
                }
                else {
                        this.velocidad -= 30;
                }
	}

	public void obtenerVelocidadActual() {
		System.out.println("Velocidad actual: " + this.velocidad + "km/h");
	}
}
