package AulasJava_thiago;

import java.util.ArrayList;
import java.util.List;

public class exemplo24_array {
    public static void main(String[] args) {
        List<Double> notas = new ArrayList<>();
        notas.add(7.5);
        notas.add(8.5);
        notas.add(9.5);
        notas.add(4.5);

        int tamanho=notas.size();
        double nota1=notas.get(0);

        System.out.println("tamanho do vetor: "+tamanho);
        System.out.println("1ª Nota: "+nota1);
    }
}
