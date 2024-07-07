import sys
import math

gamma_c = 1.5

def show_all_variables():
    print("\n")
    print("All inputs entered by user:")
    print("a:",a,'m')
    print("b:", b,'m')
    print("thickness T_s:",T_s,'m')
    print("f_cu:",f_cu,'N/mm^2')
    print("wall load:",wall_load,'t/m^2')
    print("live load:",live_load,'t/m^2')
    print("L1:",L1,'m')
    print("L2:",L2,'m')
    print("F_c:",F_c,'t/m^2')
    print("Column Type:", column_type)
    
    print("\n")
    
    print("Variables calculated from inputs")
    print("depth:",depth,'m')
    print("a_1:",a_1,'m')
    print("b_1:",b_1,'m')
    print("Beta_o:",beta_o,'m')
    print("w_u:",w_u)
    print("Beta", beta,'m')
    print("QU:",QU)   

def get_secondary_variables():
    global depth,a_1, b_1, beta_o, w_u, QU, beta, qp, initial_allowable,allowable # so that i can use it outsied 
    #Variables to calculate from inputs

    depth = T_s - 0.003
    a_1 = a + depth
    b_1 = b + depth
    beta_o = (2*a_1) + (2*b_1)
    w_u = (1.4 * ((2.5*T_s) + F_c + wall_load)) + (1.6*live_load)

    if column_type == 'interior':
        QU = w_u * ((L1*L2) - (a_1*b_1))
        beta = 1.15
    elif column_type == 'exterior':
        QU = w_u * ((L1*L2)/2 - (a_1*b_1))
        beta = 1.30
    else:
        QU = w_u * ((L1*L2)/4 - (a_1*b_1)) 
        beta = 1.50 


    # Calculating Punching Stress and rescale to N/mm^2
    qp = ((QU * beta) / (beta_o * depth))

    #Calculating the allowable
    initial_allowable = 0.316 * math.sqrt(f_cu / gamma_c)
    allowable = max(initial_allowable,1.6)

def check_safety(qp,allowable):
    print("\n")
    print("qp:", qp,'MPa')
    print("allowable:", allowable, "MPa")
    if qp <= 0:
        print('qp has to be a positive number, please revise the inputs')
    else:
        print("\n")
        if qp<allowable:
            print("Safe")
        else:
            print("NOT Safe")   

def get_numerical_input(prompt):
    while True:     
        user_input = input(prompt)
        if user_input.lower() == 'x':
            print("Exit requested by user.")
            sys.exit(0)  # Terminates the running program
        try:
            val = float(user_input)
            if val > 0:
                return val
            else:
                print("Please enter a non-negative number")
        except ValueError:
            print("Invalid input. Please enter a valid number or press 'x' to exit.")

def get_column_type():
    while True:
        print("1. Interior")
        print("2. Exterior")
        print("3. Corner")
        choice = input("Enter the type of column (1, 2, 3): ")
        if choice == '1':
            return 'interior'
        elif choice == '2':
            return 'exterior'
        elif choice == '3':
            return 'corner'
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Re-record inputs")
        print("2. Show All Variables")
        print("3. Exit System")
        choice = input("Enter your choice: ")
        if choice == '1':
            Program()
        elif choice == '2':
            show_all_variables()
        elif choice == '3':
            print("Exiting program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 3")

def Program():
    global a, b, T_s, f_cu, wall_load, live_load, L1, L2, F_c, column_type
    print("At any point, Input x if you want to exit")
    a = get_numerical_input("Enter dimension a of the column (m): ") * 1000
    b = get_numerical_input("Enter dimension b of the column (m): ")
    T_s = get_numerical_input("Enter thickness T_s of the column (m): ")
    f_cu = get_numerical_input("Enter compressive strength f_cu (N/mm^2): ")
    wall_load = get_numerical_input("Enter wall load (t/m^2): ") * 0.00981
    live_load = get_numerical_input("Enter live load (t/m^2): ") * 0.00981
    L1 = get_numerical_input("Enter L1 (m): ")
    L2 = get_numerical_input("Enter L2 (m): ")
    F_c = get_numerical_input("Enter flooring cover F_c (t/m^2): ") * 0.00981
    column_type = get_column_type()
    get_secondary_variables()
    check_safety(qp, allowable)  # Placeholder values for qp and allowable
    menu()

if __name__ == '__main__':
    Program()
