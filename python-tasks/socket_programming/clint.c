#include <stdio.h> // printf
#include <sys/types.h> // socket, send, recv
#include <sys/socket.h> //socket, send, recv
#include <netinet/in.h> // sockaddr_in
#include <arpa/inet.h> // inet_addr

#include <stdlib.h> // exit
#include <string.h> // memset
#include <unistd.h> // close

#include <string.h>

#define IP "127.0.0.1"
#define PORT 3000

int main() {

  // 1) create socket
  int sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if(sockfd == -1) {
    printf("can NOT create socket!!!\n");
    exit(1);
  }


  // 2) connect to some server
  struct sockaddr_in sockAddress;

  memset(&sockAddress, 0, sizeof(sockAddress));
  sockAddress.sin_family = AF_INET;
  sockAddress.sin_addr.s_addr = inet_addr(IP);
  sockAddress.sin_port = htons(PORT);

  if (connect(sockfd, (struct sockaddr *)&sockAddress, sizeof(sockAddress)) != 0)
  {
    printf("can NOT connect with -> [%s:%d]\n", IP, PORT);
    exit(2);
  }
  
  
  // 3) send to that server
  char buffer[4096];
  printf("msg: ");
  fgets(buffer, 1024, stdin);
  send(sockfd, buffer, strlen(buffer), 0);

  // 4) recv from that server 
  memset(&buffer, 0, sizeof(buffer));
  recv(sockfd, buffer, sizeof(buffer), 0);
  printf("[server] %s", buffer);

  close(sockfd);
  return 0;
}