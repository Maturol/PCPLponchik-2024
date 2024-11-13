class Program
{
    static int Main(string[] args)
    {
        double a = 0, b = 0, c = 0;
        double D = -1, root1, root2, root;
        if (args.Length == 3) // если есть аргументы командной строки
        {
           if(double.TryParse(args[0], out a) &&double.TryParse(args[1], out b) && double.TryParse(args[2], out c))
           {
                D = b*b - 4*a*c;
           }
           else
           {
            Console.WriteLine("Коэффициенты должны быть действительными числами!!!");
           }
        }
        else
        {
            while (D < 0)
            {
                while (true)
                {
                    Console.Write("Введите коэффициент A: ");
                    if (double.TryParse(Console.ReadLine(), out a))
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Некорректный ввод!");
                    }
                }
                while (true)
                {
                    Console.Write("Введите коэффициент B: ");
                    if (double.TryParse(Console.ReadLine(), out b))
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Некорректный ввод!");
                    }
                }
                while (true)
                {
                    Console.Write("Введите коэффициент C: ");
                    if (double.TryParse(Console.ReadLine(), out c))
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Некорректный ввод!");
                    }
                }
                D = b*b - 4*a*c;
                if (D < 0)
                {
                    Console.WriteLine("Дискриминант меньше нуля");
                }
            }
        }
        if (D >= 0)
        {
            D = Math.Sqrt(D);
            root1 = (-b + D) / (2 * a);
            root2 = (-b - D) / (2 * a);
            if (root1 >= 0 || root2 >= 0)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.Write("Уравнение имеет следующие корни: ");
                if (root1 >= 0)
                {
                    root = Math.Sqrt(root1);
                    Console.Write("{0}; {1} ", root, -root);
                    if (root1 == root2)
                    {
                        Console.WriteLine("");
                        Console.ResetColor();
                        return 0;
                    }
                }
                if (root2 >= 0)
                {
                    root = Math.Sqrt(root2);
                    Console.Write("{0}; {1} ", root, -root);
                }
                Console.WriteLine("");
                Console.ResetColor();
                return 0;
            }
        }
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("Уравнение не имеет корней");
        Console.ResetColor();
        return 0;
    }
}