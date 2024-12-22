namespace class_lab3
{
    class Rectangle : geometricShape, IPrint
    {
        public Rectangle(double h, double w)
        {
            this.Height = h;
            this.Width = w;
        }
        public double Height { get; set; }
        public double Width { get; set; }
        public override double Area()
        {
            return Height * Width;
        }
        public override string ToString()
        {
            return ("Прямоугольник со сторонами " + Height.ToString() + " и " + Width.ToString() + "; площадь: " + this.Area());
        }
    }
}