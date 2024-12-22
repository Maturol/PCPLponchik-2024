using System.ComponentModel.Design;

namespace class_lab3
{
    abstract class geometricShape: IPrint, IComparable
    {
        public abstract double Area();
        public abstract string ToString();
        public void Print()
        {
            Console.WriteLine(this.ToString());
        }
        public int CompareTo(object? obj)
        {
            if (obj is geometricShape shape) return Area().CompareTo(shape.Area());
            else throw new ArgumentException("бла бла бла: ");
        }
    }
}