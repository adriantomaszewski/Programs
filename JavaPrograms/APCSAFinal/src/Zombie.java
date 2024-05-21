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
    public void shout() { // Generic behavior
        System.out.println("I will kill you! I'm a good foe.");
    }
// Getters and setters
    public String getType() {
        return type;
    }

    public void setType(String t) {
        type = t;
    }

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int s) {
        speed = s;
    }

    public int getHealth() {
        return health;
    }

    public void setHealth(int h) {
        health = h;
    }

    public int getBehaviorType() {
        return behaviortype;
    }
    public int getAttackPower() { // Setting attackpower in constructor
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
    
