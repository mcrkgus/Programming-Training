class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        int p = 0;
        int q = 0;

        for(int i = 0; i < num_list.length; i++) {
            if (num_list[i] % 2 == 0) {
                p++;
            }
            else {
                q++;
            }
        }

        answer[0] = p;
        answer[1] = q;

        return answer;
    }
}
