//Crie um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve será informado ao usuário e o programa termina.
package lista_exercicios_01;

import java.util.Scanner;

public class ex14_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite a primeira nota: ");
        Double nota1 = scan.nextDouble();
        
        System.out.println("Digite a segunda nota: ");
        Double nota2 = scan.nextDouble();


        if(nota1<=10 && nota1>=0 && nota2>=0 && nota2>=0){
            Double media = (nota1+nota2)/2;
            System.out.printf("As notas digitadas foram %.2f e %.2f\nA média é %.2f",nota1,nota2,media);
        }
        else{
            System.out.println("Notas invalidas!");
        }
        scan.close();

    }

}
