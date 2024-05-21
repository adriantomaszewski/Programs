package APCSAFinal.src;

public class WeakZombie extends Zombie {
    public WeakZombie() {
        setType("Weak Zombie");
        setSpeed(5);
        setHealth(50);
        setBehaviorType(2);
    }
    public void shout() { // Different behavior method
        System.out.println("I will kill you! I'm an ok foe.");
    }
    public String toString() {
        return "Weak Zombie";
    }
}
