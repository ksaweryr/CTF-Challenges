public class Minified {
    public static void main(String[] args) {
        if(args.length != 1) {
            System.out.println("Please supply the flag");
            return;
        }
        
        String flag = args[0];
        System.out.println(verify(flag.getBytes()));
    }

    private static boolean verify(byte[] chars) {
        if(chars.length != 18 || chars[0] != 'i' || chars[1] != 'c' || chars[2] != 't' || chars[3] != 'f' || chars[4] != '{' || chars[17] != '}' || -21*chars[5] + 1*chars[6] + 1*chars[7] + 1*chars[8] + 1*chars[9] + 1*chars[11] + -2*chars[12] + -8*chars[13] + -3*chars[14] + -1*chars[15] + -1*chars[16] != -3048 || 2*chars[5] + -1*chars[6] + -1*chars[9] + 4*chars[10] + 2*chars[11] + 5*chars[12] + 1*chars[13] + 1*chars[14] + 1*chars[15] + -2*chars[16] != 1283 || 1*chars[5] + 7*chars[6] + 2*chars[7] + -1*chars[8] + -1*chars[9] + 1*chars[11] + -1*chars[14] + -3*chars[15] != 592 || 2*chars[5] + -1*chars[6] + -1*chars[8] + 1*chars[9] + -151*chars[10] + -1*chars[11] + 1*chars[12] + -3*chars[14] + 2*chars[15] + 20*chars[16] != -15721 || -1*chars[5] + -1*chars[6] + -21*chars[7] + 2*chars[8] + -4*chars[10] + -2*chars[11] + -3*chars[13] + -6*chars[14] + 3*chars[16] != -3620 || -1*chars[6] + 1*chars[7] + -1*chars[8] + -98*chars[9] + -1*chars[10] + -1*chars[11] + -4*chars[12] + 1*chars[13] + 1*chars[15] + -4*chars[16] != -10482 || 3*chars[5] + 4*chars[7] + -14*chars[8] + 1*chars[9] + 27*chars[10] + 2*chars[11] + 1*chars[12] + -7*chars[13] + 1*chars[14] + -1*chars[15] + -3*chars[16] != 1927 || -1*chars[5] + -1*chars[7] + -4*chars[8] + -95*chars[9] + 1*chars[10] + -47*chars[11] + -1*chars[12] + 8*chars[13] + 3*chars[14] + -1*chars[15] + -1*chars[16] != -14402 || 1*chars[5] + 1*chars[6] + -4*chars[7] + 3*chars[8] + -1*chars[9] + -3*chars[10] + -1*chars[11] + 8*chars[14] + -1*chars[16] != 175 || -1*chars[5] + 4*chars[8] + -1*chars[10] + -1*chars[12] + 2*chars[13] + -3*chars[14] + 1*chars[15] + -22*chars[16] != -2024 || -1*chars[5] + -7*chars[6] + 1*chars[7] + -2*chars[8] + 9*chars[9] + 1*chars[10] + 20*chars[11] + 1*chars[12] + -4*chars[13] + -1*chars[14] + -1*chars[15] + -6*chars[16] != 1210 || 2*chars[5] + 3*chars[6] + 1*chars[7] + 1*chars[8] + 2*chars[9] + -1*chars[10] + -1*chars[11] + 5*chars[12] + 1*chars[13] + 11*chars[14] + -5*chars[15] + 1*chars[16] != 1861) {
            return false;
        }

        return true;
    }
}
