import random

# --- Počiatočné premenné ---
N = 1       # Počet kaviarní/pobočiek
C = 6.0     # Cena kávy
M = 400     # Maximálny dopyt/potenciálni zákazníci
a = 80      # Faktor kvality (ako citlivá je káva na nízku kvalitu)
V = 4       # Variabilné náklady na kávu (Cost of Goods Sold - COGS)
q = 70      # Mzda/Plat zamestnancov (indikátor spokojnosti)
Z = 1       # Počet zamestnancov
rent = 50   # Náklady na prenájom jednej pobočky
Ml = 1000   # Príjmy z predaja (budú prepočítané)
moneyz = 500 # Aktuálna hotovosť
D = 1       # Deň

# Nastavenie minimálnych limitov pre logiku hry
MIN_EMPLOYEES = 1
MIN_V_COST = 1
MIN_A_FACTOR = 10 

running = True

def calculate_daily_profit(N, C, M, a, V, q, Z, rent):
    """
    Vypočíta denný zisk na základe aktuálnych premenných.
    P = I * N * (C * (M - a*C) - V * (M - a*C) - q*Z - rent)
    """
    
    # 1. Príjmy a náklady: Mzdy a nájom sa škálujú podľa počtu pobočiek (N).
    # Nastavíme dynamickú variabilitu v dopyte (I)
    I = random.uniform(0.8, 1.2)

    # 2. Faktor spokojnosti/dopytu na základe platu (q)
    # Toto určuje, aký je celkový potenciál predaja/zárobku (Ml)
    Ml = 1000 + Z * 500 # Základné príjmy + príjmy zo zamestnancov
    
    if q > 100:
        Ml *= 1.2
    elif q > 80:
        Ml *= 1.1
    elif q < 60 and q >= 50:
        Ml *= 0.9
    elif q < 50 and q >= 40:
        Ml *= 0.8
    elif q < 40:
        Ml = 0 # Príliš nízka mzda, zamestnanci prestanú pracovať (nulový predaj)

    # 3. Prepočet dopytu (Sales)
    # Dopyt klesá s rastúcou cenou (C) a faktorom kvality (a). 
    # Max predaj (M) znížený o (a * C). Musí byť kladné.
    base_demand = M - a * C
    
    # Prevencia záporného dopytu v rámci zátvoriek (Sales Factor)
    if base_demand <= 0:
        sales = 0
    else:
        # Váš pôvodný vzorec, kde (M - a*C) predstavuje dopyt (sales quantity)
        sales_quantity = base_demand * N * I
        
        # Zisk = (Cena - Variabilné náklady) * Množstvo - Fixné náklady
        # Váš pôvodný vzorec: P = I*N*(C*(M-a*C) - V*(M-a*C) - q*Z - rent)
        # Preusporiadané: P = I*N*((C - V) * Demand) - (q*Z*N) - (rent*N)
        
        # Demand Factor: (M - a*C)
        demand_factor = (M - a * C) 
        
        # Príjmy: I * N * C * demand_factor
        revenue = I * N * C * demand_factor
        
        # Variabilné náklady: I * N * V * demand_factor
        variable_costs = I * N * V * demand_factor
        
        # Fixné náklady: mzdy a nájom
        fixed_costs = (q * Z * N) + (rent * N)
        
        P = revenue - variable_costs - fixed_costs

    # Ak je Ml 0, zisk (Profit P) by mal byť len strata fixných nákladov, ale pre 
    # zjednodušenie ponechávame zisk P podľa pôvodného vzorca, kde Ml nebol 
    # priamo použitý, ale mal len vplyv na dopyt/potenciál. Pre túto simuláciu
    # použijeme priamo P. Ak Ml=0 (kvôli nízkej mzde), predpokladajme P = -FixedCosts.
    if Ml == 0:
        P = -(q * Z * N + rent * N)

    return P, Ml

while moneyz > -100 and running:
    # 1. Výpočet zisku pre aktuálny deň
    P, Ml_status = calculate_daily_profit(N, C, M, a, V, q, Z, rent)
    moneyz = moneyz + P
    
    print("\n" + "="*40)
    print(f"DEŇ: {D}")
    print("="*40)
    print(f"Dnes dopyt (predpokladaný) bol ovplyvnený faktorom: {Ml_status:.0f}")
    print(f"Dnešný zisk (P): {P:,.2f} €")
    print(f"Uložené/Kasa (Moneyz): {moneyz:,.2f} €")
    print(f"Pobočky (N): {N} | Zamestnanci (Z): {Z} | Cena kávy (C): {C} €")

    # 2. Vstup užívateľa pre zmeny
    go = False
    while go == False:
        print("\nMožné akcie: Ad campaign, coffee quality+, coffee quality-, recruitment, fire somebody, salary, set price, expand, make it fancy, ok, exit")
        action = input("Akékoľvek zmeny? (zadaj príkaz): ").strip().lower()

        # --- Validácia akcie a nemožných hodnôt ---
        
        if action == "ad campaign":
            COST = 100
            if moneyz >= COST:
                moneyz -= COST
                M += 50
                print(f"| Úspech: Zvýšený potenciálny dopyt. Zostatok: {moneyz:,.2f} €")
            else:
                print(f"| CHYBA: Na reklamnú kampaň potrebujete {COST} €. Máte len {moneyz:,.2f} €.")
                
        elif action == "coffee quality+":
            # Zníženie faktora 'a' zlepšuje dopyt pri vyššej cene
            a = max(MIN_A_FACTOR, a - 15)
            V += 1
            print(f"| Úspech: Zvýšená kvalita kávy. Nový faktor kvality (a): {a}")
            
        elif action == "coffee quality-":
            # Zvýšenie faktora 'a' znižuje dopyt (zhoršuje kvalitu)
            if V > MIN_V_COST:
                a += 15
                V -= 1
                print(f"| Úspech: Znížená kvalita kávy. Nový variabilný náklad (V): {V}")
            else:
                print(f"| CHYBA: Variabilné náklady (V) už nemôžu klesnúť pod {MIN_V_COST}.")
            
        elif action == "recruitment":
            # Nábor stojí menej peňazí ako zvyšovanie základnej mzdy
            moneyz -= 50
            Z += 1
            print(f"| Úspech: Prijatý nový zamestnanec. Aktuálny počet (Z): {Z}")
            
        elif action == "fire somebody":
            # Kontrola minimálneho počtu zamestnancov
            if Z > MIN_EMPLOYEES:
                moneyz += 100 # Môže byť malá úspora
                Z -= 1
                print(f"| Úspech: Prepustený zamestnanec. Aktuálny počet (Z): {Z}")
            else:
                print(f"| CHYBA: Potrebujete aspoň {MIN_EMPLOYEES} zamestnanca na prevádzku.")
            
        elif action == "salary":
            try:
                new_q = float(input("Aký bude nový plat (q)? (min. 1): "))
                # Kontrola kladnej hodnoty a logického rozsahu
                if new_q >= 1.0:
                    q = new_q
                    print(f"| Úspech: Nová mzda (q) je nastavená na {q} €.")
                else:
                    print("| CHYBA: Plat musí byť kladné číslo.")
            except ValueError:
                print("| CHYBA: Zlý formát vstupu. Zadajte prosím číslo.")
            
        elif action == "set price":
            try:
                new_C = float(input("Nová cena (C): (min. 1): "))
                # Kontrola kladnej hodnoty
                if new_C >= 1.0:
                    C = new_C
                    print(f"| Úspech: Nová cena kávy (C) je nastavená na {C} €.")
                else:
                    print("| CHYBA: Cena musí byť kladné číslo.")
            except ValueError:
                print("| CHYBA: Zlý formát vstupu. Zadajte prosím číslo.")
            
        elif action == "expand":
            COST = 1000
            if moneyz >= COST:
                moneyz -= COST
                N += 1
                print(f"| Úspech: Otvorená nová pobočka. Počet (N): {N}. Zostatok: {moneyz:,.2f} €")
            else:
                print(f"| CHYBA: Na expanziu potrebujete {COST} €. Máte len {moneyz:,.2f} €.")
            
        elif action == "make it fancy":
            COST = 500
            if moneyz >= COST:
                moneyz -= COST
                a = max(MIN_A_FACTOR, a - 15) # Zvýšenie kvality (zníženie 'a')
                M += 100 # Zvýšenie potenciálneho dopytu
                rent += 50 # Zvýšenie nájmu (fixný náklad)
                print(f"| Úspech: Pobočka je luxusnejšia. Zvýšený dopyt a nájom. Zostatok: {moneyz:,.2f} €")
            else:
                print(f"| CHYBA: Na vylepšenie potrebujete {COST} €. Máte len {moneyz:,.2f} €.")
                
        elif action == "ok":
            go = True
            
        elif action == "exit" or action == "even thou this game is excelent i do not wish to play it for the time being": 
            running = False
            go = True
            
        else:
            print("| UPOZORNENIE: Neznámy príkaz.")

    D += 1

if moneyz <= -100:
    print("\n" + "#"*40)
    print("BANKROT! Vaše dlhy prekročili 100 €.")
    print(f"Koncový zostatok: {moneyz:,.2f} €")
    print("#"*40)
elif not running:
    print("\nHra bola ukončená na žiadosť hráča.")