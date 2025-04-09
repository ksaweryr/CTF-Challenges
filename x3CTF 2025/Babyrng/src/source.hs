{-# LANGUAGE ScopedTypeVariables #-}
import Control.Monad.State.Lazy (evalState, State, state)
import Data.Bits (xor)
import Data.Char (chr, ord)
import Data.Word (Word64)
import System.Random (getStdGen, StdGen, uniform, uniformR)
import Text.Printf (printf)

flag = "MVM{4_M0n4D_15_jU5t_4_m0N01d_1n_Th3_c4t3G0Ry_0f_3ND0FUNCT0R5_:D}"

shred :: String -> State StdGen String
shred "" = return ""
shred (c:cs) = do
    k <- state $ uniformR (0, 255)
    ((:) (chr $ (ord c) `xor` k)) <$> (shred cs)

burryTreasure :: State StdGen String
burryTreasure = do
    shredded <- shred flag
    x :: Word64 <- state uniform
    y :: Word64 <- state uniform
    return $ printf "The shredded flag (%s) has been burried at (%d, %d)" (shredded >>= (printf "%02x" :: Char -> String)) x y

main :: IO ()
main = do
    rng <- getStdGen
    putStrLn $ evalState burryTreasure rng