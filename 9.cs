﻿using System;

namespace Task9
{
    class Program
    {
        // задача 9 

        static void Main()
        {
            for (var c = 1; c < 1000; c++)
                for (var b = 1; b < 1000; b++)
                    for (var a = 1; a < 1000; a++)
                        if ((a * a + b * b == c * c) && (a < b) && (b < c) && (a + b + c == 1000))
                            Console.WriteLine(a * b * c);
        }
    }
}