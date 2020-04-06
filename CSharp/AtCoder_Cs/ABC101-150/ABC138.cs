using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AtCoder_Cs
{
    class ABC138
    {

        #region A
        public static void A()
        {
            int a = int.Parse(Console.ReadLine());
            string s = Console.ReadLine();

            if (a >= 3200)
            {
                s = "red";
            }
            Console.WriteLine(s);

        }
        #endregion

        #region B
        public static void B()
        {
            int A = int.Parse(Console.ReadLine());
            var Ns = Console.ReadLine().Split().Select(decimal.Parse).ToArray();
            decimal N2 = 0;
            foreach (var N in Ns)
            {
                N2 += (1 / N);
            }
            Console.WriteLine(1 / N2);
        }
        #endregion

        #region C
        public static void C()
        {

        }
        #endregion

        #region D
        public static void D()
        {

        }
        #endregion

    }
}
