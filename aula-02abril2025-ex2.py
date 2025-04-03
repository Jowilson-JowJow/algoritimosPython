#crie duas listas que represente as notas p1 e p2 de uma turma. depois calcule a media da turma em cada p1 e p2
listaP1=[7.0,8.3,10.0,6.5,9.3]
listaP2=[8.5,6.9,5.0,7.5,9.8]
media1=sum(listaP1)/len(listaP1)#o comando sum() soma os elemetos da lista enquanto o len() conta quantos elementos tem na lista
print("%.2f"%media1)#o comando "%.2f"% indica quantas casas decimal sera usado apos a virgula
media2=sum(listaP2)/len(listaP2)
print("%.2f" %media2)

