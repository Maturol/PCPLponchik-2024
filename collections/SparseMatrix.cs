namespace class_lab3
{
    class MatrixElement : IComparable
    {
        public MatrixElement(int x, int y, int elm)
        {
            X = x;
            Y = y;
            Value = elm;
        }
        public int X { get; set; }
        public int Y { get; set; }
        public int Value { get; set; }
        public int CompareTo(object? obj)
        {
            if (obj is MatrixElement elm1)
            {
                if (this.Y > elm1.Y) return 1;
                else if (this.Y < elm1.Y) { return -1; }
                else if (this.X == elm1.X) { throw new ArgumentException("Разные элементы с совпадающими позициями"); }
                else return this.X.CompareTo(elm1.X);
            }
            else throw new ArgumentException("Некорректный тип элемента");
        }

    }

    class SparseMatrix
    {
        public SparseMatrix(int X, int Y)
        {
            dimX = X;
            dimY = Y;
            Elements = new List<MatrixElement>();
        }
        public int dimX { get; set; }
        public int dimY { get; set; }
        public List<MatrixElement> Elements { get; set; }
        public void AddElement(int x, int y, int val)
        {
            if (x < 0 || y < 0 || (x > this.dimX) || (y > this.dimY))
                Console.WriteLine("Элемент выходит за пределы матрицы");
            else
            {
                Elements.Add(new MatrixElement(x, y, val));
                Elements.Sort();
            }
        }
        public void PrintElements()
        {
            Console.WriteLine("\nМатрица " + this.dimY + " X " + this.dimX);
            foreach (MatrixElement elm in Elements)
            {
                Console.WriteLine("Элемент на позиции X = " + elm.X + ", Y = " + elm.Y + " имеет значение " + elm.Value);
            }
        }
        public override string ToString()
        {
            string res = "";
            int jNum = 0;
            for (int j = 0; j < this.dimY; j++)
            {
                for (int i = 0; i < this.dimX; i++)
                {
                    if (Elements.Count == 0 || Elements.Count <= jNum || !(Elements[jNum].X == i + 1 && Elements[jNum].Y == j + 1)) res = res + "0 ";
                    else
                    {
                        res = res + Elements[jNum].Value + " ";
                        jNum++;
                    }
                }
                res = res + "\n";
            }
            return res;
        }
    }
}