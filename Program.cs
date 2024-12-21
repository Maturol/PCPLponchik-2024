namespace class_lab2
{
    class Program
    {
        static void Main(string[] args)
        {
            Rectangle a = new Rectangle(2, 5);
            a.Print();
            Square b = new Square(5);
            b.Print();
            Circle c = new Circle(5);
            c.Print();
        }
    }
}
