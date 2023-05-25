public class Charmander : Pokemon
{
    static int hpPerLevel = 15;
    public Charmander(string nickname, int level) : base("Charmander", nickname, "Fire", null, hpPerLevel * level, hpPerLevel * level, level, 0, "Growl")
    {

    }
}