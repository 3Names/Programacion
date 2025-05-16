package com.patricio.inventari;

public class Producte {
    private String nom;
    private double preu;
    private int cantidad;

    public Producte(String nom, double preu, int cantidad) {
        this.nom = nom;
        this.preu = preu;
        this.cantidad = cantidad;
    }

    public int getCantidad() {
        return this.cantidad;
    }

    public double getPreu() {
        return this.preu;
    }

    public String getNom() {
        return this.nom;
    }
}
