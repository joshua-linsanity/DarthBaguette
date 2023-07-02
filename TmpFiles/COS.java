// Euclidean Algorithm to find gcd of two numbers

public class COS {
    public static int max(int a, int b) {
        if (a > b) { return a; }
        return b;
    }

    public static int min(int a, int b) {
        if (a > b) { return b; }
        return a;
    }

    public static int gcd(int a, int b) {
        int m = max(a, b), n = min(a, b);

        if (m % n == 0) { return n; }

        return gcd(n, m % n);
    }

    public static void main(String[] args) {
        System.out.println(gcd(10, 15));
        System.out.println(gcd(35, 10));
        System.out.println(gcd(31, 2));
        System.out.println(gcd(2, 31));
        System.out.println(gcd(10, 10));
        System.out.println(gcd(13, 17));
    }
}

