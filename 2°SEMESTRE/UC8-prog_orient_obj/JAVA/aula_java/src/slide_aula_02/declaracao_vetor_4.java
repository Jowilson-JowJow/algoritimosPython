package slide_aula_02;

public class declaracao_vetor_4 {
    public static void main(String[] args){
        String semafaro[]={"vermelho","amarelo","verde"};
        System.out.println("Ordem de um semáfaro:\n");
        for(String sinal: semafaro){
            System.out.printf("%s\n",sinal);
        }
    }
}
