using System;

public class Charmander : Pokemon
{
    static int hpPerLevel = 15;
    public Charmander(string nickname, int level) : base("Charmander", nickname, "Fire", "Water", null, hpPerLevel * level, hpPerLevel * level, level, 0)
    {
        
    }
}

public class Pokemon
{
    public string Name { get; }
    public string Nickname { get; }
    public string Type { get; }
    public string Weakness { get; }
    public string? Item { get; }
    public int HP { get; }
    public int MaxHP { get; }
    public int Level { get; }
    public int ExperiencePoints { get; }
    // no moves yet

    public Pokemon(string name, string nickname, string type, string weakness, string item, int hp, int maxHP, int level, int experiencePoints)
    {
        Name=name;
        Nickname=nickname;
        Type=type;
        Weakness=weakness;
        Item=item;
        HP=hp;
        MaxHP=maxHP;
        Level=level;
        ExperiencePoints=experiencePoints;
    }

    public void BattleCry()
    {
        Console.WriteLine(Nickname + ": Rawr!");
    }

    public Pokeball ReturnPokemon()
    {
        Console.WriteLine(Nickname + ", Come back!");
        return new Pokeball(new Pokemon(Name, Nickname, Type, Weakness, Item, HP, MaxHP, Level, ExperiencePoints));
    }
}

public class Pokeball
{
    public string TypePokeball { get; }
    public Pokemon Pokemon { get; }
    // no moves yet

    public Pokeball(Pokemon pokemon, string typePokeball = "Pokeball")
    {
        Pokemon = pokemon;
        TypePokeball = typePokeball;
    }

    public Pokemon SelectPokemon()
    {
        Console.WriteLine(Pokemon.Nickname + ", I choose you!");
        Pokemon.BattleCry();
        return Pokemon;
    }
}

public class Program
{
    static void Main()
    {

        Console.WriteLine("Enter a name for your Charmander:");
        string name = Console.ReadLine();
        Charmander charmander = new Charmander(name, 5);
        Pokeball pokeball = new Pokeball(charmander);

        for (int i = 0; i < 10; i++)
        {
            Pokemon selected = pokeball.SelectPokemon();
            Pokeball newPokeball = selected.ReturnPokemon();
            pokeball = newPokeball;
        }
        Console.ReadLine();

    }
}