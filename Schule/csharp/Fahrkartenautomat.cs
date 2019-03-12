using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fahrkartenautomat
{
    class Program
    {
        static void Main(string[] args)
        {
            //Deklarieren 
            int betrag;
            double betrag1;
            int gezahlt;
            double gezahlt1;
            int rückgeld;
            int anz20_er;
            int anz10_er;
            int anz5_er;
            int anz2_er;
            int anz1_er;
            int anz050_er;
            int rest;

            //Programmname
            Console.WriteLine("Ihr Rückgeld Bimbo");

            //Werte eingabe
            Console.Write("Bitte den Betrag der Fahrkarte angeben: ");
            betrag1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Bitte den gezahlten Betrag angeben: ");
            gezahlt1 = Convert.ToDouble(Console.ReadLine());

            //Umrechnen in Int32 
            betrag = Convert.ToInt32(betrag1 * 100);

            gezahlt = Convert.ToInt32(gezahlt1 * 100);

            //If Abfrage zur Prüfung der Beträge 
            //if ((betrag >= 2000) && (betrag <= 500))
                rückgeld = gezahlt - betrag;
            //else
                //Console.WriteLine("Bitte einen gültigen Betrag angeben!");
                //rückgeld = 0; 
   
            //Rechnen des Rückgeldes
            anz20_er = rückgeld / 2000;
            rest = rückgeld % 2000;

            anz10_er = rest / 1000;
            rest = rest % 1000;
            
            anz5_er = rest / 500;
            rest = rest % 500;

            anz2_er = rest / 200;
            rest = rest % 200;

            anz1_er = rest / 100;
            rest = rest % 100;

            anz050_er = rest / 50;

            //Zurück rechnen 
            rückgeld = rückgeld / 100;

            //Ausgabe Ergebnis
            Console.WriteLine(" ");

            Console.WriteLine("Ihr Rückgeld beträgt: " + rückgeld);
            Console.WriteLine(" ");
            Console.WriteLine("Diese Scheine bekommen Sie zurück.");
            Console.WriteLine("Die Anzahl der 20er    beträgt: " + anz20_er);
            Console.WriteLine("Die Anzahl der 10er    beträgt: " + anz10_er);
            Console.WriteLine("Die Anzahl der  5er    beträgt: " + anz5_er);
            Console.WriteLine(" ");
            Console.WriteLine("Dies bekommen Sie an Münzen zurück.");
            Console.WriteLine("Die Anzahl der  2er    beträgt: " + anz2_er);
            Console.WriteLine("Die Anzahl der  1er    beträgt: " + anz1_er);
            Console.WriteLine("Die Anzahl der  0,50er beträgt: " + anz050_er);

            Console.ReadLine();
        }
    }
}
