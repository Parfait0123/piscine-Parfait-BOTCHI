import sympy as sp

# Nous definissons la variable z générale
z = sp.symbols('z')

# Definition du polynome de l'equation
a3 = 1
a2 = -(4- 11*sp.I)
a1 = -(22 + 30*sp.I)
a0 = 68 + 54*sp.I

# On conctruit le polynome
P = a3*z**3 + a2*z**2 +a1*z + a0
# L'équation revient à P = 0 (E)

print("="*60)
print(f"SECTION A : Resolution de l'équation")
print("="*60)

# 1. Verifions si z = 2+ i est solution de E
z_test = 2 + sp.I
resultat = sp.simplify(P.subs(z,z_test))
print(f"\n 1. z = 2 +i est-il solution de l'équation ? : {resultat == 0}")

# 2. Resolution de l'équation dans C avec sympy
solution = sp.solve(P,z)
print("2. Les 3 solution de l'équation dans C sont:")
for i, sol in enumerate(solution):
    print(f" z{i+1} = {sol} = {sp.simplify(sol)} ")

# Identifions zA, aB et zC avec im(aA)<Im(zB)<Im(aC)

sol_avec_im = [(sol, sp.im(sol)) for sol in solution]
sol_triees = sorted(sol_avec_im, key = lambda x:x[1], reverse=True)

zA = sol_triees[0][0]
zB = sol_triees[1][0]
zC = sol_triees[2][0]

print(f"""\n 3. Affixes ordonnées (Im(zC)<Im(zB)<Im(zA)) 
      zA = {zA} (Im = {sp.im(zA)})
      zB = {zB} (Im = {sp.im(zB)})
      zC = {zC} (Im = {sp.im(zC)})
      """)


print("="*60)
print(f"SECTION B : Geometrie dans le plan complexe")
print("="*60)

# 4. Calcul de lraffixe de D 
# zD = zC + (zC - zB) = 2*zC - zB
zD = 2*zC - zB
print(f"\n 4. Affixe de D : zD = {sp.simplify(zD)}")

#5. Distances AB, BC, AC
AB = sp.Abs(zB - zA)
BC = sp.Abs(zC - zB)
AC = sp.Abs(zC - zA)

print(f"""\n 5. Distances : 
      AB = | zB - zA | = {sp.simplify(AB) } 
      BC = | zC - zB | = {sp.simplify(BC) } 
      AC = | zC - zA | = {sp.simplify(AC) } 
""")

AB2 = sp.simplify(AB**2)
AC2 = sp.simplify(AC**2)
BC2 = sp.simplify(BC**2)

val_AB2 = complex(AB2)
val_BC2 = complex(BC2)
val_AC2 = complex(AC2)

tol = 1e-15
rectA = abs(val_AB2+val_AC2-val_BC2) < tol
rectB = abs(val_AB2 + val_BC2-val_AC2) < tol
rectC = abs(val_AC2+val_BC2-val_AB2) < tol
rectangle = rectA or rectB or rectC

est_rectangle = (sp.N(AB2 + BC2) == AC2) or (sp.N(BC2 + AC2) == AB2) or  (sp.N(AB2 + AC2) == BC2)
print(f"\n Le triangle ABC est rectangle ? : {rectangle} ")

# 6. Aire du Quadrilatere
A = complex(zA)
B = complex(zB)
C = complex(zC)
D = complex(zD)

def calcul_aire(z1,z2,z3):
    return 0.5*abs((z2 -z1).real *(z3 - z1).imag - (z2 -z1).imag * (z3 -z1).real)

aire_ABC = calcul_aire(A,B,C)
aire_ADC = calcul_aire(A,C,D)
aire_totale = aire_ABC + aire_ADC

print(f"\n Aire du quadrilatère ABCD : {aire_totale:.2f}")