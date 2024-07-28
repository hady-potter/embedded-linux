#include <iostream>
#include <bitset>

int main()
{
  std::cout << "Enter dicimal number: ";
  short int x;
  std::cin >> x;
  std::cout << "Binry: " << std::bitset<8>(x) << std::endl;

  std::cout << "Enter binary number: ";
  std::bitset<8> y;
  std::cin >> y;
  std::cout << "Dicimal: " << std::dec << y.to_ulong() << std::endl;

  return 0;
}