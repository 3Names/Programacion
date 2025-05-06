import java.awt.*;
import java.awt.event.*;

public class ExWindow extends Frame implements ActionListener {
	private TextField campoEscribir;
	private Label areaResultado;
	private Button botonMostrar;

	public ExWindow() {
		setTitle("");
		setSize(600,500);
		setLocationRelativeTo(null);

		setLayout(new FlowLayout());
		Label nameLabel = new Label("Escribe algo");
		campoEscribir = new TextField(30);
		botonMostrar = new Button("Mostrar Texto");
		Button botonBorrar = new Button("Borrar todo");
		areaResultado = new Label("");

		add(nameLabel);
		add(campoEscribir);
		add(botonMostrar);
		add(botonBorrar);
		add(areaResultado);

		botonMostrar.addActionListener(this);
		botonBorrar.addActionListener(this);

		addWindowListener(new WindowAdapter(){
                        public void windowClosing(WindowEvent e) {
                                System.exit(0);
                        }
                });

		setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == botonMostrar) {
			String texto = campoEscribir.getText();
			areaResultado.setText(texto);
		} else {
			areaResultado.setText("");
			campoEscribir.setText("");
		}
	}

	public static void main(String[] args) {
		new ExWindow();
	}
}
