//Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros números naturais e,
// 1^2 + 2^2 + ... + 10^2 = 385
// • quadrado da soma dos dez primeiros números naturais é,
// (1 + 2 + ... + 10)2 = 552 = 3025
// A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma e 3025-385 = 2640.
package lista_exercicios_02;


public class ex41Jow {
    public static void main(String[] args){
        int i,j;
        int soma1=0;
        int soma2=0;
        int quadrado=0;
        int resultado1=0;
        int resultado2=0;
        for(i=1;i<101;i++){
            quadrado=(int)Math.pow(i,2);
            soma1=soma1+quadrado;
        }
        System.out.println(soma1);
        for(j=1;j<101;j++){
            soma2=soma2+j;
        }
        resultado1=(int)Math.pow(soma2,2);
        resultado2=resultado1-soma1;
        System.out.printf("A soma dos quadrados dos 100 primeiros numeros naturais é: %d\nA quadrado da soma dos 100 primeiros numeros naturais é: %d\nA diferença entre eles é: %d",soma1,resultado1,resultado2);
    }
}
