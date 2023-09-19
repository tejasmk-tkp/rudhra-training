#include <stdio.h>
#define N 1000

float vel(int rate, int time ) {
	float v = 0, a = 0;
	
	for (int i = 0; i <= N; i++) {
		float time = (float) i/N;
		a = rate*time*time;
		v += a * (time/(float)N);
	}
	return v;

}

int main() {return 0;}
