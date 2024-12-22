namespace class_lab3
{
    class ElementOfList<Typ>
    {
        public ElementOfList(Typ val)
        {
            Value = val;
            Next = null;
        }
        public Typ Value { get; set; }
        public ElementOfList<Typ>? Next { get; set; }
    }

    class SimpleStack<Typ>
    {
        public SimpleStack()
        {
            Element = null;
        }
        public ElementOfList<Typ>? Element { get; set; }
        public void Push(Typ elem)
        {
            ElementOfList<Typ> tempElem = new ElementOfList<Typ>(elem);
            if (Element == null)
            {
                Element = tempElem;
            }
            else
            {
                tempElem.Next = Element;
                Element = tempElem;
            }
        }

        public void Pop()
        {
            if (Element != null)
            {
                Element = Element.Next;
            }
        }

        public void PrintElements()
        {
            var temp = Element;
            Console.WriteLine("Стек: ");
            if (temp == null) Console.WriteLine("Стек пуст");
            else
            {
                while (temp != null)
                {
                    Console.WriteLine(temp.Value.ToString());
                    temp = temp.Next;
                }
            }
        }
    }
}