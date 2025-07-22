#2. Dicionário de Estoque Vamos às compras. Crie um dicionário que represente o estoque de uma loja, com produtos como chaves e quantidades em estoque como valores. Permita que o usuário insira um produto e verifique se ele está em estoque. Se estiver, informe a quantidade em estoque; caso contrário, informe que o produto não está disponível.
inventario={"adaptador usb": {"quantidade": 12, "valor": 349.99}, "alexa echo": {"quantidade": 8, "valor": 1249.50},
"alto-falante": {"quantidade": 23, "valor": 199.90}, "amplificador": {"quantidade": 5, "valor": 899.00}, 
"antena digital": {"quantidade": 14, "valor": 120.00}, "aparelho dvd": {"quantidade": 9, "valor": 450.00},
"aspirador robô": {"quantidade": 8, "valor": 3200.75}, "auricular bluetooth": {"quantidade": 16, "valor": 179.90},
"babá eletrônica": {"quantidade": 11, "valor": 399.99}, "balança digital": {"quantidade": 20, "valor": 259.50},
"barbeador elétrico": {"quantidade": 7, "valor": 350.00}, "base recarregadora": {"quantidade": 15, "valor": 190.80},
"bateria portátil": {"quantidade": 25, "valor": 799.99}, "blu-ray player": {"quantidade": 6, "valor": 450.50},
"bluetooth speaker": {"quantidade": 19, "valor": 270.00}, "caixa acústica": {"quantidade": 13, "valor": 129.99},
"caixa de som": {"quantidade": 18, "valor": 350.00}, "calculadora científica": {"quantidade": 10, "valor": 99.90},
"campainha smart": {"quantidade": 5, "valor": 220.75}, "capinha de celular": {"quantidade": 30, "valor": 29.99},
"carregador portátil": {"quantidade": 22, "valor": 120.00}, "carregador sem fio": {"quantidade": 16, "valor": 350.50},
"cartão de memória": {"quantidade": 14, "valor": 80.00}, "celular": {"quantidade": 9, "valor": 2300.99},
"chromecast": {"quantidade": 7, "valor": 420.00}, "controle remoto": {"quantidade": 21, "valor": 150.00},
"câmera digital": {"quantidade": 8, "valor": 899.90}, "câmera ip": {"quantidade": 12, "valor": 350.00},
"câmera de ação": {"quantidade": 17, "valor": 680.00}, "despertador digital": {"quantidade": 11,
"valor": 150.50},"dvr": {"quantidade": 14, "valor": 1099.99}, "dock station": {"quantidade": 10,
"valor": 399.90}, "drive ssd": {"quantidade": 18, "valor": 850.00}, "entrada hdmi": {"quantidade": 12, "valor": 250.75},
"fone bluetooth": {"quantidade": 20, "valor": 320.00}, "fone de ouvido": {"quantidade": 22, "valor": 150.50},
"fonte de alimentação": {"quantidade": 7, "valor": 600.00}, "gabinete pc": {"quantidade": 11, "valor": 299.99},
"headset gamer": {"quantidade": 15, "valor": 420.00}, "hub usb": {"quantidade": 9, "valor": 100.00},
"impressora": {"quantidade": 5, "valor": 799.00}, "joystick": {"quantidade": 8, "valor": 250.00},
"leitor biométrico": {"quantidade": 17, "valor": 1250.00}, "leitor de cartão": {"quantidade": 13, "valor": 180.00},
"microfone": {"quantidade": 16, "valor": 300.00}, "monitor": {"quantidade": 10, "valor": 1300.00},
"mouse gamer": {"quantidade": 21, "valor": 220.00}, "mouse sem fio": {"quantidade": 24, "valor": 180.00},
"notebook": {"quantidade": 6, "valor": 4500.00}, "placa de vídeo": {"quantidade": 14, "valor": 2500.00},
"placa mãe": {"quantidade": 9, "valor": 1200.00}, "power bank": {"quantidade": 23, "valor": 200.00},
"projetor": {"quantidade": 8, "valor": 3500.00}, "roteador": {"quantidade": 15, "valor": 350.00},
"scanner": {"quantidade": 7, "valor": 400.00}, "smartphone": {"quantidade": 25, "valor": 3200.00},
"smartwatch": {"quantidade": 19, "valor": 900.00}, "teclado": {"quantidade": 20, "valor": 200.00},
"tv led": {"quantidade": 11, "valor": 2200.00}, "webcam": {"quantidade": 13, "valor": 320.00},
"adaptador hdmi": {"quantidade": 18, "valor": 129.99}, "antena wi-fi": {"quantidade": 22, "valor": 89.90},
"ar condicionado portátil": {"quantidade": 5, "valor": 1999.00}, "bateria de notebook": {"quantidade": 14, "valor": 350.75},
"cabo usb": {"quantidade": 30, "valor": 39.90}, "caixa de som bluetooth": {"quantidade": 20, "valor": 179.99},
"carregador veicular": {"quantidade": 16, "valor": 99.99}, "controle de jogo": {"quantidade": 12, "valor": 399.00},
"docking station": {"quantidade": 8, "valor": 499.99}, "estabilizador": {"quantidade": 10, "valor": 250.00},
"fita hdmi": {"quantidade": 25, "valor": 15.99}, "fonte de energia": {"quantidade": 7, "valor": 499.90},
"hub usb-c": {"quantidade": 18, "valor": 129.90}, "impressora multifuncional": {"quantidade": 9, "valor": 899.99},
"leitor de ebook": {"quantidade": 11, "valor": 1200.00}, "microfone usb": {"quantidade": 15, "valor": 299.99},
"monitor gamer": {"quantidade": 14, "valor": 2300.00}, "mouse gamer sem fio": {"quantidade": 22, "valor": 499.00},
"pen drive": {"quantidade": 28, "valor": 99.00}, "placa de som": {"quantidade": 10, "valor": 350.00},
"placa de rede": {"quantidade": 8, "valor": 150.00}, "power supply": {"quantidade": 6, "valor": 900.00},
"projetor portátil": {"quantidade": 13, "valor": 1499.99}, "rádio comunicador": {"quantidade": 5, "valor": 650.00},
"roteador wi-fi": {"quantidade": 24, "valor": 350.00}, "smart home hub": {"quantidade": 7, "valor": 799.90},
"smartphone dual sim": {"quantidade": 17, "valor": 2200.00}, "tablet": {"quantidade": 20, "valor": 1800.00},
"teclado mecânico": {"quantidade": 11, "valor": 550.00}, "webcam hd": {"quantidade": 9, "valor": 399.99},
"adaptador de energia": {"quantidade": 14, "valor": 199.99}, "antivírus": {"quantidade": 25, "valor": 99.90},
"armazenamento externo": {"quantidade": 18, "valor": 320.00}, "base para notebook": {"quantidade": 10, "valor": 150.00},
"cabo de rede": {"quantidade": 22, "valor": 40.00}, "câmera de segurança": {"quantidade": 12, "valor": 450.50},
"câmera instantânea": {"quantidade": 7, "valor": 699.99}, "caixa de som 2.1": {"quantidade": 15, "valor": 320.00},
"carregador rápido": {"quantidade": 30, "valor": 120.00}, "controlador midi": {"quantidade": 8, "valor": 550.00},
"dock usb": {"quantidade": 11, "valor": 299.99}, "filtro de linha": {"quantidade": 20, "valor": 100.00},
"fonte atx": {"quantidade": 17, "valor": 399.90}, "fone de ouvido gamer": {"quantidade": 23, "valor": 270.00},
"hd externo": {"quantidade": 19, "valor": 600.00}, "hub usb 3.0": {"quantidade": 16, "valor": 200.00},
"impressora 3d": {"quantidade": 5, "valor": 3500.00}, "interface de áudio": {"quantidade": 9, "valor": 999.99},
"leitor de cartão sd": {"quantidade": 14, "valor": 75.00}, "memória ram": {"quantidade": 21, "valor": 450.00},
"monitor ultrawide": {"quantidade": 7, "valor": 2500.00}, "mouse pad gamer": {"quantidade": 24, "valor": 45.00},
"notebook gamer": {"quantidade": 6, "valor": 5500.00}, "placa de captura": {"quantidade": 10, "valor": 1250.00},
"placa mãe gamer": {"quantidade": 8, "valor": 1800.00}, "projetor full hd": {"quantidade": 11, "valor": 3100.00},
"roteador mesh": {"quantidade": 13, "valor": 850.00}, "smartphone gamer": {"quantidade": 18, "valor": 4500.00},
"tablet android": {"quantidade": 20, "valor": 1500.00}, "teclado rgb": {"quantidade": 15, "valor": 700.00},
"amplificador de som": {"quantidade": 12, "valor": 1200.00}, "antena parabólica": {"quantidade": 8, "valor": 600.00},
"aquecedor elétrico": {"quantidade": 5, "valor": 350.00}, "bateria externa": {"quantidade": 22, "valor": 150.00},
"caixa de som portátil": {"quantidade": 18, "valor": 299.99}, "carregador solar": {"quantidade": 10, "valor": 450.00},
"câmera ip wireless": {"quantidade": 14, "valor": 1200.00}, "câmera profissional": {"quantidade": 6, "valor": 3200.00},
"computador desktop": {"quantidade": 7, "valor": 4000.00}, "controlador de drone": {"quantidade": 9, "valor": 750.00},
"dock para hd externo": {"quantidade": 15, "valor": 180.00}, "estabilizador de tensão": {"quantidade": 11, "valor": 900.00},
"fonte chaveada": {"quantidade": 13, "valor": 350.00}, "fone intra-auricular": {"quantidade": 20, "valor": 120.00},
"gabinete gamer": {"quantidade": 16, "valor": 450.00}, "hd interno": {"quantidade": 19, "valor": 400.00},
"hub de carregamento": {"quantidade": 25, "valor": 350.00}, "impressora fotográfica": {"quantidade": 8, "valor": 1100.00},
"leitor de blu-ray": {"quantidade": 10, "valor": 700.00}, "memória externa": {"quantidade": 21, "valor": 250.00},
"monitor 4k": {"quantidade": 9, "valor": 2800.00}, "mouse ergonômico": {"quantidade": 23, "valor": 150.00},
"notebook ultrafino": {"quantidade": 6, "valor": 5300.00}, "placa de rede wireless": {"quantidade": 12, "valor": 320.00},
"placa tuner tv": {"quantidade": 7, "valor": 600.00}, "projetor 3d": {"quantidade": 5, "valor": 4500.00},
"roteador gigabit": {"quantidade": 15, "valor": 550.00}, "smartphone android": {"quantidade": 24, "valor": 2100.00},
"tablet ios": {"quantidade": 20, "valor": 3000.00}, "teclado wireless": {"quantidade": 18, "valor": 350.00},
"adaptador bluetooth": {"quantidade": 14, "valor": 220.00}, "antena 4g": {"quantidade": 9, "valor": 150.00},
"ar condicionado split": {"quantidade": 5, "valor": 2500.00}, "bateria para drone": {"quantidade": 11, "valor": 350.00},
"caixa amplificada": {"quantidade": 16, "valor": 1200.00}, "cabo hdmi 2.1": {"quantidade": 25, "valor": 80.00},
"carregador usb-c": {"quantidade": 20, "valor": 100.00}, "controle remoto universal": {"quantidade": 13, "valor": 90.00},
"dock para iphone": {"quantidade": 8, "valor": 150.00}, "estabilizador de imagem": {"quantidade": 7, "valor": 500.00},
"fone de ouvido sem fio": {"quantidade": 22, "valor": 250.00}, "gabinete para pc": {"quantidade": 19, "valor": 350.00},
"hd externo portátil": {"quantidade": 17, "valor": 600.00}, "hub para notebook": {"quantidade": 14, "valor": 120.00},
"impressora laser": {"quantidade": 6, "valor": 850.00}, "leitor de código de barras": {"quantidade": 9, "valor": 450.00},
"memória flash": {"quantidade": 23, "valor": 75.00}, "monitor curvo": {"quantidade": 12, "valor": 1700.00},
"mouse bluetooth": {"quantidade": 21, "valor": 140.00}, "notebook 2 em 1": {"quantidade": 10, "valor": 4300.00},
"placa de captura hdmi": {"quantidade": 8, "valor": 1100.00}, "placa de rede ethernet": {"quantidade": 15,
"valor": 250.00}, "projetor portátil mini": {"quantidade": 13, "valor": 650.00}, "rádio digital": {"quantidade": 7, "valor": 380.00},
"roteador wireless": {"quantidade": 24, "valor": 320.00}, "smart home speaker": {"quantidade": 16, "valor": 500.00},
"smartphone 5g": {"quantidade": 20, "valor": 2800.00}, "tablet windows": {"quantidade": 11, "valor": 2300.00},
"teclado gamer mecânico": {"quantidade": 18, "valor": 750.00}, "webcam full hd": {"quantidade": 15, "valor": 450.00}}
print('='*64)
print('=',' '*10,'BEM VINDO A LOJA DE ELETRôNICO DO JOWs',' '*10 ,'=')
print('='*64)
while True:
    estoque=input('DIGITE:\n1--PARA VERIFICAR DISPONIBILIDADE DO PRODUTO: \n2--PARA INSERIR O PRODUTO NO ESTOQUE:\nX--para sair do estoque:\n')
    if estoque=='1':
        produto=input('Digite o nome do prduto:\n').lower()
        if produto in inventario:
            print( f'O produto: ', produto,'possui: ',inventario[produto])
        else:
            print('Produto não encontrado no estoque.\nFaça outra pesquisa (Digite: 1) ou Insira o produto no inventario do estoque (Digite: 2)\n')
    elif estoque=='2':
        produto_novo_in=input('Digite o produto: \n').lower()
        qty_prod_novo=int(input('Digite a quantidade do prdduto: \n').lower())
        valor_prod_novo=float(input('Digite o valor do produto: \n'))
        inventario[produto_novo_in]={'quantidade':qty_prod_novo,'valor':valor_prod_novo}
        print( f'O produto', produto_novo_in,'foi inserido no estoque.\nEle possui ',qty_prod_novo, 'peças\nSeu preço é de: R$: ',valor_prod_novo)
    else: 
        estoque =='x'
        break

