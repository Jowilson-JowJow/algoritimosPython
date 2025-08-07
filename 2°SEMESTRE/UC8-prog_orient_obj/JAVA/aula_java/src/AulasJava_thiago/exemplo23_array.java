package AulasJava_thiago;

import java.util.ArrayList;
import java.util.List;

public class exemplo23_array {
   public static void main(String[] args) {
        //cria um array vazio
        List<String> lista_nome = new ArrayList<>();
        
        //adiciona elementos nessa array
        lista_nome.add("Jowilson");//coloca "jowilson" no index 0 ficando assim ("Jowilson")
        lista_nome.add("Ribas");//coloca "Ribas" no index 1 ficando assim ("Jowilson","Ribas")
        lista_nome.add(2,"Nunes");//coloca  "Nunes" no index 2 ficando assim ("Jowilson","Ribas","Nunes")
        System.out.println(lista_nome);
        lista_nome.add(1,"Wellyngton");//insere no index 1 "wellyngton" ficando assim ("Jowilson","Wellyngton","Ribas","Nunes")
        System.out.println(lista_nome);
        int tamaho_lista_nome=lista_nome.size();//da o tamanho do array
        System.out.println(tamaho_lista_nome);
        String nome1 = lista_nome.get(2);
        System.out.println(nome1);

        //remove elementos no array
        lista_nome.remove("Jowilson");//remove o "Jowilson" da array
        System.out.println(lista_nome);
        lista_nome.remove(2);//remove o ques esta no index 2
        System.out.println(lista_nome);
        int tamaho_lista_nome1=lista_nome.size();//da o tamanho do array
        System.out.println(tamaho_lista_nome1);

        String nome2 = lista_nome.get(1);
        System.out.println(nome2);


   } 
}
