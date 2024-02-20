import math

def beregn_vinkler(sidelængde_a, sidelængde_b, sidelængde_c):
    # Beregn vinklerne i trekanten ved hjælp af cosinusrelationen
    vinkel_A = math.degrees(math.acos((sidelængde_b**2 + sidelængde_c**2 - sidelængde_a**2) / (2 * sidelængde_b * sidelængde_c)))
    vinkel_B = math.degrees(math.acos((sidelængde_c**2 + sidelængde_a**2 - sidelængde_b**2) / (2 * sidelængde_c * sidelængde_a)))
    vinkel_C = 180 - vinkel_A - vinkel_B


print("Velkommen til trekantsberegneren")

    # Udskriv resultaterne
    print(f"Sidelængde a: {sidelængde_a}")
    print(f"Sidelængde b: {sidelængde_b}")
    print(f"Sidelængde c: {sidelængde_c}")
    print(f"Vinkel A: {vinkel_A}")
    print(f"Vinkel B: {vinkel_B}")
    print(f"Vinkel C: {vinkel_C}")

# Indtast sidelængderne a, b, c
a = float(input("Indtast sidelængde a: "))
b = float(input("Indtast sidelængde b: "))
c = float(input("Indtast sidelængde c: "))

# Beregn og udskriv vinkler
beregn_vinkler(a, b, c)
