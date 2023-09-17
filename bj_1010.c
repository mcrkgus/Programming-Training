#include<stdio.h>
#include<stdlib.h>

double fac(int m)
{
	if(m==0)
		return 1;
	return m * fac(m-1);
}
double C(int m, int n)
{
	return fac(m) / (fac(m-n)*fac(n));
}
int main()
{
	int cnt = 0;
	int n_site=0;
	int m_site=0;
	scanf("%d", &cnt);

	for(int i=0; i<cnt; i++) {
		scanf("%d %d", &n_site, &m_site);
		printf("%.lf\n", C(m_site, n_site));

	}
	return 0;
}
