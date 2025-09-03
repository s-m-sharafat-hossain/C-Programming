/*
=> Formate Spacifires: used with in printf() function to tell compiler of data the variable is storing. It is basically a placeholder for the variable value.

-> int	                        %d or %i	    printf("%d", 10); → 10
-> float	                        %f	        printf("%f", 3.14); → 3.140000
-> double	                        %lf	        printf("%lf", 3.14159);
-> char	                            %c	        printf("%c", 'A'); → A
-> string	                        %s	        printf("%s", "Hello"); → Hello
-> pointer	                        %p	        printf("%p", ptr);

->How many number take after decimal specifie like      %.2f or %.3f
*/

#include<stdio.h>
#include<string.h>

int main(){
    int a = 5;
    float f = 4.55;
    double d = 445.3234;
    char c = 'C';
    char s[] = "String Here";

    printf("Integer: %d\n", a);
    printf("Float: %f\n", f);
    printf("Double: %lf\n", d);
    printf("Character: %c\n", c);
    printf("String: %s\n", s);
    printf("Fixed decimal: %.2f\n", d);
}