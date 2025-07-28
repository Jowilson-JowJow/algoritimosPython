import java.util.Scanner;
public class exemplo05
{
	public static void main(String[] args) {
     //printar inteiros %d
     //printar strings %s
     //printar double %f
    Scanner sc = new Scanner(System.in);
    System.out.println("Digite um numero: ");
    int number = sc.nextInt();
    System.out.println("O numero digitado foi: "+number);
	}
}