#include <iostream>
int main(){
    int m,n;
    std::cin>>m>>n;
    if(m == 1) 
        return 1; 
    else if(n == 1) 
        return m; 
    else { 
        int result = 1, i = 1, j; 
        while(i <= m) { 
            result = 1; 
            for(j = 1; j <= n; j++) { 
                    result *= i; 
            } 
            if(result > m) {std::cout<<i-1<<std::endl; break;}
            i++; 
        } 
    } 
} 
