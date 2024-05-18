package APCSAFinal.src;

public class Zombie {
    private String type;
    private int speed;
    private int health;
    private int behaviortype;
    public Zombie() {
        type = "Normal Zombie";
        speed = 10;
        health = 100;
        behaviortype = 0;
    }
    public void shout() {
        System.out.println("I will kill you! I'm a good foe.");
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public int getBehaviorType() {
        return behaviortype;
    }
    public int getAttackPower() {
        if (behaviortype==0) {
            return 10;
        }
        if (behaviortype==1) {
            return 15;
        }
        if (behaviortype==2) {
            return 5;
        }
        return -1;
    }
    public void setBehaviorType(int behaviortype) {
        this.behaviortype = behaviortype;
    }
    public String toString() {
        return "Zombie";
    }
}
    // utilizes inheritance and polymorphism to create different zombie types with unique behaviors. Behavior could be some thing the zombie says before the fight.
    
