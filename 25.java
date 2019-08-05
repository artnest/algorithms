import java.io.*;

public class WagnerFischer {
    public static void main(String[] args) throws IOException {
        int p;

        try (BufferedReader reader = new BufferedReader(new FileReader("in.txt"))) {

            int del_cost = Integer.parseInt(reader.readLine());
            int ins_cost = Integer.parseInt(reader.readLine());
            int sub_cost = Integer.parseInt(reader.readLine());

            String str1 = reader.readLine();
            String str2 = reader.readLine();

            p = getWagnerFischer(str1, str2, del_cost, ins_cost, sub_cost);
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("out.txt"))) {
            writer.write(String.valueOf(p));
        }
    }

    private static int getWagnerFischer(String s1, String s2, int deletion, int insertion, int substitution) {
        int len_s1 = s1.length();
        int len_s2 = s2.length();

        int[][] d = new int[len_s1 + 1][len_s2 + 1];

        for (int i = 1; i < len_s1 + 1; i++) {
            d[i][0] = i * deletion;
        }

        for (int j = 1; j < len_s2 + 1; j++) {
            d[0][j] = j * insertion;
        }

        for (int i = 1; i < len_s1 + 1; i++) {
            for (int j = 1; j < len_s2 + 1; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    d[i][j] = d[i - 1][j - 1];
                } else {
                    d[i][j] = Math.min(d[i - 1][j] + deletion,
                              Math.min(d[i][j - 1] + insertion,
                                       d[i - 1][j - 1] + substitution));
                }
            }
        }

        return d[len_s1][len_s2];
    }
}
