package Semana3_JazminAlfaro;

import java.time.LocalDate;

public class PruebaPersona {

    public static void main(String[] args) {
        // Constructor por defecto
        Persona persona1 = new Persona();

        // Metodos set
        persona1.setCedula(123456789);
        persona1.setNombre("Jazmin Alfaro");
        persona1.setFechaNacimiento(LocalDate.of(1900, 1, 15));
        persona1.setLateralidad('D');
        persona1.setDireccionExacta("San Jose");
        persona1.setPeso(62.5);

        // Metodos get
        System.out.println("- Nombre: " + persona1.getNombre());
        System.out.println("- Cedula: " + persona1.getCedula());
        System.out.println("- Fecha de nacimiento: " + persona1.getFechaNacimiento());
        System.out.println("- Lateralidad: " + persona1.getLateralidad());
        System.out.println("- Direccion: " + persona1.getDireccionExacta());
        System.out.println("- Peso: " + persona1.getPeso());

        // Constructor sobrecargado
        Persona persona2 = new Persona(456, "Lola");
        persona2.setFechaNacimiento(LocalDate.of(2010, 8, 20));
        persona2.setLateralidad('D');
        persona2.setDireccionExacta("Heredia");
        persona2.setPeso(55.0);

        // Metodo toString
        System.out.println("\nPrimera persona: " + persona1.toString());
        System.out.println("\nSegunda persona: " + persona2.toString());

        // Llamadas a los metodos
        System.out.println("\nPrimera persona:");
        System.out.println("- Es zurdo: " + persona1.esZurdo());
        System.out.println("- Edad: " + persona1.determinarEdad());
        System.out.println("- Es mayor de edad: " + persona1.esMayorDeEdad());

        System.out.println("\nSegunda persona:");
        System.out.println("- Es zurdo: " + persona2.esZurdo());
        System.out.println("- Edad: " + persona2.determinarEdad());
        System.out.println("- Es mayor de edad: " + persona2.esMayorDeEdad());
    }
}
