# Início do programa
executando_principal = True

while executando_principal:
    # === MENU PRINCIPAL ===
    print("\n=== Menu Principal ===")
    print("1. Opção 1 (Acessar Submenu 1)")
    print("2. Opção 2 (Acessar Submenu 2)")
    print("3. Opção 3 (Acessar Submenu 3)")
    print("0. Sair")
    
    escolha_principal = input("Escolha uma opção: ")

    if escolha_principal == '1':
        # --- SUBMENU 1 ---
        executando_submenu = True
        while executando_submenu:
            print("\n--- Submenu 1 ---")
            print("1. Ação A do Submenu 1")
            print("2. Ação B do Submenu 1")
            print("3. Ação C do Submenu 1")
            print("9. Voltar ao Menu Principal")
            sub_escolha = input("Escolha uma opção: ")

            if sub_escolha == '1':
                print("Executando Ação A do Submenu 1...")
            elif sub_escolha == '2':
                print("Executando Ação B do Submenu 1...")
            elif sub_escolha == '3':
                print("Executando Ação C do Submenu 1...")
            elif sub_escolha == '9':
                executando_submenu = False  # Sai do submenu
            else:
                print("Opção inválida. Tente novamente.")

    elif escolha_principal == '2':
        # --- SUBMENU 2 ---
        executando_submenu = True
        while executando_submenu:
            print("\n--- Submenu 2 ---")
            print("1. Ação X do Submenu 2")
            print("2. Ação Y do Submenu 2")
            print("3. Ação Z do Submenu 2")
            print("9. Voltar ao Menu Principal")
            sub_escolha = input("Escolha uma opção: ")

            if sub_escolha == '1':
                print("Executando Ação X do Submenu 2...")
            elif sub_escolha == '2':
                print("Executando Ação Y do Submenu 2...")
            elif sub_escolha == '3':
                print("Executando Ação Z do Submenu 2...")
            elif sub_escolha == '9':
                executando_submenu = False  # Sai do submenu
            else:
                print("Opção inválida. Tente novamente.")

    elif escolha_principal == '3':
        # --- SUBMENU 3 ---
        executando_submenu = True
        while executando_submenu:
            print("\n--- Submenu 3 ---")
            print("1. Item I do Submenu 3")
            print("2. Item II do Submenu 3")
            print("3. Item III do Submenu 3")
            print("9. Voltar ao Menu Principal")
            sub_escolha = input("Escolha uma opção: ")

            if sub_escolha == '1':
                print("Executando Item I do Submenu 3...")
            elif sub_escolha == '2':
                print("Executando Item II do Submenu 3...")
            elif sub_escolha == '3':
                print("Executando Item III do Submenu 3...")
            elif sub_escolha == '9':
                executando_submenu = False  # Sai do submenu
            else:
                print("Opção inválida. Tente novamente.")

    elif escolha_principal == '0':
        print("\nSaindo do programa. Até mais!")
        executando_principal = False  # Sai do loop principal
        
    else:
        print("\n*** Opção inválida no Menu Principal. Tente novamente. ***")