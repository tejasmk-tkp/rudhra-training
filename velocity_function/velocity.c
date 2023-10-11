#include <stdio.h>
#define N 10000

float vel(int rate, int time ) {
	float v = 0, a = 0;
	
	for (int i = 0; i <= N; i++) {
		float time = (float) i/N;
		a = rate*time*time;
		v += a * (time/(float)N);
	}
	return v;

}

void main() {
	
	float v = vel(4, 5);
	printf("%.2f", v);
}
