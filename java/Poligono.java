import java.awt.Point;
public class Poligono extends Figura{
	protected Point punto;
	protected double lados;
	protected double longitud;

	public Poligono(Point punto, double lados, double longitud) {
		this.punto = punto;
		this.lados = lados;
		this.longitud = longitud;
	}
	
	public double apotema() {
		return this.longitud / 2 * Math.tan(Math.PI/this.lados);
	}
	
	public double perimetro() {
		return this.longitud * this.lados;
	}

	public double area() {
		return (this.lados * this.longitud * this.apotema());
	}	
}
