//Crie um programa que calcule e mostre a área de um trapézio. Sabe-se que: A=(basemaior+basmenor)*altura/2 -- Lembre-se a base maior e a base menor devem ser números maiores que zero.
package lista_exercicios_01;

import java.util.Scanner;

public class ex23_jow {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Vamos calcular a area do trapezio: ");
        System.out.println("Digite o valor da Base Maior: ");
        Double base_maior = scan.nextDouble();
        System.out.println("Digite o valor da Base Menor: ");
        Double base_menor = scan.nextDouble();
        System.out.println("Digite o valor da ALtura: ");
        Double altura = scan.nextDouble();
        if(base_maior>=0 && base_menor>=0 && altura>=0){
            Double area=((base_maior+base_menor)*altura)/2;
            System.out.printf("O trapezio tem base maior de B= %.2f u.m\nbase menor b= %.2f u.m\ne altura h= %.2f u.m\nA área do trapezio é A= %.2f u.m²",base_maior,base_menor,altura,area);
        }
        else{
            System.out.println("Digite apenas valores positivos.");
        }
        scan.close();
    }
    
}
