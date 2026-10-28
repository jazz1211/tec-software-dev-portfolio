import java.util.Scanner;

public class Cuadrado {
    public static int numero;

    public static int calcularCuadrado() {
        return numero * numero;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingresa un número: ");
        numero = sc.nextInt();

        int resultado = calcularCuadrado();
        System.out.println("El cuadrado es: " + resultado);
    }
}