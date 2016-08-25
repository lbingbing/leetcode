class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        sort(ransomNote.begin(),ransomNote.end());
        sort(magazine.begin(),magazine.end());
        int len1 = ransomNote.size();
        int len2 = magazine.size();
        int i = 0;
        int j = 0;
        while(i<len1 && j<len2){
            if(ransomNote[i]==magazine[j]){
                i++;
                j++;
            }else if(ransomNote[i]>magazine[j]){
                j++;
            }else{
                break;
            }
        }
        return i==len1;
    }
};
