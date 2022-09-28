#include <math.h>
#define PI 3.14159265359
double borwein_c(int n){


    double x_nback = sqrt(2);
    double y_nback = 0;
    double pi_nback = 2 + sqrt(2);
    
    double pi_n, y_n, x_n;
    
    int i = 1;

    printf("%lf\n\n",pi_nback);
    while(i<=n){
        
        x_n = 0.5*(sqrt(x_nback) + ((double)1/(sqrt(x_nback))));
        printf("%lf\n",x_n);

        y_n = ((1+y_nback)*(sqrt(x_nback)))/(x_nback + y_nback);

        pi_n = ((1+x_n)*pi_nback*y_n)/(y_n + 1);


        x_nback = x_n;
        y_nback = y_n;
        pi_nback = pi_n;

        i++;
        
    }
    return pi_n;

}

int main(){

    double papi;

    papi = borwein_c(10);

    printf("Hola: \n ", papi);


    return 0;
}