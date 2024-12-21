namespace class_lab2
{
    abstract class geometricShape
    {
        public abstract double Area();
        public override abstract string ToString();
        public void Print()
        {
            Console.WriteLine(this.ToString());
        }
    }
}