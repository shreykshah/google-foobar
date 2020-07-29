//FAILING
//not sure why - returns same values as .py
//may be too slow
public class fuel_injection_perfection {
  public static void main(String args[]) {
    // fuel_injection_perfection a = new fuel_injection_perfection();
    // System.out.println(a.solution(4));
    // System.out.println(a.solution(15));
    for (int i = 1; i < 1000; i++) {
      System.out.println(i + " " + solution(Integer.toString(i)));
    }

  }

  public int solution1(int n) {
    //assume positive integer input
    int i = 0;
    while (n > 1) {
      if ((n & 1) == 0)
        n = n >>> 1;
      else if ((n & 4) == 1 || n == 3)
        n = n - 1;
      else
        n = n + 1;
      i++;
    }
    return i;
  }

  public static int solution(String x) {
    //input will be positive integer given as a String
    int pellets = Integer.parseInt(x);
    // System.out.println("------------------");
    // int x1 = Integer.parseInt("111",2);
    // System.out.println(Integer.toBinaryString(x1-2));
    // System.out.println(Integer.toBinaryString(x1-1));
    // System.out.println(Integer.toBinaryString(x1));
    // System.out.println(Integer.toBinaryString(x1+1));
    // System.out.println(Integer.toBinaryString((x1+1)&x1));
    // System.out.println(Integer.toBinaryString((x1-2)&(x1-1)));
    // System.out.println(((x1+1)&x1) > ((x1-2)&(x1-1)));
    // System.out.println("------------------");
    // System.out.println(pellets);
    //counter for num steps taken
    int i = 0;
    while (pellets > 1) {
        //if even, bitshift down (divide by 2)
        if ((pellets & 1) == 0) {
            // System.out.println("/2");
            pellets = pellets >>> 1;
        //if last 2 bits are '01', subtraction is better
      }else if ((pellets & 3) == 1 || pellets == 3) {
            // System.out.println("-1");
        // else if ((pellets&(pellets+1) > ((pellets-1)&(pellets-2))) || pellets == 3)
            pellets--;
        //if last 2 bits are '11', addition is better
      } else {
            // System.out.println("+1");
            pellets++;
}
        i++;
    }
    return i;
}

}
