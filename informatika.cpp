#include <iostream>
using namespace std;

int main() {
  int panjang;
  int lp;
  cout << "berapa panjang sisinya?: "; /* memasukkan berat dalam kg */
  cin >> panjang; // yang tadi diketik dimasukkan ke variabel x
  lp = panjang * panjang * 6;
  cout << "luas permukaan kubus dengan panjang sisi " << panjang << " sama dengan " << lp; /* dijumlahkan dan di print */
  return 0;
}
