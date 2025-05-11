import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class ventana extends JFrame {
	private JButton boton;
	private JLabel etiqueta;
	private JTextField campo;

	public ventana() {
		super("");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(300,200);
		etiqueta = new JLabel("Contador:");
		campo = new JTextField(20);
		boton = new JButton("Sumar");
		campo.setText("0");
		boton.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				String cadena = campo.getText();
				int numero = Integer.parseInt(cadena);
				int resultado = numero + 1;
				String valor = String.valueOf(resultado);
				campo.setText(valor);
			}
		});
		JPanel panel = new JPanel();
		panel.add(etiqueta);
		panel.add(campo);
		panel.add(boton);
		add(panel);
		setVisible(true);
	}
	public static void main(String[] args) {
		new ventana();
	}
}
