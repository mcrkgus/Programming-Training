import java.util.Arrays;
class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int idx = 0;
        
        Arrays.sort(numbers);
        idx = numbers.length;
        
        answer = numbers[idx-1] * numbers[idx-2];
        
        return answer;
    }
}
