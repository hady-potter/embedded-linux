#include <iostream>
#include <vector>

#include "address_book.hpp"

void menu() {
  std::cout << "\t|  List        | List all users\n";
  std::cout << "\t|  Add         | Add user\n";
  std::cout << "\t|  Delete      | Delete user\n";
  std::cout << "\t|  Delete All  | Delete all users\n";
  std::cout << "\t|  Search      | search for user\n";
  std::cout << "\t|  Close       | Close address book\n";
  std::cout << "What do you want? ";
}

enum cases {
  List = 1,
  Add,
  Delete,
  Delete_all,
  Search,
  Close
};

cases hash(std::string option) {
  if(option == "List") return List;
  if(option == "Add") return Add;
  if (option == "Delete") return Delete;
  if (option == "Delete_all") return Delete_all;
  if(option == "Search") return Search;
  return Close;
}

int main() {
  auto& ad = address_book::getInstance();
  bool flag = true;
  while (flag)
  {
    menu();
    std::string answer;
    std::cin >> answer;
    int option = hash(answer);

    switch (option)
    {
    case List:
      ad.print_all_users();
      break;

    case Add:{
      std::cout << "[id, name]\n";
      int id;
      std::string name;
      std::cin >> id >> name;
      ad.add_user(User(id, name));
      break;
    };

    case Delete: {
      std::cout << "ID: ";
      int id;
      std::cin >> id;
      ad.delete_user(User(id, ""));
      break;
    }
    case Delete_all:
      ad.delete_all_users();
      std::cout << "All users are deleted.\n";
      break;
    case Search: {
      std::cout << "ID: ";
      int id;
      std::cin >> id;
      User u = ad.search_for_user(id);
      ad.print_user(u);
      break;
    }
    case Close:
    flag = false;
    break;

    default:
    std::cout << "Invalid option\n";
      break;
    }

  }
  
  
  return 0;
}