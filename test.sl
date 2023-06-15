function main (): void { 
   string res = "tes";
   res = "s";
   int a = 0;
   a = 10;
   int r = 0;
   r = sum(10, a);
   if(r < 10){
      print(r);
   } else if (a == r) {
      print(a);
   } else if (res > 10) {
      print(res);
   } else {
      print("teste");
   }
}

function sum(x: int, y: int): int {
   int sum = x + y;
   return x;
}