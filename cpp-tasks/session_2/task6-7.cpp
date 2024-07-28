#include <iostream>
#include <algorithm>
#include <cmath>

int main() {

  // task6: Simple Lambda: Write a lambda function to calculate the square of a given number.
  auto my_sqrt = [](int n) { return sqrt(n); };
  int res = my_sqrt(16);
  std::cout << res << std::endl;

  // task7: Sort with Lambda : Use lambda functions to sort an array of integers in ascending and descending order.
  int arr[6]{1222, 325, 454, 12, 6723, 99};
  std::sort(arr, arr + 6, [](const int& a, const int& b){return a < b ;});

  return 0;
}