namespace class_lab3
{
    class Square : Rectangle
    {
        public Square(double a) : base(a, a) {}
        public override string ToString()
        {
            return ("Квадрат со стороной " + Height.ToString() + "; площадь: " + this.Area());
        }
    }
}