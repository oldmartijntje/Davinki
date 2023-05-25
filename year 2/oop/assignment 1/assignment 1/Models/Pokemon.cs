public class Pokemon
{
    public string Name { get; }
    public string Nickname { get; set; }
    public string Type { get; }
    public string? Item { get; set; }
    public int HP { get; set; }
    public int MaxHP { get; set; }
    public int Level { get; set; }
    public int ExperiencePoints { get; set; }
    public string Sound { get; }
    static int HpPerLevel = 1;
    // no moves yet

    public Pokemon(string name, string? nickname, string type, string item, int hp, int maxHP, int level, int experiencePoints, string sound)
    {
        Name = name;
        if (nickname == null || nickname == "")
        {
            Nickname = Name;
        } else
        {
            Nickname = nickname;
        }
        Type = type;
        Item = item;
        HP = hp;
        MaxHP = maxHP;
        Level = level;
        ExperiencePoints = experiencePoints;
        Sound = sound;
    }

    public void BattleCry()
    {
        Console.WriteLine(Nickname + ": " + Sound + "!");
    }

   
}