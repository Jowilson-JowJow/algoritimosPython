package AulasJava_thiago;


public class Funcoes{

    public static void main (String[] args){
        // hello();
        // hello2("jowjow");
        // hello3("jowJow",48);

        // int res = soma(12,48);
        // System.out.println(res);

        // String name = myname();
        // System.out.println(name);  
        
        double meuimc =imc(140,1.82);
        System.out.printf("O IMC do Paciente é %.2f",meuimc);
    }
    //função do tipo void não retorna nada
    public static void hello(){
        System.out.println( "hellooooo!!");
    }

    public static void hello2(String nome){
        System.out.printf( "Hellooooo %s !!!", nome);
    }

    public static void hello3(String nome, int idade){
        System.out.printf( "\nHellooooo %S você tem %d!!", nome, idade);
    }

    public static int soma(int x, int y){
        int sum = x+y;
        return sum;
    }

    public static String myname(){
        return "JowJow";
    }

    public static double imc(double peso, double altura){
        double myimc=peso/(altura*altura);
        return myimc;
    }

    //ecercicio:
    //criar uma função para calcular o imc, receber dois parametros double peso e double altura, fazer as condicionais e retornar uma strin --> "bom", "regular","critico"

}