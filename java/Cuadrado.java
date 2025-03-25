import java.awt.Point;

public class Cuadrado extends Figura {
	protected double lado;
	protected Point punto;

	public Cuadrado(Point punto, double lado) {
		this.punto = punto;
		this.lado = lado;
	}

	public double perimetro() {
		return 4.0 * this.lado;
	}

	public double area() {
		return this.lado * this.lado;
	}
}
