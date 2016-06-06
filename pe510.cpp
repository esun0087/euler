#include <iostream>
#include <set>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

typedef long long LL;

void output_log()
{
	LL n = 1000000000L;
    //LL n = 100L;
	ofstream fout("log.txt");
	for (LL k = 1; ; k++)
	{
		bool tag = true;
		for (LL p = 1; k * p <= n && k * p * p <= n; p++)
		{
			for (LL q = p; k * p * p * q <= n && 
                        k * p * p * q * q <= n && 
                        k * p * p * (p + q) <= n && 
                        k * p * p * (p + q) * (p + q) <= n && 
                                    k * q * q * (p + q) <= n &&
                                    k * q * q * (p + q) * (p + q) <= n; ++q)
			{
				LL ra = k * p * p * (p + q) * (p + q);
				LL rb = k * q * q * (p + q) * (p + q);
				LL rc = k * p * p * q * q;
				tag = false;
				if (ra <= rb && rb <= n)
				{
					fout << ra << " " << rb << " " << rc << "\n";
				}
			}
		}
		if (tag)
			break;
	}
	fout.close();
}

void f()
{

	set<string> exist_s;
	ifstream fin("log.txt");
	ofstream fout("0.txt");
	string s;
	int len = 0;
	while (getline(fin, s))
	{
		len++;
	}
	cout << len << endl;
	fin.close();
	fin.open("log.txt");
	int i = 0;
	while (getline(fin, s))
	{
		if (exist_s.size() > 30000000)
		{
			fout.close();
			char file_name[1024];
			i++;
			sprintf(file_name, "%d.txt", i);
			fout.open(file_name);
			exist_s.clear();
		}
		if (exist_s.find(s) == exist_s.end())
		{
			exist_s.insert(s);
			fout << s << "\n";
		}
	}
}
int main()
{
	output_log();
	set<string> exist_s;
	ifstream fin("log.txt");
	string s;
	while (getline(fin, s))
		exist_s.insert(s);
	LL sum = 0;
    LL n = 1000000000L;
	for (set<string>::iterator p = exist_s.begin(); p != exist_s.end(); ++p)
	{
		stringstream ss;
		ss << *p;
		LL a, b, c;
		ss >> a;
		ss >> b;
		ss >> c;
        if (a <= n && b <= n && c <= n)
            sum += a + b + c;
	}
	cout << sum << endl;

}