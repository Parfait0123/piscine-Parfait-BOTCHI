from scipy.stats import hypergeom
from math import comb

print("="*60)
print("Problème 2")
print("="*60)

N = 200
K = 120
n = 3

loi = hypergeom(N,K,n)
print(f"Paramètres de départ : N = {N}, K = {K} et n = {n}")

#1. Calcul de probabilité
p_tous_3 = loi.pmf(3)
print(f"\n 1. P(X = 3) = {p_tous_3:.4f}")

#2. Probabilité d'avoir exactement 1 certifé
p_1_sans_emploi = comb(30,1)*comb(170,2)/comb(200,3)
print(f"\n 2. P (exactement 1 n'a pas trouvé d'emploi) = {p_1_sans_emploi:.4f}")

#3 Espérance et variance
E_X = loi.mean()
V_X = loi.var()
print(f"\n 3. Expérance = {E_X} \n Variance = {V_X}")

#4. P(X >= 2)
print("\n 4. P(X >= 2)")
p_x_sup2 = loi.sf(1)
print(f"\n P(X>=2) = {p_x_sup2:.4f}")

print("="*60)
print("FIN")
print("="*60)