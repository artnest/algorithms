import java.io.*;
import java.util.Scanner;

public class Tree {
    private static int m = 0;
    private static int adj[][];
    private static boolean used[];

    private static void dfs(int v) {
        used[v] = true;
        m++;
        for (int i = 0; i < adj.length; i++) {
            if (adj[v][i] == 1 && !used[i]) {
                dfs(i);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(new FileReader("input.txt"));

        int n = scanner.nextInt();
        adj = new int[n][n];
        used = new boolean[n];

        int edges = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                adj[i][j] = scanner.nextInt();
                edges += adj[i][j];
            }
        }
        scanner.close();

        dfs(0);
        edges /= 2;

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"))) {
            if (edges == n - 1 && m == n) {
                writer.write("Yes");
            } else {
                writer.write("No");
            }
        }
    }
}