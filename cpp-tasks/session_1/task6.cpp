#include <iostream>

int main() {

  // int num;
  std::string num;
  std::cin >> num;

  int sum = 0;
  for(auto n: num) {
    sum += n - '0';
  }

  std::cout << sum << std::endl;
  return 0;
}