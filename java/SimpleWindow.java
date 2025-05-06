import java.awt.*;
import java.awt.event.*;

public class SimpleWindow extends Frame implements ActionListener{
	private TextField nameField;
	private Label resultLabel;
	
	public SimpleWindow() {
		setTitle("");
		setSize(400,300);
		setLocationRelativeTo(null);
		
		setLayout(new GridLayout(1,2));

		Label nameLabel = new Label("What's your name?");
		nameField = new TextField(20);
		Button greetButton = new Button("Greet");
		resultLabel = new Label("");
		Checkboc checkboc = new Checkbox("Check me")
		Choice choice = new Choice();
		choice.add("1");
		choice.add("2");
		choice.add("3");
		TextArea textarea = new TextArea(5,20);

		add(nameLabel);
		add(nameField);
		add(greetButton);
		add(resultLabel);

		greetButton.addActionListener(this);
		
		addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});

		setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		String name = nameField.getText();
		resultLabel.setText("Hello " + name);
	}

	public static void main(String[] args) {
		new SimpleWindow();
	}
}
