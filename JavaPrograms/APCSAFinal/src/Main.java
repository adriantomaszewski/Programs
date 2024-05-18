package APCSAFinal.src;
import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Supply Health = new Supply(0);
        Supply Sword = new Supply(1);
        Supply Machete = new Supply(2);
        Zombie StrongZombie = new StrongZombie();
        Zombie WeakZombie = new WeakZombie();
        Zombie Zombie = new Zombie();
        Scanner scanner = new Scanner(System.in);
        boolean gamestate = true;
        Object[][] map = {{Health,Health,Sword,Health,"Nothing",StrongZombie},
                          {StrongZombie,"Nothing",Sword,Zombie,Health,"Nothing"},
                          {Zombie,Health,Machete,Sword,"Nothing","Exit"},
                          {Health,Machete,WeakZombie,"Nothing",Zombie,StrongZombie},
                          {Health,"Nothing",StrongZombie,"Nothing","Nothing",WeakZombie},
                          {"Nothing",Sword,Health,Zombie,"Nothing",Sword}};
        System.out.println("Type out the name you'd like to have for your protagonist.");
        Player player1 = new Player(scanner.nextLine());
        while (gamestate == true) {
            if (map[player1.getRowLocation()][player1.getColLocation()] instanceof String) {
                if(map[player1.getRowLocation()][player1.getColLocation()].equals("Exit")) {
                    System.out.println("You have reached the exit and won!");
                    gamestate = false;
                    break;
                }
            }
            if (map[player1.getRowLocation()][player1.getColLocation()] instanceof Supply || map[player1.getRowLocation()][player1.getColLocation()] instanceof Zombie) {
                System.out.println("You are at " + player1.getHealth() + "HP, have " + player1.getAttackPower() + " attack power, and have an inventory of " + player1.getInventory() + ". At your location is a " + map[player1.getRowLocation()][player1.getColLocation()].toString() +  ". Would you like to collect supplies, attack, use supplies, or move. (Enter 0, 1, 2, or 3 corresponding to your chioce.)");
            }
            else if (map[player1.getRowLocation()][player1.getColLocation()] instanceof String) { 
                System.out.println("You are at " + player1.getHealth() + "HP, have " + player1.getAttackPower() + " attack power, and have an inventory of " + player1.getInventory() + ". At your location is a " + map[player1.getRowLocation()][player1.getColLocation()] +  ". Would you like to collect supplies, attack, use supplies, or move. (Enter 0, 1, 2, or 3 corresponding to your chioce.)");
            }
            else {System.out.println("Error.");}
            try {
                int choice = scanner.nextInt();
                scanner.nextLine();
                if (choice == 0) {
                    try {
                        player1.collectSupplies(player1, (Supply) map[player1.getRowLocation()][player1.getColLocation()]);
                        map[player1.getRowLocation()][player1.getColLocation()] = "Nothing";
                    }
                    catch(Exception E) {
                        System.out.println("There are no supplies at your location.");
                    }
                }
                else if (choice == 1) {
                    if (!(map[player1.getRowLocation()][player1.getColLocation()] instanceof Zombie)) {
                        System.out.println("There is no zombie here! Please do another action.");
                    }
                    else if (player1.attack(player1, (Zombie) map[player1.getRowLocation()][player1.getColLocation()]) == 0) {
                        System.out.println("You have died.");
                        gamestate=false;
                    }
                    else if (player1.attack(player1, (Zombie) map[player1.getRowLocation()][player1.getColLocation()]) == 1) {
                        map[player1.getRowLocation()][player1.getColLocation()] = "Nothing";
                        WeakZombie.setHealth(50);
                        Zombie.setHealth(100);
                        StrongZombie.setHealth(150);
                        System.out.println("You have defeated the zombie.");
                    }
                    else {System.out.println("Error.");}
                }
                else if (choice == 2) {
                    try {
                        System.out.println("From which slot would you like to use your supply. You have an inventory of " + player1.getInventory() + ". (Starts at 0)");
                        int indexchosen = scanner.nextInt();
                        player1.useSupplies(player1, (Supply) player1.getInventory().get(indexchosen));
                        player1.removeInventory(indexchosen);
                    }
                    catch(Exception E) {
                        System.out.println("You have selected an out of bounds supply.");
                    }
                }
                else if (choice == 3) {
                    if (map[player1.getRowLocation()][player1.getColLocation()] instanceof Zombie) {
                        System.out.println("You cannot move out of a zombie fight! Choose again.");
                    }
                    else {
                        System.out.println("Which direction would you like to move? Use w, a, s, or d.");
                        String input = scanner.nextLine();
                        player1.move(player1, input.charAt(0));
                    }
                }
                else {
                    System.out.println("Invalid choice!");
                }
            }
            catch (Exception e) {
                System.out.println("Invalid choice.");
                scanner.nextLine();
            }
        }
        scanner.close();   
    }
}