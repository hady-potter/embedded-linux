#include <iostream>

// task5: find the even and odd numbers in the array
int main() {
  int arr2[8]{1, 2, 3, 4, 1, 7, 12, 8};
  int evens[8];
  int odds[8];
  [&evens, &odds, &arr2]()
  {
    int j = 0;
    int k = 0;
    for (int i = 0; i < 8; i++)
    {
      (arr2[i] & 1) ? odds[j++] = arr2[i] : evens[k++] = arr2[i];
    }
  }();
}