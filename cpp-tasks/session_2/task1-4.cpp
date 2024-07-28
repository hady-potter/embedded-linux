#include <iostream>
#include <algorithm>
#include <cmath>

// task1: max element of array
int get_max_numeber(int* arr, int size) {
  return *std::max_element(arr, arr + size);
}

// task2: search for a number in array
int find_index(int* arr, int size, int key) {
  auto position = std::find(arr, arr + size, key);
  return std::distance(arr, position);
}

// task3: delete number from array
void delete_number_from_array(int* arr, int size, int key) {
  std::remove(arr, arr + size, key);
}

// task4: merge two arrays together
void merge_two_array(int* arr1, int size1, int* arr2, int size2, int*& hole_array, int& size) {
  size = size1 + size2;
  hole_array  = new int[size];
  std::merge(arr1, arr1 + size1, arr2, arr2 + size2, hole_array);
}



int main() {

  int arr[6] { 1222,325,454,12,6723,99 };
  int arr2[8] { 1,2,3,4,1,7,12,8 };
  int* arr3;
  int size;
  // std::cout << get_max_numeber(arr, 6) << std::endl;
  // std::cout << find_index(arr, 6, 12) << std::endl;
  // delete_number_from_array(arr, 6, 12);
  // merge_two_array(arr, 6, arr2, 8, *&arr3, size);

  
  // delete[] arr3;
  return 0;
}