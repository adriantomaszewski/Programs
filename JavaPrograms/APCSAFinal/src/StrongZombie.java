package APCSAFinal.src;

public class StrongZombie extends Zombie {
    public StrongZombie() {
        setType("Strong Zombie");
        setSpeed(15);
        setHealth(150);
        setBehaviorType(1);
    }
    public void shout() {
        System.out.println("I will kill you! I'm a very strong foe.");
    }
    public String toString() {
        return "Strong Zombie";
    }
}
