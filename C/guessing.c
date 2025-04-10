#include <stdio.h>


void main(){
    int ans=2;
    int guess;
    int guesses=3;
    int guessed=0;
    while(guess!=ans && guessed<guesses){
        printf("Enter your guess: ");
        guessed++;
        scanf("%d", &guess);
        printf("\n");
        
        if(guess==ans){
            printf("You guessed it!\n");
        }
        
        }
    }


