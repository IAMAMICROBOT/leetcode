#include<math.h>
bool isPowerOfFour(int n) {
    for(int i=0;i<17;i++){
        if (n==pow(4,i))
            return true;
    }
    return false;
}
