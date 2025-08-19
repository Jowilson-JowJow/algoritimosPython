package AulasJava_thiago;

import java.util.Scanner;

public class exemplo25_matriz {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite o numeros de linhas: ");
        int linhas=scan.nextInt();
        
        System.out.println("Digite o numeros de colunas: ");
        int colunas=scan.nextInt();
        
        
        int m[][]= new int [linhas][colunas];
        int i, j;
        
        System.out.println("Digite os elementos da mtriz: ");
        for(i=0; i<linhas;i++){
            for(j=0; j<colunas;j++){
                System.out.println("Elemento [" +i+"]["+j+"]: ");
                m[i][j]=scan.nextInt();
            }
        }
        
        for(i=0; i<m.length; i++){
            System.out.printf( "%d linha: ",(i+1) );
            for (j=0; j<m[i].length;j++){
                System.out.printf("%d ",m[i][j]);    
            }
            System.out.println("\n");
        }
        scan.close();


    }
    
}
