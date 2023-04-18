using System;

public class Charmander
{
    public string Name { get; }
    public string Strength { get; } = "Fire";
    public string Weakness { get; } = "Water";

    public Charmander(string name)
    {
        Name = name;
    }

    public void BattleCry()
    {
        Console.WriteLine(Name + "!");
    }
}

public class Program
{
    static void Main()
    {
        bool quit = false;

        while (!quit)
        {
            Console.WriteLine("Enter a name for your Charmander:");
            string name = Console.ReadLine();
            Charmander charmander = new Charmander(name);

            for (int i = 0; i < 10; i++)
            {
                charmander.BattleCry();
            }

            Console.WriteLine("Do you want to rename your Charmander? (Y/N)");
            string response = Console.ReadLine();

            while (response.ToLower() == "y")
            {
                Console.WriteLine("Enter a new name for your Charmander:");
                name = Console.ReadLine();
                charmander = new Charmander(name);

                for (int i = 0; i < 10; i++)
                {
                    charmander.BattleCry();
                }

                Console.WriteLine("Do you want to rename your Charmander again? (Y/N)");
                response = Console.ReadLine();
            }

            Console.WriteLine("Do you want to quit the game? (Y/N)");
            response = Console.ReadLine();

            if (response.ToLower() == "y")
            {
                quit = true;
            }
        }
    }
}