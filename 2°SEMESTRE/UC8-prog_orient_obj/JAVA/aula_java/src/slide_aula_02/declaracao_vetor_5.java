package slide_aula_02;

import java.util.Arrays;
import java.util.Scanner;

public class declaracao_vetor_5 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int n=5;
        int vet[]=new int[n];
        int i;
        for (i=0;i<n;i++){
            System.out.printf("Informe %d ° valor de %d: ",(i+1),n);
            vet[i]=scan.nextInt();
        }
        System.out.println(Arrays.toString(vet));
        scan.close();
    }
}
