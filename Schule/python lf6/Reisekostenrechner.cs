using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Klassenarbeit_3_Reisekostenrechner
{
    class Program
    {
        //Deklarieren der Werte 
        public static double Fahrkarte;
        public static double Taxi;
        public static double Frühstück;

        static void Main(string[] args)
        {          
            //Einlesen der Werte
                Console.Write("Preis der Fahrkarte:");
                Fahrkarte = Convert.ToDouble(Console.ReadLine());
                double FahrkarteNetto = Fahrkarte / 1.19;
                Console.Write("Preis für das Taxi:");
                Taxi = Convert.ToDouble(Console.ReadLine());
                double ÜbernachtungNetto = Taxi / 1.07;
                Console.Write("Preis für das Frühstück:");
                Frühstück = Convert.ToDouble(Console.ReadLine());
                double FrühstückNetto = Frühstück / 1.19;
            //Ausgabe der Werte
                Console.WriteLine("Umsatzsteuersumme: " + Fahrkarte_Bahn.Umsatzsteuer(Fahrkarte, Taxi, Frühstück));
                Console.WriteLine("Betriebsausgabe: " + Fahrkarte_Bahn.Betriebsausgabe(Fahrkarte, Taxi));
                Console.ReadLine();

            }
    }
}
