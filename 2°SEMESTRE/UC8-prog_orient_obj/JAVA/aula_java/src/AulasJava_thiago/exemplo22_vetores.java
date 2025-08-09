package AulasJava_thiago;

import java.util.Scanner;

public class exemplo22_vetores {
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);
        int n=5;
        int vet[] = new int [n];
        int i;
        for (i=0;i<n;i++){
            System.out.printf("Informe %2d°. valor de %d: ",(i+1),n);
            vet[i]=scan.nextInt();
            scan.close();
        }
    }
}
