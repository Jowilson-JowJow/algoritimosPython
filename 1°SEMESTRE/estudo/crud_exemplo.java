package 1°SEMESTRE.estudo;

package crud_exemplo;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Classe que representa o "objeto" que vamos manipular
class Usuario {
    int id;
    String nome;
    String email;

    // Construtor
    Usuario(int id, String nome, String email) {
        this.id = id;
        this.nome = nome;
        this.email = email;
    }

    // Exibir dados de um usuário
    @Override
    public String toString() {
        return "ID: " + id + " | Nome: " + nome + " | Email: " + email;
    }
}

public class CrudUsuarios {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        List<Usuario> usuarios = new ArrayList<>();
        int idCounter = 1; // contador para IDs automáticos

        while (true) {
            System.out.println("\n==== MENU CRUD ====");
            System.out.println("1 - Criar Usuário");
            System.out.println("2 - Listar Usuários");
            System.out.println("3 - Atualizar Usuário");
            System.out.println("4 - Deletar Usuário");
            System.out.println("0 - Sair");
            System.out.print("Escolha: ");
            int opcao = scan.nextInt();
            scan.nextLine(); // consumir quebra de linha

            switch (opcao) {
                case 1: // CREATE
                    System.out.print("Nome: ");
                    String nome = scan.nextLine();
                    System.out.print("Email: ");
                    String email = scan.nextLine();
                    usuarios.add(new Usuario(idCounter++, nome, email));
                    System.out.println("Usuário cadastrado com sucesso!");
                    break;

                case 2: // READ
                    System.out.println("\n--- Lista de Usuários ---");
                    for (Usuario u : usuarios) {
                        System.out.println(u);
                    }
                    break;

                case 3: // UPDATE
                    System.out.print("Digite o ID do usuário a atualizar: ");
                    int idUpdate = scan.nextInt();
                    scan.nextLine();
                    boolean encontradoUpdate = false;
                    for (Usuario u : usuarios) {
                        if (u.id == idUpdate) {
                            System.out.print("Novo Nome: ");
                            u.nome = scan.nextLine();
                            System.out.print("Novo Email: ");
                            u.email = scan.nextLine();
                            System.out.println("Usuário atualizado!");
                            encontradoUpdate = true;
                            break;
                        }
                    }
                    if (!encontradoUpdate) {
                        System.out.println("Usuário não encontrado!");
                    }
                    break;

                case 4: // DELETE
                    System.out.print("Digite o ID do usuário a excluir: ");
                    int idDelete = scan.nextInt();
                    scan.nextLine();
                    boolean removido = usuarios.removeIf(u -> u.id == idDelete);
                    if (removido) {
                        System.out.println("Usuário removido!");
                    } else {
                        System.out.println("Usuário não encontrado!");
                    }
                    break;

                case 0:
                    System.out.println("Saindo do sistema...");
                    scan.close();
                    return;

                default:
                    System.out.println("Opção inválida!");
            }
        }
    }
}
