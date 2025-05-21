class Coordenadas<T,R> {
	private T x;
	private R y;

	public Coordenadas(T x, R y) {
		this.x = x;
		this.y = y;
	}

	public T getX() {
		return x;
	}

	public R getY() {
		return y;
	}
}

class Coord {
	public static void main(String[] args) {
		Coordinate<String, Integer> si = new Coordinate<String, Integer>("xd",12);
		Coordinate<String, String> dx = new Coordinate<String, String>("qwe","das");
		Coordinate<Integer, Integer> a = new Coordinate<Integer, Integer>(1,2);
		Coordinate<Boolean, Integer> asd = new Coordinate<Boolean, Integer>(true,22);
	}
}
