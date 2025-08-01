//Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem: Números iguais.
package lista_exercicios_01;

import java.util.Scanner;

public class ex13_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero: ");
        int num = scan.nextInt();
        
        System.out.println("Digite outro numero: ");
        int num1 = scan.nextInt();


        if(num>num1){
            System.out.printf("Os numeros digitados foram %d e %d\nO maior numero é %d",num,num1,num);
        }
        else if(num1>num){
            System.out.printf("Os numeros digitados foram %d e %d\nO maior numero é %d",num,num1,num1);
        }
        else if(num==num1){
            System.out.println("Os numeros digitados são iguais");
        }
        else{
            System.out.println("Os numeros invalidos!");
        }
        scan.close();

    }

}
