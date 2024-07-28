#include <iostream>

int main() {

  char voules[] {'a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U'};

  char letter; 
  std::cin >> letter;
  bool flag = false;
  
  for(auto voule: voules) {
    if(letter == voule){
      flag = true;
      break;
    }
  }
  flag ? std::cout << "YES\n" : std::cout << "NO\n";
  return 0;
}