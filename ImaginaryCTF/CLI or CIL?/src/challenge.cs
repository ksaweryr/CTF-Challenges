using System;
using System.Linq;

// ictf{C#_r3v3R51ng_cH411}
namespace Challenge {
    public static class Program {
        public static void Main(string[] args) {
            if(args.Length != 1) {
                Console.WriteLine($"Usage: ./challenge.exe <flag>");
                return;
            }

            string input = args[0];

            if(input.Length != 24) {
                Console.WriteLine("Nope.");
                return;
            }

            // char[] reference = {};
            string reference = "f1Hr31tR_C31cv4#n}i{g_5c";
            char[] scrambled = new char[24];
            int x = 7312;

            for(int i = 0; i < 24; i++) {
                x = (69 * x + 42) % 24;
                while(scrambled[x] != 0) {
                    x = (x + 1) % 24;
                }
                scrambled[x] = input[i];
            }

            if(Enumerable.SequenceEqual(reference, scrambled)) {
                Console.WriteLine("Yup.");
            } else {
                Console.WriteLine("Nope.");
            }
        }
    }
}
