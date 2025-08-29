//Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes. A primeira vez deve usar a estrutura de repetição for e a segunda while.
package lista_exercicios_02;

public class ex4Jow {
    public static void main(String[] args){
        int i=0;
        int x=0;
        while(i<100){
            x=i+1;
            System.out.println("com while: "+x);
            i++;
        }
        for(i=0;i<100;i++){
            x=i+1;
            System.out.println("com for: "+x);
        }
    }
}
