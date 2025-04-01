class Main {
	public static void main(String[]args) {
		Automobil uno = new Automobil("Audi");
		Bicicleta dos = new Bicicleta("Montaña");
		uno.accelerar(50);
		uno.obtenerVelocidadActual();
		uno.frenar();
		uno.frenar();
		uno.frenar();
		uno.frenar();
		dos.accelerar(60);
		dos.frenar();
		dos.obtenerVelocidadActual();
		dos.frenar();
		dos.obtenerVelocidadActual();
	}
}
