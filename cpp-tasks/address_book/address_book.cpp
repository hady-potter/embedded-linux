#include "address_book.hpp"

address_book& address_book::getInstance()
{
  static address_book INSTANE;
  return INSTANE;
}

void address_book::print_user(const User &user)
{
  std::cout << user.id << "\t\t" << user.name << std::endl;
}

void address_book::print_all_users()
{
  std::cout << "ID\t\tName\n";
  for (auto user : users)
  {
    print_user(user);
  }
  std::cout << "============================\n";
}

void address_book::add_user(const User &user)
{
  users.push_back(user);
}

void address_book::delete_user(const User &user)
{
  auto it = std::find_if(users.begin(), users.end(),[user](const auto& u){ return u.id == user.id; });
  users.erase(it);
}

void address_book::delete_all_users()
{
  users.clear();
}
User address_book::search_for_user(int id)
{
  return *std::find_if(users.begin(), users.end(), [id](const auto& u) { return u.id == id; });
}
