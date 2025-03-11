public class Media {
	private String nom;
	private String autor;
	private int duradaSegons;

	public String getNom() {
		return this.nom;
	}

	public String getAutor() {
		return this.autor;
	}

	public int getDurada() {
		return this.duradaSegons;
	}

	public void setNom(String n) {
		this.nom = n;
	}

	public void setAutor(String a) {
		this.autor = a;
	}

	public void setDurada(int d) {
		this.duradaSegons = d;
	}
}

class media {
	public static void main (String[]args) {
		Media a = new Media();
		a.setNom("xd");
		a.setAutor("El risas");
		a.setDurada(120);
		System.out.println(a.getNom());
		System.out.println(a.getAutor());
		System.out.println(a.getDurada());
	}
}
