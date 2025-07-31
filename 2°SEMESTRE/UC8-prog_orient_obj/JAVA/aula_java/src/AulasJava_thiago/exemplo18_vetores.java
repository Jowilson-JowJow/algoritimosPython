package AulasJava_thiago;

public class exemplo18_vetores {
    public static void main(String[] args) {
        //lista de compra no hortifruti
        String[] frutas={"banana","maçã","kiwi","mamão"};//entre chaves {} os elementos String do vetor
        String fruta_preferida = frutas[1];
        System.out.println("minha fruta preferida é: "+fruta_preferida);

        for(int i=0; i< frutas.length; i++){
            System.out.println(frutas[i]);
        }

    }
}
