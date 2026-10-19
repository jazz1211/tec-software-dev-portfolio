public class LoopPractrice3 {
    public static void main(String[] args) {
        // LOOP 1:
        System.out.println("\nCODIGO CORREGIDO DE LOS ERRORES DE SINTAXIS:\nLoop 1:");
        for (int count = 2; count <= 12; count++)
            System.out.print(count + " ");

        // LOOP 2:
        System.out.println("\n\nLoop 2:");
        int sum = 0;
        for (int count = 0; count <= 10; count++) { //El error se encontraba en la falta de parentesis y la variable i no estaba declarada, se cambio por count y se arreglo la sintaxis del for
            System.out.println(count + " ");
            sum += count;
        }
        System.out.println("La suma de 0 a 10 es: " + sum);

        // LOOP 3:
        System.out.println("\nLoop 3:");
        for (int count = 20; count >= 10; count--)
            System.out.println(count + " ");
        // El Loop funciona correctamente, pero el bucle imprime desde de 20 a 10
        // y no de 10 a 20 como se esperaba

        // LOOP 4:
        System.out.println("\nLoop 4:"); 
        for (int x = 0; x < 15; x++) //Encabezado del loop for que imprime los numeros del 0 con 15 iteraciones
            System.out.println(x + " ");

        // Loop 5:
        System.out.println("\nLoop 5:"); 
        for (int y = 10; y > 5; y--) //Encabezado del loop for que imprime los numeros del 10 con 5 iteraciones DE 1 EN 1
            System.out.println(y + " ");

    }

}