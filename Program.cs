using System.Collections;

namespace class_lab3
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                #region создание геометрических фигур
                Rectangle myRect = new Rectangle(2, 5);
                myRect.Print();
                Square mySquare = new Square(5);
                mySquare.Print();
                Circle myCircle = new Circle(5);
                myCircle.Print();
                #endregion

                #region создание коллекции класса ArrayList
                Console.WriteLine("\nСоздание коллекции ArrayList и сортировка");
                ArrayList shapesArr = [myCircle, myRect, mySquare];
                shapesArr.Sort();
                foreach (object obj in shapesArr)
                {
                    if (obj is geometricShape)
                    {
                        geometricShape res = (geometricShape)obj;
                        res.Print();
                    }
                }
                #endregion

                #region создание коллекции класса List
                Console.WriteLine("\nСоздание коллекции List и сортировка");
                List<geometricShape> shapesList = [myRect, myCircle, mySquare];
                shapesList.Sort();
                foreach (geometricShape gs in shapesList)
                {
                    gs.Print();
                }
                #endregion

                #region работа с матрицей
                SparseMatrix MyMatrix = new SparseMatrix(5, 5);
                MyMatrix.AddElement(90, 50, 2);
                MyMatrix.AddElement(1, 1, 2);
                MyMatrix.AddElement(1, 4, 3);
                MyMatrix.AddElement(5, 5, 8);

                MyMatrix.PrintElements();
                Console.WriteLine(MyMatrix.ToString());
                #endregion

                #region работа со стеком
                var myStack = new SimpleStack<geometricShape>();
                myStack.PrintElements();
                myStack.Push(myRect);
                myStack.Push(mySquare);
                myStack.Push(myCircle);

                myStack.PrintElements();
                myStack.Pop();
                myStack.PrintElements();
                #endregion
            }
            catch (Exception ex) {Console.WriteLine("Ошибка: " + ex.Message);}
        }
    }
}