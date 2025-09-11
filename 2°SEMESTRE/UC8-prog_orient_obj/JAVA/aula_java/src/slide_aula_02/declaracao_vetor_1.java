package slide_aula_02;

public class declaracao_vetor_1 {
     public static void main(String[] args){
        int num=10;//define o tamanho do vetor que nesse caso tem 10 posições
        int[] vet = new int[num];//cria um vetor com 10 posições onde todas as posições é 0
        int i;//cria indice ou poição sendo seus valores inteiros
        for (i=0;i<num;i++){
            vet[i]=(2*i+1);
            System.out.println(vet[i]);
        }

    }
}
