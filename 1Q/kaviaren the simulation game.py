import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# --- 4. Main Tkinter Setup ---
# Create the main window instance FIRST
root = tk.Tk()
root.title("Coffee Shop Tycoon Simulator")
root.geometry("1100x700") # Set initial window size

# --- 1. Game State Variables ---
# Use Tkinter's special variables for automatic GUI updates
moneyz_var = tk.DoubleVar(value=500.0)
N = 1 # Number of Shops
C = 6.0 # Price per Coffee
M = 400.0 # Market Demand (Base)
a = 50.0 # Attractiveness/Quality Factor
V = 5.0 # Variable Cost per Coffee
q = 70.0 # Staff Salary/Satisfaction
Z = 1 # Number of Employees
rent = 100.0 # Fixed Daily Rent
D = 1 # Day Counter

# Variables to display game stats
day_var = tk.IntVar(value=D)
profit_var = tk.DoubleVar(value=0.0)
N_var = tk.IntVar(value=N)
C_var = tk.DoubleVar(value=C)
M_var = tk.DoubleVar(value=M)
a_var = tk.DoubleVar(value=a)
V_var = tk.DoubleVar(value=V)
q_var = tk.DoubleVar(value=q)
Z_var = tk.IntVar(value=Z)
rent_var = tk.DoubleVar(value=rent)

# --- 2. Game Logic Function ---

def run_day():
    """Calculates daily profit and advances the day."""
    global moneyz_var, N, C, M, a, V, q, Z, rent, D
    global day_var, profit_var
    
    # Temporarily disable the RUN DAY button during calculation
    next_day_button.config(state=tk.DISABLED)
    
    # Check for game over condition
    if moneyz_var.get() < -100:
        messagebox.showinfo("Game Over", f"You went bankrupt after {D-1} days!")
        root.quit()
        return

    # --- Daily Calculations (as per the algorithm) ---
    Ml = 200 + Z * 400
    
    # Adjust Ml based on Staff Salary (q)
    if q > 100:
        Ml *= 1.2
    elif q > 80:
        Ml *= 1.1
    elif q < 60:
        Ml *= 0.9
    elif q < 50:
        Ml *= 0.8
    elif q < 40:
        Ml = 0
    
    # Cap Market Demand (M) at Max Potential (Ml)
    if M > Ml:
        current_M = Ml
    else:
        current_M = M

    I = random.uniform(0.7, 1.2)
    
    # Ensure customer count is non-negative
    customers = max(0, current_M - a * C)

    # Core Profit Calculation (P)
    P = I * N * ( (C - V) * customers - (q * Z) - rent)
    
    # Update game state
    moneyz_var.set(moneyz_var.get() + P)
    D += 1

    # Update GUI display variables
    day_var.set(D)
    profit_var.set(P)
    
    # Update status labels and plot
    update_stats_display()
    update_plot()

    # >>> CORRECTED LOGIC: ENABLE ACTION BUTTONS, RUN DAY REMAINS DISABLED UNTIL AN ACTION IS TAKEN <<<
    set_action_buttons_state(tk.NORMAL)
    print(M)


def set_action_buttons_state(state):
    """Enables or disables the action buttons."""
    # This list must be defined in the main scope after the buttons are created
    buttons_to_control = [
        ad_button, quality_plus_button, quality_minus_button,
        recruit_button, fire_button, fancy_button, expand_button
    ]
    for button in buttons_to_control:
        button.config(state=state)


def start_next_day():
    global rent, D
    """PREPARES the GUI for the next day's calculations by enabling action buttons."""
    # NOTE: This function's previous command was reversed. We rely on perform_action
    # to ENABLE the RUN DAY button.
    set_action_buttons_state(tk.NORMAL)
    rent = rent*(D/2)
    
    # We don't enable next_day_button here anymore. It's enabled by perform_action/set_new_price

# --- 3. Action Handlers ---

def perform_action(action_name):
    """Applies the effects of the chosen action."""
    global moneyz_var, N, C, M, a, V, q, Z, rent

    # ... (action logic remains the same) ...

    if action_name == "ad campaign":
        moneyz_var.set(moneyz_var.get() - 200)
        M += 40
    elif action_name == "coffee quality+":
        a -= 5
        V += 1
    elif action_name == "coffee quality-":
        a += 5
        V -= 1
    elif action_name == "recruitment":
        moneyz_var.set(moneyz_var.get() - 50)
        Z += 1
    elif action_name == "fire somebody":
        if Z == 1:
            messagebox.showinfo("Error", "Cannot fire the last employee.")
            return
        Z -= 1
    elif action_name == "expand":
        moneyz_var.set(moneyz_var.get() - 10000)
        N += 1
    elif action_name == "make it fancy":
        moneyz_var.set(moneyz_var.get() - 1000)
        a -= 15
        M += 100
        rent += 50

    # Update the display variables and plot after action
    update_game_state_vars()
    update_stats_display()
    update_plot()
    
    # >>> NEW LOGIC: Any action taken enables the RUN DAY button <<<
    next_day_button.config(state=tk.NORMAL)


def set_new_price():
    """Handles the 'set price' action with an input box."""
    global C
    try:
        new_price = float(price_entry.get())
        if new_price > 0:
            C = new_price
            C_var.set(C)
            price_entry.delete(0, tk.END)
            price_entry.insert(0, str(C))
            update_plot() # Update plot immediately after price change
            next_day_button.config(state=tk.NORMAL) # ENABLE RUN DAY after setting price
        else:
            messagebox.showerror("Error", "Price must be positive.")
    except ValueError:
        messagebox.showerror("Error", "Invalid price value.")

def set_new_salary():
    """Handles the 'salary' action with an input box."""
    global q
    try:
        new_salary = int(salary_entry.get())
        if new_salary >= 0:
            q = new_salary
            q_var.set(q)
            salary_entry.delete(0, tk.END)
            salary_entry.insert(0, str(q))
            update_plot() # Update plot
            next_day_button.config(state=tk.NORMAL) # ENABLE RUN DAY after setting salary
        else:
            messagebox.showerror("Error", "Salary cannot be negative.")
    except ValueError:
        messagebox.showerror("Error", "Invalid salary value.")


def update_game_state_vars():
    # ... (rest of the update functions remain the same) ...
    N_var.set(N)
    C_var.set(C)
    M_var.set(M)
    a_var.set(a)
    V_var.set(V)
    q_var.set(q)
    Z_var.set(Z)
    rent_var.set(rent)

def update_stats_display():
    # ... (rest of the update functions remain the same) ...
    moneyz_label.config(text=f"Total Savings: ${moneyz_var.get():.2f}")
    profit_label.config(text=f"Today's Profit: ${profit_var.get():.2f}")

    N_val_label.config(text=str(N_var.get()))
    C_val_label.config(text=f"${C_var.get():.2f}")
    M_val_label.config(text=str(M_var.get()))
    a_val_label.config(text=str(a_var.get()))
    V_val_label.config(text=f"${V_var.get():.2f}")
    q_val_label.config(text=f"${q_var.get():.0f}")
    Z_val_label.config(text=str(Z_var.get()))
    rent_val_label.config(text=f"${rent_var.get():.2f}")

# --- Plotting Function ---
# ... (update_plot remains the same) ...
def update_plot():
    # Recalculate dynamic Ml based on current Z and q
    Ml = 800 + Z * 500
    if q > 100: Ml *= 1.2
    elif q > 80: Ml *= 1.1
    elif q < 60: Ml *= 0.9
    elif q < 50: Ml *= 0.8
    elif q < 40: Ml = 0
    
    current_M = min(M, Ml) 

    # Define a range of prices (C) to evaluate the profit function
    C_range = np.linspace(V, 20, 200) 
    
    # Calculate Core Profit for the C_range
    P_core = []
    for c_val in C_range:
        customers = max(0, current_M - a * c_val)
        p = (c_val - V) * customers
        P_core.append(p)

    P_core = np.array(P_core)
    
    # 1. Clear the previous plot
    ax.clear()

    # 2. Plot the Profit Curve (excluding fixed costs for clarity)
    ax.plot(C_range, P_core, label='Potential Gross Profit Curve', color='blue')

    # 3. Plot the current position (C, P_core at C)
    current_customers = max(0, current_M - a * C)
    current_P_core = (C - V) * current_customers
    
    ax.plot(C, current_P_core, 'ro', markersize=8, label=f'Your Current Price: ${C:.2f}')
    
    # 4. Add the max potential profit point (Optional but helpful)
    try:
        C_opt = (current_M / a + V) / 2
        P_opt = (C_opt - V) * max(0, current_M - a * C_opt)
        ax.plot(C_opt, P_opt, 'g*', markersize=12, label=f'Optimal Price: ${C_opt:.2f}')
    except ZeroDivisionError:
        pass


    # 5. Labels and Titles
    ax.set_title('Price vs. Potential Gross Profit (Maximized Customers)')
    ax.set_xlabel('Price per Coffee (C)')
    ax.set_ylabel('Potential Gross Profit (per shop, before fixed costs)')
    ax.legend()
    ax.grid(True)
    ax.set_ylim(bottom=0)
    ax.set_xlim(left=V)

    # 6. Redraw the canvas
    canvas.draw()


# --- Tkinter Layout and Widget Creation (Now defined after root) ---

# Configure styles
tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 1, weight=1)
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.rowconfigure(root, 1, weight=1)


# --- Frame Setup ---
status_frame = tk.LabelFrame(root, text="💰 STATUS 💰", padx=10, pady=10)
status_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

stats_frame = tk.LabelFrame(root, text="📊 Current Metrics", padx=10, pady=10)
stats_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

actions_frame = tk.LabelFrame(root, text="🛠️ ACTIONS", padx=10, pady=10)
actions_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)

plot_frame = tk.LabelFrame(root, text="📈 Price-Profit Curve", padx=5, pady=5)
plot_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
tk.Grid.rowconfigure(root, 2, weight=2) # Give the plot frame more vertical space


# --- Matplotlib Integration ---
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# --- 5. STATUS Frame (Row 0, Col 0) ---

# Day Counter
tk.Label(status_frame, text="Day:", font=('Arial', 14)).grid(row=0, column=0, sticky="w", padx=5, pady=2)
tk.Label(status_frame, textvariable=day_var, font=('Arial', 14, 'bold')).grid(row=0, column=1, sticky="w", padx=5, pady=2)

# Saved Money
moneyz_label = tk.Label(status_frame, text=f"Total Savings: ${moneyz_var.get():.2f}", font=('Arial', 16, 'bold'), fg='blue')
moneyz_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

# Today's Profit
profit_label = tk.Label(status_frame, text=f"Today's Profit: ${profit_var.get():.2f}", font=('Arial', 12))
profit_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=2)

# NEXT DAY Button (The main game advancement button)
# COMMAND is simplified to just run_day. The enabling/disabling is handled inside run_day and perform_action.
next_day_button = tk.Button(status_frame, text="RUN DAY (CALCULATE PROFIT)", command=run_day, bg='green', fg='white', font=('Arial', 12, 'bold'))
next_day_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=10)
# >>> CORRECTED INITIAL STATE: The game starts ready to commit to Day 1 <<<
next_day_button.config(state=tk.NORMAL)


# --- 6. STATS Frame (Row 1, Col 0) ---
# ... (Stats frame widgets remain the same) ...

tk.Label(stats_frame, text="Shops (N):", anchor="w").grid(row=0, column=0, sticky="w")
N_val_label = tk.Label(stats_frame, textvariable=N_var, font=('Arial', 10, 'bold'))
N_val_label.grid(row=0, column=1, sticky="w")

tk.Label(stats_frame, text="Price (C):", anchor="w").grid(row=1, column=0, sticky="w")
C_val_label = tk.Label(stats_frame, textvariable=C_var, font=('Arial', 10, 'bold'))
C_val_label.grid(row=1, column=1, sticky="w")

tk.Label(stats_frame, text="Market Demand (M):", anchor="w").grid(row=2, column=0, sticky="w")
M_val_label = tk.Label(stats_frame, textvariable=M_var, font=('Arial', 10, 'bold'))
M_val_label.grid(row=2, column=1, sticky="w")

tk.Label(stats_frame, text="Quality Factor (a):", anchor="w").grid(row=3, column=0, sticky="w")
a_val_label = tk.Label(stats_frame, textvariable=a_var, font=('Arial', 10, 'bold'))
a_val_label.grid(row=3, column=1, sticky="w")

tk.Label(stats_frame, text="Variable Cost (V):", anchor="w").grid(row=4, column=0, sticky="w")
V_val_label = tk.Label(stats_frame, textvariable=V_var, font=('Arial', 10, 'bold'))
V_val_label.grid(row=4, column=1, sticky="w")

tk.Label(stats_frame, text="Salary (q):", anchor="w").grid(row=5, column=0, sticky="w")
q_val_label = tk.Label(stats_frame, textvariable=q_var, font=('Arial', 10, 'bold'))
q_val_label.grid(row=5, column=1, sticky="w")

tk.Label(stats_frame, text="Employees (Z):", anchor="w").grid(row=6, column=0, sticky="w")
Z_val_label = tk.Label(stats_frame, textvariable=Z_var, font=('Arial', 10, 'bold'))
Z_val_label.grid(row=6, column=1, sticky="w")

tk.Label(stats_frame, text="Daily Rent:", anchor="w").grid(row=7, column=0, sticky="w")
rent_val_label = tk.Label(stats_frame, textvariable=rent_var, font=('Arial', 10, 'bold'))
rent_val_label.grid(row=7, column=1, sticky="w")


# --- 7. ACTIONS Frame (Row 0/1, Col 1) ---

# Action Buttons
ad_button = tk.Button(actions_frame, text="Ad Campaign (-$200)", command=lambda: perform_action("ad campaign"))
quality_plus_button = tk.Button(actions_frame, text="Coffee Quality +", command=lambda: perform_action("coffee quality+"))
quality_minus_button = tk.Button(actions_frame, text="Coffee Quality -", command=lambda: perform_action("coffee quality-"))
recruit_button = tk.Button(actions_frame, text="Recruitment (-$50)", command=lambda: perform_action("recruitment"))
fire_button = tk.Button(actions_frame, text="Fire Somebody", command=lambda: perform_action("fire somebody"))
fancy_button = tk.Button(actions_frame, text="Make it Fancy (-$1000)", command=lambda: perform_action("make it fancy"))
expand_button = tk.Button(actions_frame, text="EXPAND (-$10000)", command=lambda: perform_action("expand"), bg='red', fg='white')

ad_button.grid(row=0, column=0, columnspan=2, sticky="ew", padx=2, pady=2)
quality_plus_button.grid(row=1, column=0, sticky="ew", padx=2, pady=2)
quality_minus_button.grid(row=1, column=1, sticky="ew", padx=2, pady=2)
recruit_button.grid(row=2, column=0, sticky="ew", padx=2, pady=2)
fire_button.grid(row=2, column=1, sticky="ew", padx=2, pady=2)
fancy_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=2, pady=2)
expand_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=2, pady=2)

tk.Label(actions_frame, text="--- Set Values ---", font=('Arial', 10, 'bold')).grid(row=5, column=0, columnspan=2, pady=5)

# Set Price
tk.Label(actions_frame, text="New Price:").grid(row=6, column=0, sticky="w")
price_entry = tk.Entry(actions_frame, width=10)
price_entry.grid(row=6, column=1, sticky="ew", padx=2, pady=2)
price_entry.insert(0, str(C))
tk.Button(actions_frame, text="Set Price", command=set_new_price).grid(row=7, column=0, columnspan=2, sticky="ew", padx=2, pady=2)

# Set Salary
tk.Label(actions_frame, text="New Salary:").grid(row=8, column=0, sticky="w")
salary_entry = tk.Entry(actions_frame, width=10)
salary_entry.grid(row=8, column=1, sticky="ew", padx=2, pady=2)
salary_entry.insert(0, str(q))
tk.Button(actions_frame, text="Set Salary", command=set_new_salary).grid(row=9, column=0, columnspan=2, sticky="ew", padx=2, pady=2)

# --- Initial Setup and Main Loop ---
update_game_state_vars() # Initialize the display variables
update_stats_display() # Update the labels

# All action buttons are enabled at the start of the game
set_action_buttons_state(tk.NORMAL)

# Draw the initial plot
update_plot()

root.mainloop()