from Crypto.Util.number import bytes_to_long, long_to_bytes


def coppersmith(highbits, c, ring):
    _.<x> = ring[]
    i = 1
    while True:
        m = highbits << (19 * 8)
        p = (m + x)^3 - c
        roots = p.small_roots()

        if len(roots) != 0:
            return roots[0]

        i += 1

# the following 3 methods have been shamelessly stole... borrowed from https://github.com/pwang00/Cryptographic-Attacks/blob/master/Public%20Key/RSA/coppersmith_short_pad.sage
def coppersmith_short_pad(C1, C2, N, e = 3, eps = 1/25):
    P.<x, y> = PolynomialRing(Zmod(N))
    P2.<y> = PolynomialRing(Zmod(N))

    g1 = (x^e - C1).change_ring(P2)
    g2 = ((x + y)^e - C2).change_ring(P2)
 
    # Changes the base ring to Z_N[y] and finds resultant of g1 and g2 in x
    res = g1.resultant(g2, variable=x)

    # coppersmith's small_roots only works over univariate polynomial rings, so we 
    # convert the resulting polynomial to its univariate form and take the coefficients modulo N
    # Then we can call the sage's small_roots function and obtain the delta between m_1 and m_2.
    # Play around with these parameters: (epsilon, beta, X)
    roots = res.univariate_polynomial().change_ring(Zmod(N))\
        .small_roots(epsilon=eps)

    return roots[0]


def franklin_reiter(C1, C2, N, r, e=3):
    P.<x> = PolynomialRing(Zmod(N))
    equations = [x ^ e - C1, (x + r) ^ e - C2]
    g1, g2 = equations
    return -composite_gcd(g1,g2).coefficients()[0]


def composite_gcd(g1,g2):
    return g1.monic() if g2 == 0 else composite_gcd(g2, g1 % g2)


n = 0x6ac86e4b12354dc1210f11526c58c7fe989b72d2a68bd0081e63dab322c2905dbaee70086570c23d37ebc7cb95c43c3c52c7e9b6d9e83a2a0c4f6fb5189933d7c8c61ce3aa5c19aad6f2fc089770c97efed7b2d3891f44870ef9461994beb8a1e4a41163cc15ed7e5992dbb047996cd3a837df5635b7cbe530348853e6dd8a4fd7bb80f8f2c260c1166440382b9ac23ddea574c8b6fd671e54c5a8210ac29372d6dbc5f3e0fd2ae4e8eb3eadc140081b3dbeb964d240e511a2237a8251a59829e04eed326eb535214ad740c25869fd898d6124a9fbe2bc635e77e3fa85f2688ea33541a3f1f80ad5977b6cc4b143e738ebc8c33e5f573dbb79589aa76bb216a7
c1 = 0x1ebedcb80e40dc9069eac645d45a43304831dc582be471c340c04cf26ea72472e8f1ca6024176b7ba90d11e51f2219df1def5120625e139a67f2ef3db838e508d745b8c6b79d6ea5a58baaae03aa178f1883531f28681bf6ed67cf61e4c9fdad8353d003d39b08423386e49316484d37cbb1e6c31110fef05720a1022ab7b77b962971d87acdea1382655b1968e5983f40bd4f9649507af7b9a5989b73e68265d3cd2ba26044e51a03de5c11f15fd78749eb90b2f94e80086f276fc8291e105095d6a1572416092875768550573746619aafa9323f7e5c74a9269f571db048bd6c0ba86a3452c8539893abe8d4e98f9f4ed1cac12db9f6161d6b9269176ebc9a
c2 = 0x35fbd515f0d9a2778ccc3d009ffe7773c7c58843cfb3d62dd26a1ef3d4f22808b536f63f15f9219ddbbef7cb28dee0151aa873411d0641bd5787cdea5428922325eb28fdaea21290f260966c1866a90b878f53b5eebebd863603693b1e45127717d811ccb31326e81ae5ae875882d93979db71d573920978f001321c6356a322abf0fef92a77e0a26e98839d9f66f870281c3b2673aa24eee36cce561ed43427b8cc47a147dfb893722d03c95f220b71e57a02b6a8ef925de649f0c5a712873e6c36588461d0e33d761102c2c0e6271fb773d456d2b7f89ae93ef3f58e62f4b768059f8c4780a55f767f458cebf03961bca27069b6c97b83fe0d89a47b713c21
c3 = 0x518ff20dcbad2aebd4576557ce1f79d78c4b503d0b2b8ca9af293863ed6174be1385f57120939d88587d3e0b4bbb29b40a0161a2c29517c4c445ce15b38d51234de67a4bdf170b88aed91cb923fb5317593c5cd07b0a19f5ceb4b7eb5d95b58321d05bb17857157469ac21b312ae4284a2ea2f101f09132f39e63ad3048acf6302ed01a13cef45d1e0932c547f654cd4037075a81952490c7cecb9a1cd6bc32a8f351b80cd358b3557c17f4956ede318f53a804899ad96b9146dd864b922f74eeed0cbc99fdb1177ac57378396b46cd8cd7c0cfdd8f25f472a00c6e29ccbe8979acd806a655adb7e76b863cad088b09c2351cb66b69493379513d41e30f2f6a2
c4 = 0x556d6848099ce066a01fdaa096a1e530ce8ef8d576abd5deabb4167b9f6953af05c6f8f8336a766a57668e174d7955ad1b964e64e26d8f0ef9ad8cb42f773c8651cb77abebc397379b6eb230c36797d6c9ea75a6a1e6c0cd3e3b293c35c2b82179ef2f0714667d015cb30bc3a8a8880df9e60e1ea4029a8bd246b0b01a8a7dcaf7d7c8cbf6058df43226c4b73107ac074a39ebfc0870546da31b5619fac66ef19a497ab57fd21cd1f52fd17d117ee996880c1cac34562dfa832070b3781168ef37e9389b47c77719edf34d101bc3782edb195fe047bd03c113eca3d67f44fc8037fb7419f563e194883928746d3c1f2ef4e7337f7653b88188a5bad491e836ca

m1 = bytes_to_long(b'How can you tell a difference between a good cryptography joke and a random string of words? ')
m2 = bytes_to_long(b'You can\'t. They\'re indistinguishable! Hahahahahahahahahahahahahahahahahahahahahahahahahaha! ')

K = Zmod(n)

f1 = long_to_bytes(int(coppersmith(m1, c1, K)))
f2 = long_to_bytes(int(coppersmith(m2, c2, K)))

r = coppersmith_short_pad(c3, c4, n)
f3 = long_to_bytes(int(franklin_reiter(c3, c4, n, r)))[128:-16]

print((f1 + f2 + f3).decode())
