#include <iostream>
#include <map>
#include <stdlib.h>
#include <string.h>

using namespace  std;


int main()
{
    int n = 400000000;
    unsigned *count_seq = new unsigned[n+10];
    unsigned **seq = new unsigned*[2];
    seq[0] = new unsigned[n+10];
    seq[1] = new unsigned[n+10];
    memset(count_seq, 0, (n+10) * sizeof(unsigned));
    memset(seq[0], 0, (n+10) * sizeof(unsigned));
    memset(seq[1], 0, (n+10) * sizeof(unsigned));
    cout << "new ok" << endl;
    int k = 0;
    seq[k][1] = 1;
    for(unsigned i = 0; i <= n; ++i)
    {
        cout << "iter\t" << i << endl;
        bool tag = false;
        for(int kk = 0; kk <= n; ++kk)
        {
            if(seq[k][kk] == 0)
                continue;
            unsigned x = kk;
            for(unsigned y = 2; y <= n; ++y)
            {
                if(x * y > n)
                    break;
                tag = true;
                unsigned t = x * y;
                seq[1-k][t] += seq[k][x];
                count_seq[t] += seq[k][x];
            }
        }
        if(!tag)
            break;
        memset(seq[k], 0, (n+10) * sizeof(unsigned));
        k = 1-k;
    }
    cout << "cal over" << endl;
    long long ss = 0;
    for(int i = 1; i < n; ++i)
        if(i == count_seq[i])
            {
                cout << i << endl;
                ss += i;
                system("pause");
            }
    cout << ss << endl;
}