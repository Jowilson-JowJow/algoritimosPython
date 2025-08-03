//Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde h corresponde à altura):
//• Homens: (72.7∗ h)−58
//• Mulheres: (62,1∗ h)−44,7
package lista_exercicios_01;

import java.util.Scanner;

public class ex17_jow {
    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite:\nM - maculino\nF para feminino");        
        String sexo = scan.nextLine();
        sexo=sexo.toLowerCase();
        
        System.out.println("Digite a sua altura: ");        
        Double altura = scan.nextDouble();

        if(sexo.equals("f")){
           Double  peso_ideal=(62.1*altura)-44.7;           
            System.out.println("seu peso ideal é: "+ peso_ideal);
        }
        else if (sexo.equals("m")){
            Double peso_ideal=(72.7*altura)-58;
            System.out.println("Seu peso ideal é "+ peso_ideal);
        }
        scan.close();
    }

    
}
