class Solution {
    public int[] solution(int money) {
        int[] answer = new int[2];
        int coffee = 0;
        int change = 0;
        coffee = money / 5500;
        change = money % 5500;
        answer[0] = coffee;
        answer[1] = change;
        return answer;
    }
}
