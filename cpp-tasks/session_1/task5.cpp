#include <iostream>


int main() {
  int j = 1;
  while ( j++ < 6)
  {
    for (int i = 1; i < 13; i++)
    {
      std::cout << i << " * " << j << " = " << i * j << std::endl;
    }
    std::cout << "===================\n";
  }
  
  

  return 0;
}