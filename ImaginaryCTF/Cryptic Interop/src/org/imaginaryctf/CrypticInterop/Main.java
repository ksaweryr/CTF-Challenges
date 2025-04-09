package org.imaginaryctf.CrypticInterop;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Function;
import java.util.stream.Stream;

public class Main implements Function<Byte, Integer> {
    int s = 4629;

    public static void main(String[] args) throws IOException, URISyntaxException {
        new Main().run(args);
    }

    public void run(String[] args) throws IOException {
        if(args.length == 0) {
            System.out.println(false);
        } else {
            InputStream s = getClass().getClassLoader().getResourceAsStream("libinterop.so.enc");
            byte[] bytes = s.readAllBytes();
            AtomicInteger cnt = new AtomicInteger(0);
            List<Integer> bs = Stream.generate(() -> bytes[cnt.getAndIncrement()])
                .limit(bytes.length)
                .map(this)
                .toList();
            byte[] decoded = new byte[bytes.length];
            for(int i = 0; i < decoded.length; i++) {
                decoded[i] = bs.get(i).byteValue();
            }
            Path dest = Path.of("/tmp/libinterop.so");
            Files.copy(new ByteArrayInputStream(decoded), dest, StandardCopyOption.REPLACE_EXISTING);
            System.load(dest.toString());
            Files.delete(dest);
            System.out.println(verify(args[0]));
        }
    }

    private native boolean verify(String flag);

    @Override
    public Integer apply(Byte t) {
        this.s = (75 * s + 74) % 65537;
        int x = (s & 0xf) | ((s >> 4) & 0xf0);
        return t.intValue() ^ x;
    }
}