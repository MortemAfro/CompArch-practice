#include <math.h>

double gauss_legendre_c(int n){

    double a_o = 1;
    double b_o = ((double)1/(sqrt(2)));
    double t_o = 0.25;

    double a_n = a_o, a_nplus, t_nplus, b_nplus, pi_nplus;
    double b_n = b_o, t_n=t_o;

    for(int i=0;i<n+1;i++){

        a_nplus = 0.5*(a_n + b_n);
        b_nplus = sqrt(a_n*b_n);

        t_nplus = t_n - (pow(2,i))*pow(a_n-a_nplus,2);

        pi_nplus = (pow(a_nplus+b_nplus,2))/(4*t_nplus);

        a_n = a_nplus;
        b_n = b_nplus;
        t_n = t_nplus;


    }



    return pi_nplus;
}