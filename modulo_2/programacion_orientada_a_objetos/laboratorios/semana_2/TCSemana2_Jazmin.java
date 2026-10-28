import java.util.Scanner;

public class TCSemana2_Jazmin {
    // Ejercicio 1: convierte de Fahrenheit a Celsius
    public static double fahToCel(double fahrenheit) {
        return (fahrenheit - 32) * 5.0 / 9.0;
    }
    // Ejercicio 2: calcula la hipotenusa de un triángulo rectángulo
    public static double hipotenusa(double ladoA, double ladoB) {
        return Math.sqrt(ladoA * ladoA + ladoB * ladoB);
    }

    // Ejercicio 3: suma el resultado de lanzar dos dados
    public static int lanzarDados() {
        int dado1 = (int) (Math.random() * 6) + 1;
        int dado2 = (int) (Math.random() * 6) + 1;
        return dado1 + dado2;
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("* EJERCICIO 1:");
        System.out.print("- Temperatura en Fahrenheit: ");
        double fahrenheit = entrada.nextDouble();
        System.out.println("- Temperatura en Celsius: "
                + fahToCel(fahrenheit));

        System.out.println("\n* EJERCICIO 2:");
        System.out.print("- Longitud del lado A: ");
        double ladoA = entrada.nextDouble();
        System.out.print("- Longitud del lado B: ");
        double ladoB = entrada.nextDouble();
        System.out.println("- Longitud de la hipotenusa: "
                + hipotenusa(ladoA, ladoB));

        System.out.println("\n* EJERCICIO 3:");
        System.out.println("- La suma de los valores de los dados es "
                + lanzarDados());

        entrada.close();
    }
}
