package Semana3_JazminAlfaro;

import java.time.LocalDate;

public class Persona {

    // Zona de atributos:
    private int cedula;
    private String nombre;
    private LocalDate fechaNacimiento;
    private char lateralidad;
    private String direccionExacta;
    private double peso;

    // Metodo constructor por defecto: hasce espacio en memoria.
    public Persona() {
    }

    // Constructor sobrecargado:
    public Persona(int cedula, String nombre) {
        this.cedula = cedula;
        this.nombre = nombre;
    }

    // Zona de metodos get y set:
    public int getCedula() {
        return cedula;
    }

    public void setCedula(int cedula) {
        this.cedula = cedula;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public LocalDate getFechaNacimiento() {
        return fechaNacimiento;
    }

    public void setFechaNacimiento(LocalDate fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }

    public char getLateralidad() {
        return lateralidad;
    }

    public void setLateralidad(char lateralidad) {
        this.lateralidad = lateralidad;
    }

    public String getDireccionExacta() {
        return direccionExacta;
    }

    public void setDireccionExacta(String direccionExacta) {
        this.direccionExacta = direccionExacta;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    // Metodo toString: para mostrar los datos de la persona.
    @Override // Este override indica que estamos sobreescribiendo el metodo toString de la
              // clase Object.
    public String toString() {
        return "Persona [cedula=" + cedula + ", nombre=" + nombre
                + ", fechaNacimiento=" + fechaNacimiento
                + ", lateralidad=" + lateralidad
                + ", direccionExacta=" + direccionExacta
                + ", peso=" + peso + "]";
    }

    public boolean esZurdo() {
        return false;
    }

    public int determinarEdad() {
        return 0;
    }

    public boolean esMayorDeEdad() {
        return false;
    }

}