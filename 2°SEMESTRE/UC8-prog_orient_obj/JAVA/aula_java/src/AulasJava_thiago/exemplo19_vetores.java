package AulasJava_thiago;
import java.util.Scanner;

public class exemplo19_vetores {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int n=5;//tamanho do vetor
        int vet[]=new int[n];//declaração do vetor "vet"
        int i;//indice da posição
        
        //entrada de dados
        for(i=0; i<n;i++){
            System.out.printf("informe %2d°. valor de %d: ",(i+1),n);
            vet[i]=scan.nextInt();
            scan.close();
        }
        
        for(i=0; i<n;i++){
            System.out.println( vet[i]);
            
        }   
    }
}
