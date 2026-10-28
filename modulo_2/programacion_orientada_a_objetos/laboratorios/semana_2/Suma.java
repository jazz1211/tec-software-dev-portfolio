import java.util.Scanner;

public class Suma {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1, num2;
        int suma;

        System.out.print("Ingresa el primer número: ");
        
        num1 = sc.nextInt();

        System.out.print("Ingresa el segundo número: ");
        num2 = sc.nextInt();

        suma = num1 + num2;

        System.out.println("La suma es: " + suma);
    }
}