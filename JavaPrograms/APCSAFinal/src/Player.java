package APCSAFinal.src;

import java.util.ArrayList;
import java.util.Random;

public class Player {
    private String name;
    private int health;
    private int maxhealth;
    private int attackpower;
    private int speed;
    private ArrayList<Supply> inventory;
    private int rowlocation;
    private int collocation;
    public Player(String n) {
        name = n;
        health = 100;
        maxhealth = 150;
        attackpower = 10;
        speed = 5;
        inventory = new ArrayList<Supply>();
        rowlocation = 0;
        collocation = 4;
    }
    public void move(Player player, char choice) {
        if(player.rowlocation == 5 && choice == 's') {
            System.out.println("Invalid move.");
        }
        else if(player.rowlocation == 0 && choice == 'w') {
            System.out.println("Invalid move.");
        }
        else if(player.collocation == 5 && choice == 'd') {
            System.out.println("Invalid move.");
        }
        else if(player.collocation == 0 && choice == 'a') {
            System.out.println("Invalid move.");
        }
        else if(choice == 'a') {
            collocation--;
        }
        else if(choice == 's') {
            rowlocation++;
        }
        else if(choice == 'w') {
            rowlocation--;
        }
        else if(choice == 'd') {
            collocation++;
        }
        else {System.out.println("Invalid move.");}
    }
    public int attack(Player player, Zombie z) {
        Random random = new Random();
        z.shout();
        while (player.health > 0 && z.getHealth() > 0) {
            if (random.nextInt(0, 50+z.getSpeed()) <= z.getSpeed()) {
                System.out.println("The " + z.getType() + " has dodged your attack.");
            }
            else {
                z.setHealth(z.getHealth()-attackpower);
                System.out.println("You have attacked zombie for " + attackpower + " damage.");
            }
            if (random.nextInt(0, 50+speed) <= speed) {
                System.out.println(name + " has dodged " + z.getType() + "'s attack.");
            }
            else {
                health = (health-z.getAttackPower());
                System.out.println(z.getType() + " has attacked you for " + getAttackPower() + " damage.");
            }
            System.out.println("You now have " + health + " health. The zombie now has " + z.getHealth() + " health.");
            attack(player, z);
        }
        if (player.health <= 0) {
            return 0;
        }
        if (z.getHealth() <= 0) {
            return 1;
        }
        return -1;
    }
    public void collectSupplies(Player player, Supply supply) {
        supply.collectSupplies(player, supply);
    }
    public void useSupplies(Player player, Supply supply) {
        supply.use(player, supply);
    }
    public void removeInventory(int index) {
        inventory.remove(index);
    }
    public int getRowLocation() {
        return rowlocation;
    }
    public int getColLocation() {
        return collocation;
    }
    public int getHealth() {
        return health;
    }
    public int getMaxHealth() {
        return maxhealth;
    }
    public int getAttackPower() {
        return attackpower;
    }
    public ArrayList<Supply> getInventory() {
        return inventory;
    }
    public void addInventory(Supply supply) {
        inventory.add(supply);
    }
    public void setAttackPower(int atp) {
        attackpower = atp;
    }
    public void setHealth(int h) {
        health = h;
    }
    public void setMaxHealth(int mh) {
        maxhealth = mh;
    }
}
