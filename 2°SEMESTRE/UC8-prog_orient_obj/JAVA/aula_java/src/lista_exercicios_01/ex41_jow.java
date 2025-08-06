//Calcule as raízes da equação de 2o grau.
// Lembrando que: x=(-b+-(delta)²)/2a
// Onde
// Δ = B²−4ac
// E ax2+ bx + c = 0 representa uma equação de 2o grau.
// A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não é equação
// de segundo grau”.
// i. Se Δ < 0, não existe real. Imprima a mensagem: Não existe raiz.
// ii. Se Δ = 0, existe uma raiz real. Imprima a raiz e a mensagem: Raiz única.
// iii. Se Δ ≥ 0, imprima as duas raízes reais.
package lista_exercicios_01;

import java.util.Scanner;

public class ex41_jow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Vamos verificar as raizes da equação do 2° grau.");
        System.out.println("Digite o valor de a= ");
        int a=scan.nextInt();
        System.out.println("Digite o valor de b= ");
        int b=scan.nextInt();
        System.out.println("Digite o valor de c= ");
        int c=scan.nextInt();

        if(a==0){
            System.out.println("Não é equação de segundo grau");
        }
        else{
            double delta = b*b-4*a*c;
            if(delta<0){
                System.out.printf("Não existe raiz.");
            }
            else if(delta==0){
                double raiz=(-b)/(2*a);
                System.out.printf("Raiz Unica. E a raiz da equação de 2° Grau é %.2f",raiz);
            }
            else if(delta>0){
                double raiz1=(((-b)+Math.pow(delta,0.5))/(2*a));
                double raiz2=(((-b)-Math.pow(delta,0.5))/(2*a));
                System.out.printf("Raizes da equação do 2° são:\nx¹ = %.2f\nx² = %.2f",raiz1,raiz2);
            }
        }
        scan.close();
    }
}
