int a = 3;
float b = 0.3;

float square (float x) {
	return x * x;
}

int main () {
	float c = a / b;
	c /= 3 * (2 - b) + 4;
	return 0;
}