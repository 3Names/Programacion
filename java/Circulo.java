import java.awt.Point;

public class Circulo extends Figura {
	protected Point centro;
	protected double radio;

	public Circulo(Point centro, double radio) {
		this.centro = centro;
		this.radio = radio;
	}
	
	public double perimetro() {
		return 2.0 * Math.PI * radio;
	}

	public double area() {
		return Math.PI * radio * radio;
	}

	public void expandir(double escalar) {
		this.radio = this.radio * escalar;
	}
}
