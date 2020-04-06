using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AtCoder_Cs
{
    public class Program
    {
        public static void Main()
        {
            decimal[] vs = Console.ReadLine().Split().Select(decimal.Parse).ToArray();
            decimal ans = 0;
            if (vs[1] > 1)
            {
                ans = 1;
            }
            if (vs[0] < vs[1])
            {
                ans = 1 + Math.Ceiling((vs[1] - vs[0]) / (vs[0] - 1));
            }
            Console.WriteLine(  ans);
        }
    }

}
