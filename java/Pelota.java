import javax.swing.*;
import java.awt.*;

public class Pelota extends JFrame {
    private Canva canva;
    private final int posicion = 10;

    public Pelota() {
        super("Pelota");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 350);
        setLayout(new BorderLayout());

        canva = new Canva();
        canva.setBackground(Color.CYAN);
        add(canva, BorderLayout.CENTER);

        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();
        
        JButton arriba = new JButton("UP");
        JButton abajo = new JButton("DOWN");
        JButton izquierda = new JButton("LEFT");
        JButton derecha = new JButton("RIGHT");

        arriba.addActionListener(e -> canva.moverPelota(0, -posicion));
        abajo.addActionListener(e -> canva.moverPelota(0, posicion));
        izquierda.addActionListener(e -> canva.moverPelota(-posicion, 0));
        derecha.addActionListener(e -> canva.moverPelota(posicion, 0));

        c.gridx = 1;
        c.gridy = 0;
        panel.add(arriba, c);

        c.gridx = 0;
        c.gridy = 1;
        panel.add(izquierda, c);

        c.gridx = 2;
        c.gridy = 1;
        panel.add(derecha, c);

        c.gridx = 1;
        c.gridy = 2;
        panel.add(abajo, c);

        add(panel, BorderLayout.SOUTH);
    }

    class Canva extends JPanel {
        private int x = 180;
        private int y = 100;
        private final int Diametro = 30;

        public void moverPelota(int xd, int yd) {
            x += xd;
            y += yd;
            repaint();
        }

        @Override

        public void paintComponent(Graphics g) {
            super.paintComponent(g);
            g.setColor(Color.RED);
            g.fillOval(x, y, Diametro, Diametro);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Pelota ventana = new Pelota();
            ventana.setVisible(true);
        });
    }
}