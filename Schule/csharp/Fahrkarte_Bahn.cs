using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Klassenarbeit_3_Reisekostenrechner
{
    class Fahrkarte_Bahn
    {
        public static double Umsatzsteuer(double Fahrkarte, double Taxi, double Frühstück)
        {
            double Umsatzsteuer = (Fahrkarte * 0.19) + (Taxi * 0.07) + (Frühstück * 0.19);
            return Umsatzsteuer;
        }

        public static double Betriebsausgabe(double Fahrkarte, double Taxi)
        {
            double Betriebsausgabe = (Fahrkarte / 1.19) + (Taxi / 1.19); 
            return Betriebsausgabe;
        }
    }
}
