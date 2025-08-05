//Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui umataxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
package lista_exercicios_01;
import java.util.Scanner;
public class ex29_jow {
    public static void main(String[] args){
        
        Scanner scan = new Scanner(System.in);
       
        while (true){
            System.out.println("\nDigite para qual estado será enviado a mercadoria:\n1 -- MG\n2 -- MS\n3 -- SP\n4 -- RJ\n0 -- SAIR");
            int destino = scan.nextInt();
            
            if(destino==0){
                System.out.println("Sistema Encerrado!!!");
                break;
            }

            System.out.println("Digite o Valor da mercadoria: ");
            double valor = scan.nextDouble();
            double valor_final=0;
            if(destino==1){
                valor_final=valor*1.07;
                System.out.printf("A mercadoria será enviada para o estado de MG e o valor da mercadoria após incidencia de 7%% de imosto é de R$ %.2f",valor_final);
            }
            else if(destino==2){
                valor_final=valor*1.08;
                System.out.printf("A mercadoria será enviada para o estado de MS e o valor da mercadoria após incidencia de 8%% de imosto é de R$ %.2f",valor_final);  
            }
            else if(destino==3){
                valor_final=valor*1.12;
                System.out.printf("A mercadoria será enviada para o estado de SP e o valor da mercadoria após incidencia de 12%% de imosto é de R$ %.2f",valor_final);  
            }
            else if(destino==4){
                valor_final=valor*1.15;
                System.out.printf("A mercadoria será enviada para o estado de RJ e o valor da mercadoria após incidencia de 15%% de imosto é de R$ %.2f",valor_final);  
            }
            
        }
        scan.close();
        

    }
    
}
