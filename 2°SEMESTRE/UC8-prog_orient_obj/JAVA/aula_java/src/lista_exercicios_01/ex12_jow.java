//Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
package lista_exercicios_01;

import java.util.Scanner;

public class ex12_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero: ");
        int num = scan.nextInt();
        
        System.out.println("Digite outro numero: ");
        int num1 = scan.nextInt();


        if(num>num1){
            int sub = num-num1;
            System.out.printf("Os numeros digitados foram %d e %d\nO maior numero é %d e a diferença entre os dois numeros é %d",num,num1,num,sub);
        }
        else if(num1>num){
            int sub = num1-num;
            System.out.printf("Os numeros digitados foram %d e %d\nO maior numero é %d e a diferença entre os dois numeros é %d",num,num1,num1,sub);
        }
        else{
            System.out.println("Os numeros digitados são iguais ou invalidos!");
        }
        scan.close();

    }

}
