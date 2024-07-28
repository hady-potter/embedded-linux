#include <iostream>
#include <math.h>

int main() {

  int a = 3;
  int b = 4;
  int c = 5;
  if(c == (sqrt(a * a + b * b)) ) {
    std::cout << "YES\n";
  } else std::cout << "NO\n";

  return 0;
}