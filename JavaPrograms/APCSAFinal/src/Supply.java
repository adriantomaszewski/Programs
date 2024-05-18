package APCSAFinal.src;

public class Supply {
    private int type; //0 is health, 1 is sword, 2 is machete
    private String name;
    public Supply() {

    }
    public Supply(int t) {
        type = t;
        if (t==0) {
            name = "Health Pack";
        }
        else if (t==1) {
            name = "Sword";
        }
        else if (t==2) {
            name = "Machete";
        }
        else {name = null;}
    }
    public void collectSupplies(Player player, Supply supply) {
        System.out.println("You have collected "+supply.name+".");
        player.addInventory(supply);
    }
    public void use(Player player, Supply supply) {
        if (supply.type==0) {
            player.setHealth(player.getHealth()+50);
            player.setMaxHealth(player.getMaxHealth()+5);
            if (player.getHealth()>player.getMaxHealth()) {player.setHealth(player.getMaxHealth());}
            System.out.println("You have used a health pack to heal at most 50 healthpoints and increase your max health by 5.");
        }
        else if (supply.type==1) {
            player.setAttackPower(player.getAttackPower()+10);
            System.out.println("You have used a sword to increase your attack power by 10.");
        }
        else if (supply.type==2) {
            player.setAttackPower(player.getAttackPower()+5);
            System.out.println("You have used a machete to increase your attack power by 5.");
        }
        else {
            System.out.print("This location is not a supply. Please try again."); 
        }
    }
    public String toString() {
        return name;
    }
}
