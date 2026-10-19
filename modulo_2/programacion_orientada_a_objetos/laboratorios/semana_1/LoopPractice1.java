public class LoopPractice1 {
    public static void main(String[] args) {
        // LOOP 1:
        System.out.println("\nLoop 1:");
        int c = 4;
        int d = 5;

        for (int p = c + d; p > 1; p--) {
            System.out.println(p);
            if (p == 5)
                break;
            d = d + p;
        }
        System.out.println(d);

        // LOOP 2:
        System.out.println("\nLoop 2:");
        int x = 15;

        while (x < 22) {
            x++;
            if (x % 2 == 0)
                continue;
            System.out.println("Bye!");
        }
        System.out.println(x);

        // LOOP 3:
        System.out.println("\nLoop 3:");
        int y = 3;
        do {
            y = y - 2;
            System.out.println("Hi Mom");
        } while (y > -3);
        System.out.println(y);

        // LOOP 4:
        System.out.println("\nLoop 4:");
        int a = 3;
        while (a < 10) {
            System.out.println(a);
            a = a + 3;
        }
        System.out.println(a);
    }
}
