//Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
// 1 , 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
// 5 - Voto Nulo
// 6 - Voto em Branco
// Faça um programa que calcule e mostre:
// ▪ O total de votos para cada candidato;
// ▪ O total de votos nulos;
// ▪ O total de votos em branco;
// ▪ A percentagem de votos nulos sobre o total de votos;
// ▪ A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
package lista_exercicios_02;

import java.util.Scanner;

public class ex42Jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int candidato1 = 0, candidato2 = 0, candidato3 = 0, candidato4 = 0;
        int nulos = 0, brancos = 0;
        int totalVotos = 0; 
        while (true){
            System.out.println("****Cedula de votação, digite o numero do candidato****");
            System.out.println("1 - João da pinga\n2 - Mané dos pobres\n3 - Mario do armario\n4 - Zé busca pé\n5 - Voto Nulo\n6 - Voto em Branco\n0 - para sair");
            int escolha=scan.nextInt();
            if(escolha==1){
                candidato1++;
                totalVotos++;
                
            }
            else if(escolha==2){
                candidato2++;
                totalVotos++;
            }
            else if(escolha==3){
                candidato3++;
                totalVotos++; 
            }
            else if(escolha==4){
                candidato4++;
                totalVotos++;
            }
            else if(escolha==5){
                nulos++;
                totalVotos++;
            }
            else if(escolha==6){
                brancos++;
                totalVotos++;
            }
            else if(escolha==0){
                System.out.println("Votação Encerrada");
                break;
            }
        }
        double percNulos = (nulos * 100.0) / totalVotos;
        double percBrancos = (brancos * 100.0) / totalVotos;

        System.out.println("===== Resultado da Eleição =====");
        System.out.println("João da pinga: " + candidato1 + " votos");
        System.out.println("Mané dos pobres: " + candidato2 + " votos");
        System.out.println("Mario do armario: " + candidato3 + " votos");
        System.out.println("Zé busca pé: " + candidato4 + " votos");
        System.out.println("Nulos: " + nulos + " votos (" + String.format("%.2f", percNulos) + "%)");
        System.out.println("Brancos: " + brancos + " votos (" + String.format("%.2f", percBrancos) + "%)");
        System.out.println("Total de votos: " + totalVotos);
        scan.close();
    }
}
