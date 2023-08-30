class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int [2];
        int max_num = array[0];
        int idx = 0;
        for(int i = 1; i < array.length; i++) {
            if(max_num < array[i]) {
                max_num = array[i];
                idx = i;
            }
        }
        answer[0] = max_num;
        answer[1] = idx;
        return answer;
    }
}
