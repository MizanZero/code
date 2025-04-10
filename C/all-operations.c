#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct student{
	char name[15];
	int rollNo;
};

void main(){
    char name[]="%";
    struct student student1;
    student1.rollNo = 1;
    strcpy(student1.name, name);
    printf("%d\n%s",student1.rollNo,student1.name);
}

