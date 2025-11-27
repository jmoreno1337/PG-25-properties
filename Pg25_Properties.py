import csv
import pandas as pd
from CoolProp.CoolProp import PropsSI

FLUID = "INCOMP::MPG[0.25]"   # PG-25
P = 101325                    # Pa, 1 atm
T_C_list = range(-5, 105, 5)

rows = []
for T_C in T_C_list:
    T_K = T_C + 273.15
    rho = PropsSI("D", "T", T_K, "P", P, FLUID)
    mu  = PropsSI("V", "T", T_K, "P", P, FLUID)
    cp  = PropsSI("C", "T", T_K, "P", P, FLUID)
    k   = PropsSI("L", "T", T_K, "P", P, FLUID)
    h   = PropsSI("H", "T", T_K, "P", P, FLUID)
    rows.append([T_C, rho, mu, cp, k, h])

# Save CSV (good for everything)
csv_name = "PG25_props.csv"
with open(csv_name, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T_C", "rho_kgm3", "mu_Pas", "cp_JkgK", "k_WmK", "h_Jkg"])
    writer.writerows(rows)

# Also save as Excel
xlsx_name = "PG25_props.xlsx"
df = pd.DataFrame(rows, columns=["T_C", "rho_kgm3", "mu_Pas", "cp_JkgK", "k_WmK", "h_Jkg"])
df.to_excel(xlsx_name, index=False)

print("Wrote", csv_name, "and", xlsx_name)
