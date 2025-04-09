import java.util.Base64;
import java.util.function.IntUnaryOperator;
import java.util.stream.Collectors;

public class JavaRev101 implements IntUnaryOperator {
    public static String fakeFlag = "jctf{red_flags_and_fake_flags_form_an_equivalence_class}";
    public static String reference = "K0c2QjkVcRd1eyFWcUArUDF7NRQwUCp7ckIdR3JRMFdxVz8=";

    private int cnt = 0;

    public static void main(String[] args) {
        new JavaRev101().run(args);
    }

    public void run(String[] args) {
        if(args.length != 1) {
            System.out.println("Usage: java JavaRev101 <flag>");
            return;
        }

        String userInput = args[0];
        String tmp = userInput.chars()
            .map(this)
            .mapToObj(c -> new Character((char)c).toString())
            .collect(Collectors.joining(""));
        String enc = Base64.getEncoder().encodeToString(tmp.getBytes());

        if(enc.equals(reference)) {
            System.out.println("You passed this course!");
        } else {
            System.out.println("It seems that you'll need to resit this class...");
        }
    }

    public int applyAsInt(int x) {
        return x ^ (cnt++ % 2 == 0 ? 0x42 : 0x24);
    }
}
