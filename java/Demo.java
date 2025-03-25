import java.awt.Point;
import java.awt.Color;

public class Demo {
	public static void main(String[] args) {
		Figura[] figuras = new Figura[6];
		figuras[0] = new Circulo(new Point(50,50),40);
		figuras[1] = new Circulo(new Point(100,200),17);
		figuras[2] = new Cuadrado(new Point(90,143),32);
		figuras[3] = new Circulo(new Point(50,90),20);
		figuras[4] = new Cuadrado(new Point(0,0),15);
		figuras[5] = new Poligono(new Point(0,0),4,15);

		for (Figura f : figuras) {
			f.setColor(Color.red);
			System.out.println(f.area());
		}
	}
}
