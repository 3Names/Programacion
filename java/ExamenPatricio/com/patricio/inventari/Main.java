package com.patricio.inventari;

import java.util.*;
import java.io.*;
import com.patricio.inventari.Producte;

public class Main {
    private List<Producte> lista_productos = new ArrayList<>();
    private final int baix_stock = 10;

    public void leerInventario() {
        String nom = "";
        double preu = 0.00;
        int cantidad = 0;
        try (FileReader fr = new FileReader("com/patricio/inventari/inventari.txt")) {
            BufferedReader br = new BufferedReader(fr);
            String linea;
            while((linea = br.readLine()) != null) {
                String[] partes = linea.split(",");
                if (partes.length == 3) {
                    try {
                            nom = partes[0];
                            preu = Double.parseDouble(partes[1]);
                            cantidad = Integer.parseInt(partes[2]);
                            Producte nuevo = new Producte(nom, preu, cantidad);
                            lista_productos.add(nuevo);
                    }
                    catch(Exception e) {
                        System.err.println("ERROR: Formato erroneo");
                    }
                } else {
                    System.err.println("ERROR: Linea con formato invalido");
                }
            }
        }
        catch(Exception e) {
            System.err.println(e);
        }
    }

    public void generarInformeLowStock() {
        try (FileWriter fichero = new FileWriter("com/patricio/inventari/stock_baix.txt")) {
            PrintWriter pw = new PrintWriter(fichero);
            for(Producte producto: lista_productos) {
                if(producto.getCantidad() < baix_stock) {
                    pw.println(producto.getNom() +" (" + producto.getCantidad() + ")");
                }
            }
        } catch (Exception e) {
            System.err.println(e);
        }
    }

    public void calcularTotalInventari() {
        try {
            double total = 0;
            for (Producte producto: lista_productos) {
                total += producto.getCantidad() * producto.getPreu();
            }
            System.out.println("Valor total de l'inventari: " + total + " €");

        } catch (Exception e) {
            System.err.println(e);
        }
    }


    public static void main(String[] args) {
        Main productos = new Main();
        productos.leerInventario();
        productos.generarInformeLowStock();
        productos.calcularTotalInventari();
    }
}