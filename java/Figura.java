import java.awt.Color;

public abstract class Figura {
	protected Color color = Color.blue;

	public void setColor(Color c) {
		this.color = c;
	}

	public Color getColor() {
		return this.color;
	}

	public abstract double perimetro();

	public abstract double area();
}
