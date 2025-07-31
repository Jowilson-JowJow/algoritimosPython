//Crie um programa que leia um número inteiro e, caso ele seja positivo, calcule e mostre:
//• O número digitado ao quadrado;
//• A raiz quadrada do número digitado;

package lista_exercicios_01;

import java.util.Scanner;

public class ex10_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero: ");
        int num = scan.nextInt();
        if(num >=0){
            int quadrado = num*num;
            Double raiz = Math.sqrt(num);
            System.out.printf("O numero digitado foi: %d\nSeu quadrado perfeito é %d\nSua raiz quadrado é %.2f ",num,quadrado,raiz);
        }
        else{
            System.out.println("O numero digitado é negativo");
        }
        scan.close();
    }
    
}
