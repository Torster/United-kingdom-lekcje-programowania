#include <iostream>
#include <ostream>
#include <cmath>
using namespace std;

int main()
{
double a, b, wynik;
int dzialanie;

cout << "Wybierz dzialanie :" << endl << "1. dodawanie" << endl
<< "2. odejmowanie" << endl
<< "3. mnozenie" << endl << "4. dzielenie" << endl << "5. pierwiastkowanie"
<< endl << "6. potegowanie" << endl <<  endl
<< "Wybierz inna liczbe aby zakonczyc program"
<< endl << endl;
cin >> dzialanie;

switch (dzialanie){
case 1:
cout << endl << "Podaj liczby :" << endl;
cin >> a >> b;
wynik = a + b;
break;
case 2:
cout << endl << "Podaj liczby :" << endl;
cin >> a >> b;
wynik = a - b;
break;
case 3:
cout << endl << "Podaj liczby :" << endl;
cin >> a >> b;
wynik = a * b;
break;
case 4:
cout << endl << "Podaj liczby :" << endl;
cin >> a >> b;
wynik = a / b;
break;
case 5:
cout << endl << "podaj liczbe do spierwiastkowania :" << endl;
cin >> a;
cout <<"podaj stopien pierwiastka :";
cin >> b;
wynik = pow(a,(1/b));
break;
case 6:
cout << endl << "podaj liczbe do spotegowania :";
cin >> a;
cout << endl << "do ktorej potegi ma byc podniesiona liczba:";
cin >> b;
wynik = pow(a,b);
break;
default :
cout << endl << "Koniec programu." << endl;
wynik = 0;
}

cout << endl << "Wynik wynosi " << wynik << endl << endl;

system("PAUSE");
return 0;
}
