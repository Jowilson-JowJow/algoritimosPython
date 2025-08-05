//Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
//Categoria Idade
// Infantil 5 a 12
// Juvenil 12 a 17
// Sênior maiores de 18 anos

package lista_exercicios_01;

import java.util.Scanner;

public class ex31_jow {
    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);

        System.out.println("Digie a sua idade: ");
        int idade = scan.nextInt();

        
        if (idade>=5 && idade<12){
            System.out.println("+---------------+-------------+");
            System.out.println("|   Categoria   |    Idade    |");
            System.out.println("+---------------+-------------+");
            System.out.println("|    Infantil   |    5 a 12   |");
            System.out.println("+---------------+-------------+");
        }
        else if(idade>=12 && idade<18){
            System.out.println("+---------------+-------------+");
            System.out.println("|   Categoria   |    Idade    |");
            System.out.println("+---------------+-------------+");
            System.out.println("|    Juvenil    |   12 a 17   |");
            System.out.println("+---------------+-------------+");
        }
        else if(idade>=18){
            System.out.println("+---------------+-------------+");
            System.out.println("|   Categoria   |    Idade    |");
            System.out.println("+---------------+-------------+");
            System.out.println("|    senior     | acima de 18 |");
            System.out.println("+---------------+-------------+");
        }
        else if(idade<5){
            System.out.println("Menor de idade para competir!!");
        }
        scan.close();
    }
    
}
