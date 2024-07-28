#pragma once
#include <iostream>

class User{
public:
  int id;
  std::string name;
  User(int id, std::string name) :id(id), name(name){};
  void operator==(const User& u) { id == u.id; };

};


