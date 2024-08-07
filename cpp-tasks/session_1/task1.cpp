#include <iostream>
#include <iomanip>

/* TASK 1
+------+--------+
| CHAR | ASCII  |
+------+--------+
|  a   |   97   |
|  b   |   98   |
|  c   |   99   |
|  d   |  100   |
|  e   |  101   |
|  f   |  102   |
|  g   |  103   |
|  h   |  104   |
|  i   |  105   |
|  j   |  106   |
|  k   |  107   |
|  l   |  108   |
|  m   |  109   |
|  n   |  110   |
|  o   |  111   |
|  p   |  112   |
|  q   |  113   |
|  r   |  114   |
|  s   |  115   |
|  t   |  116   |
|  u   |  117   |
|  v   |  118   |
|  w   |  119   |
|  x   |  120   |
|  y   |  121   |
|  z   |  122   |
+------+--------+
*/

int main()
{

  std::cout << "+------+--------+\n";
  std::cout << "| CHAR | ASCII  |\n";
  std::cout << "+------+--------+\n";

  for (char i = 'a'; i <= 'z'; i++)
  {
    std::cout << "|  " << i << "   |  ";
    std::cout << std::setw(3);
    std::cout << (int)i;
    std::cout << "   |\n";
  }
  std::cout << "+------+--------+\n";
}