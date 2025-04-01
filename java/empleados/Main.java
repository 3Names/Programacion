class Main {
	public static void main(String[]args) {
		EmpleatPerHores uno = new EmpleatPerHores("diego",24,30.0);
		EmpleatAsalariat dos = new EmpleatAsalariat("jesus",1500.0);
		EmpleatPerComisio tres = new EmpleatPerComisio("victor",35.0,50.0);
		uno.imprimirDetalls();
		dos.imprimirDetalls();
		tres.imprimirDetalls();
	}
}
