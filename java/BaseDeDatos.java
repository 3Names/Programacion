import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;

public class BaseDeDatos {
	public static Connection getConnection() {
		String url = "jdbc:mysql://127.0.0.1:33060/biblioteca";
		String user = "root";
		String password = "12";

		try {
			return DriverManager.getConnection(url, user, password);
		} catch (SQLException e) {
			e.printStackTrace();
			return null;
		}
	}

	public static void main(String[] args) {
		Connection c = BaseDeDatos.getConnection();
		if (c != null) {
			try {
				Statement query = c.createStatement();
				ResultSet result = query.executeQuery("SELECT");

				while (result.next()) {
					System.out.println(result.getInt("id") + ": " + result.getString("nom") + " " + result.getString("cognoms"));
				}
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
}
