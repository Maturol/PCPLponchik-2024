namespace class_lab3
{
    class Circle : geometricShape
    {
        public Circle(double R)
        {
            Radius = R;
        }
        public double Radius { get; set; }
        public override double Area()
        {
            return Math.PI * Radius * Radius;
        }
        public override string ToString()
        {
            return ("Круг с радиусом " + Radius.ToString() + "; площадь: " + this.Area());
        }
    }
}