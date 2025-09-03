/*
=> Variables are containers for storing data values, like numbers and characters.

-> int: stores integers (whole numbers), without decimals, such as 123 or -123

-> float: stores floating point numbers, with decimals, such as 19.99 or -19.99

-> double: stores big integers and floting value.

-> char: stores single characters, such as 'a' or 'B'. Characters are surrounded by single quotes
*/



#include<stdio.h>

int main(){
    int i = 5;
    float f = 6.0;
    double d = 30.5;
    char ch = 'a';
    char s[]= "Sharafat Hossain"; //this is character string in c.

    printf("Name: %s\n",s);
    printf("Double: %.2f\n",d);

    //Now change value
    d = f;
    printf("Change value of d is: %.2f\n", d);

    //Another way to change value
    i=9;
    printf("Change value of i is: %d/n",i);
}