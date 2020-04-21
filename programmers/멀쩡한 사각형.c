#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 3x + 2y = 24
// 3x + 2y <= 24

long casting(long i, long j)
{
    if(j == 0)
        return i;
    
    else
        return casting(j, i%j);
}

long solution(int w, int h) {
    long answer = 0;
    long W = (long) w;
    long H = (long) h;
    
    long sol = W < H ? casting(H, W) : casting(W, H);
    long ans = (W * H) / sol;
    long delta = (H / sol);
    
    // h * x + w * y <= h * w
    for(int i = 0; (i + 1) < w; i++)
    {
        long foo = ans - delta * (i + 1);
        answer += foo / (W / sol);
    }
    
    return answer * 2;
}