package slide_aula_02;

public class declaracao_vetor_3 {
    public static void main(String[] args){
        String mes[]={"janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"};
        int[] diaMes = {31,28,31,30,31,30,31,31,30,31,30,31};
        for(int i=0;i<12;i++){
            System.out.printf("%s, tem %d dias\n",mes[i],diaMes[i]);
        }
    }
}
