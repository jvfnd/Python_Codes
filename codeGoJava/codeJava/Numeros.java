import java.util.Scanner;


public class Numeros {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        int[] numbers = new int[6];
        int sumEven = 0;
        int countOdd = 0;

        System.out.println("Digite 6 números inteiros: ");

        for(int i = 0; i < 6; i++){
            numbers[i] = teclado.nextInt();
        }

        System.out.println("Númeors pares digitados: ");
        for (int num : numbers){
            if(num % 2 == 0){
                System.out.println(num + " ");
                sumEven += num;
            }
        }
        System.out.println();
        System.out.println("Soma dos números pares: " + sumEven);
        System.out.println("Números ímpares digitados: ");
        for (int num : numbers){
            if(num % 2 != 0){
                System.out.println(num + " ");
                countOdd++;
            }
        }
        System.out.println();
        System.out.println("Quantidades de números ímpares: "+ countOdd);

    }
}
