//Crie um programa que receba um número inteiro e verifique se este número é par ou ímpar.
package lista_exercicios_01;

import java.util.Scanner;

public class ex11_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite um numero: ");
        int num = scan.nextInt();
        if(num % 2 ==0){
            System.out.println("O numero digitado é par.");
        }
        else{
            System.out.println("O numero digitado é impar.");
        }
        scan.close();
    }
    
}

// em pytoh
// num = int(input('Digite um numero: '))
// num1 = num % 2

// if (num1 == 0):
//     print('O numero digitado é par.')
// else:
//     print('O numero digitado não é impar')





