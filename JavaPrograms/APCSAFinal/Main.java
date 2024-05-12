package APCSAFinal;

public class Main {
    public final Object[][] map = {{new Zombie(),0,0,0,0,0},
                                   {0,0,0,0,0,0},
                                   {0,0,0,0,0,0},
                                   {0,0,0,0,0,0},
                                   {0,0,0,0,0,0},
                                   {0,0,0,0,0,0}};
    public static void main(String[] args) {
        Player player1 = new Player();
        player1.attack();
    }
}
