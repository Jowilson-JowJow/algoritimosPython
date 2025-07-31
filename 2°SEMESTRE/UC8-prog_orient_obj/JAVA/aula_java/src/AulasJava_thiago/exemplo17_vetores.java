package AulasJava_thiago;

public class exemplo17_vetores {
    public static void main(String[] args) {
        int num =10;//tamanho do vetor
        int[] vet=new int[num];//declaração e alocação de epaço para vetor "v"
        int i; // indice ou posição
        //processando on "n" do vetor 'v'
        for (i=0; i<num; i++){
            vet[i]=i;//na posição 'i' do vetor 'vet' armazena o valor da variavel 'i'
            System.out.println(vet[i]);
        }
    }
}
