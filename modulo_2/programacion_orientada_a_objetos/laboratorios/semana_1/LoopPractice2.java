public class LoopPractice2 {
    public static void main(String[] args) {
        // LOOP 1:
        System.out.println("\nLoop 1:");
        int x = 9;
        int y = 7;
        for (int z = x + y; z > 1; z--) {
            System.out.println(z);
            if (z == 5)
                break;
            y = y + z;
        }
        System.out.println(y);

        // LOOP 2:
        System.out.println("\nLoop 2:");
        int a = 25;

        while (a < 50) {
            a++;
            if (a % 3 == 0)
                continue;
            System.out.println("Oh my!");
        }
        System.out.println(a);

        // LOOP 3:
        System.out.println("\nLoop 3:");
        int r = 5;

        do {
            r = r - 2;
            System.out.println("Hello");
        } while (r > -5);
        System.out.println(r);

        // LOOP 4:
        System.out.println("\nLoop 4:");
        int b = 12;
        while (b < 22) {
            System.out.println(b);
            b = b + 3;
        }
        System.out.println(b);

    }
}