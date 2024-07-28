#pragma once

#include <iostream>
#include <vector>
#include <algorithm>

#include "user.hpp"



class address_book
{
private:
  std::vector<User> users;
  address_book():users(){};
public:
  static address_book& getInstance();
  void print_all_users();
  void add_user(const User &user);
  void delete_user(const User &user);
  void delete_all_users();
  User search_for_user(int id);
  void print_user(const User &user);
  address_book(const address_book&) = delete;
  void operator=(const address_book&) = delete;
};
