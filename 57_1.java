import java.io.*;
import java.util.LinkedHashMap;
import java.util.Map;

public class Hashtable {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));

        String[] parameters = reader.readLine().split(" ");
        int m = Integer.parseInt(parameters[0]);
        int c = Integer.parseInt(parameters[1]);

        Map<Integer, Integer> hashtable = new LinkedHashMap<>();
        for (int i = 0; i < m; i++) {
            hashtable.put(i, -1);
        }

        String line;
        while ((line = reader.readLine()) != null) {
            int x = Integer.parseInt(line);
            if (!hashtable.containsValue(x)) {
                int i = 0;
                int idx = (x % m + c * i) % m;
                while (hashtable.get(idx) != -1) {
                    i++;
                    idx = (x % m + c * i) % m;
                }
                hashtable.put(idx, x);
            }
        }
        reader.close();

        Writer writer = new FileWriter("output.txt");
        hashtable.values().forEach(v -> {
            try {
                writer.write(v.toString() + " ");
            } catch (IOException e) {
                System.err.println(e.getMessage());
            }
        });
        writer.close();
    }
}
