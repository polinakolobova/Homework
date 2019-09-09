using System;

namespace Task28
{
    class Program
    {
        // задача 28 

        static void Main()
        {
            int size = 1001;
            int sum = 0;
            int value = 1;
            sum += value;
            for (int i = 2; i < size; i += 2)
                for (int j = 1; j <= 4; j++)
                {
                    value = value + i;
                    sum += value;
                }
            Console.WriteLine(sum);
        }
    }
}