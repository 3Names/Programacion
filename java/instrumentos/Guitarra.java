public class Guitarra extends Cuerdas{
	public Guitarra() {
		this.sound = "hola";
		this.numerodecuerdas = 12;
		this.tipocuerda = "pulsada";
		this.trastes = true;
		this.mastil = true;
		this.teclado = false;
		this.resonador = false;
	}

	public void makeSound() {
		System.out.println(this.sound);
	}
	public int numeroCuerdas() {
		return this.numerodecuerdas;
	}
	public String tipo() {
		return this.tipocuerda;
	}

	public static void main(String[] args){
		Guitarra guitarra = new Guitarra();
		guitarra.makeSound();
		System.out.println(guitarra.numeroCuerdas());
		System.out.println(guitarra.tipo());
	}
}
