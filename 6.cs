using System;

namespace Task6
{
    class Program
    {
        // задача 6 

        static void Main()
        {
            int sumKv = 0; //сумма квадратов 
            int kvSum = 0; //квадрат суммы 
            for (var i = 1; i <= 100; i++)
            {
                sumKv = sumKv + i * i;
                kvSum = kvSum + i;
            }
            kvSum = kvSum * kvSum;
            Console.WriteLine(kvSum - sumKv);
        }
    }
}
