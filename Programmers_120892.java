class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        String[] str = cipher.split("");
        
        for(int i = 0; i < str.length; i++) {
            if ((i+1) % code == 0) {
                answer += str[i];
            }
        }
        return answer;
    }
}
