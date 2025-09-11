
package slide_aula_02;

public class declaracao_vetor_0 {
    public static void main(String[] args){
        int[] vet = new int[10];
        //vet é declarado com um vetor de inteiros.
        //a expressão new int[10] cria efetivamete o um vetor de inteiros,
        //de tamanho 10, dessa maneira temos o vetor onde cada posição tem valor zero
        // System.out.println(vet);
        // //quer dizer "um array ([) de inteiros (I) em tal posição de memória (hash 372f7a8d)".
        vet[0]=10;//troca o zero na primeira posição por 10
        vet[1]=vet[0]+10; //  na 2° posição pega o valor da primeira e soma com 10 
        System.out.println(vet[0]);//imprime 10
        System.out.println(vet[1]);//imprime 20(10+10)
        System.out.println(vet[2]);// nesse caso imprime 0
    }
   
}