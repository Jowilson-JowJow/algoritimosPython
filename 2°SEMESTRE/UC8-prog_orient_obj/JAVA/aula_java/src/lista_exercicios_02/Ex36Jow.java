//Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma mensagem de erro na tela, “Intervalo de valores invalido” e o programa´ termina. Exemplo de tela de saída:
// Digite o valor inicial e valor final: 5
// 10
// Soma dos ímpares neste intervalo: 21


package lista_exercicios_02;//Diz ao compilador que essa classe (Ex36Jow) faz parte do pacote lista_exercicios_02. Pacotes em Java são usados para organizar as classes em "pastas lógicas". Isso evita confusão de nomes de classes iguais e melhora a estrutura do projeto.


// Importação das classes necessárias
import java.util.ArrayList;//Importa a classe ArrayList, que permite criar listas dinâmicas (estruturas de dados que crescem de tamanho automaticamente). Diferente de um array fixo (int[]), o ArrayList pode ter elementos adicionados ou removidos livremente.

import java.util.List; //Importa a interface List, que define o comportamento genérico de uma lista em Java. ArrayList é uma implementação concreta dessa interface. Usar a interface List no lugar de ArrayList dá mais flexibilidade (se amanhã você quiser trocar por outra lista, como LinkedList, não precisa mudar todo o código).

import java.util.Scanner;//Importa a classe Scanner, que serve para ler dados digitados pelo usuário no console. Exemplo: nextInt() lê um número inteiro, nextLine() lê uma linha de texto.


public class Ex36Jow {    public static void main(String[] args) {
        // Objeto Scanner para leitura de dados via teclado
        Scanner scan = new Scanner(System.in);

        // Entrada dos valores de início e fim do intervalo
        System.out.println("Digite um valor de inicio e um valor de final:");
        int inicio = scan.nextInt();
        int fim = scan.nextInt();

        // Lista dinâmica para armazenar os números ímpares encontrados
        List<Integer> lista_impar = new ArrayList<>();

        // Estrutura de repetição para percorrer todos os números no intervalo
        for (int i = inicio; i <= fim; i++) {
            // Verifica se o número atual (i) é ímpar
            if (i % 2 != 0) {
                // Adiciona o número ímpar na lista
                lista_impar.add(i);
            }
        }

        // Exibição dos números ímpares encontrados
        System.out.println("Os numeros impares no intervalo dos numeros digitados são: " + lista_impar);

        // Cálculo da soma dos números ímpares
        int soma = 0;
        // Laço de repetição que percorre a lista "lista_impar" do primeiro elemento (índice 0) 
        // até o último elemento (índice size() - 1). 
        // A variável "j" funciona como índice para acessar cada posição da lista.
        for (int j = 0; j < lista_impar.size(); j++) {
            soma += lista_impar.get(j); // soma cada elemento da lista
        }

        // Exibição da soma total
        System.out.println("A soma dos numeros impares é: " + soma);

        // Fechamento do Scanner (boa prática)
        scan.close();
    }
}

