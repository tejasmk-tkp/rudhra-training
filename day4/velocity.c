#include <stdio.h>
#define N 1000
float vel(int rate, ) {
	float t, v, a;

	printf("Enter time in seconds: ");
	scanf("%d", &t);
	
	for (float i = 0; i <=  t; i += t/N) {
		a = 4*t*t;
		v += a * (t/N);
	}

	printf("v = %f", v);

}
