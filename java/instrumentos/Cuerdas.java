public abstract class Cuerdas implements Instrumentos {
	protected String sound;
	protected int numerodecuerdas;
	protected String tipocuerda;
	protected boolean trastes;
	protected boolean mastil;
	protected boolean teclado;
	protected boolean resonador;

	public abstract int numeroCuerdas();

	public abstract String tipo();
}
