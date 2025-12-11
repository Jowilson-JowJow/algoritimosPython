//aula do thiago em 10/12/2025 sobre classes em java

package AulasJava_thiago.aulaThiago;

import java.util.Scanner;

public class User {
    //ATRIBUTOS
    public String nome; 
    public String email; //o protected no java é o (_email) no python
    public String senha; //o private no java é o (__senha) no python
    public int status;

    //CONSTRUTOR __init__
    public User(String nome, String email, String senha){
        this.nome = nome;
        this.email = email;
        this.senha = senha;
    }
//void não retorna nada
    public void setNome(String nome){
        this.nome = nome;
    }
    public String getNome(){
        return this.nome;
    }

    public void setEmail(String email){
        this.email = email;
    }
    public String getEmail(){
        return this.nome;
    }

    public void setSenha(String senha){
        this.senha = senha;
    }
    public String getSenha(){
        return this.senha;
    }
    
    public void setStatus(int novo){
        this.status = novo;
    }
    public int getStatus(){
        return this.status;
    }

    public void mostrarDados(){
        System.out.printf("Nome: %s\nEmail: %s\n",this.nome, this.email);
    }

    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);

        User user1 = new User("joão", "joaozinho@gmail.com", "123");
        User user2 = new User("tesman", "tesman@gmail.com", "321");
        System.out.println(user1.getNome());
        String novoNome = scan.nextLine();
        user1.setNome(novoNome);
        System.out.println(user1.getNome());
        System.out.println(user2.getNome());
        user2.setStatus(1);
        int x = user2.getStatus();
        if (x==1){
            System.out.println("Usuario Ativo!!!");
        }
        else{
            System.out.println("Usuario Inativo!!!");
        }

        user1.mostrarDados();
        user2.mostrarDados();


        scan.close();

    }    
}
