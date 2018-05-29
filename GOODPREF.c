#include <stdio.h>

int main(){
    int tests, n;
    unsigned long long int prefixes;
    scanf("%d", &tests);

    char s[1001];
    while(tests--){
        scanf("%s %d", s, &n);
        prefixes = 0;
        int sum = 0, diff = 0;

        while(n--){
            int increase = 0, j = -1;
            while(s[++j]){
                sum += s[j] == 'a'? 1 : -1;

                if(sum > 0){
                  prefixes++;
                  increase++;
                }
            }

            if(increase == diff){
                prefixes += n*diff;
                break;
            }
            diff = increase;
        }
        printf("%lld\n", prefixes);
    }
}