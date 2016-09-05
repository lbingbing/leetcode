class Solution {
public:
    string intToRoman(int num) {
        string res;
        switch((num/1000)%10){
            case 1: res += "M";   break;
            case 2: res += "MM";  break;
            case 3: res += "MMM"; break;
        }
        switch((num/100)%10){
            case 1: res += "C";    break;
            case 2: res += "CC";   break;
            case 3: res += "CCC";  break;
            case 4: res += "CD";   break;
            case 5: res += "D";    break;
            case 6: res += "DC";   break;
            case 7: res += "DCC";  break;
            case 8: res += "DCCC"; break;
            case 9: res += "CM";   break;
        }
        switch((num/10)%10){
            case 1: res += "X";    break;
            case 2: res += "XX";   break;
            case 3: res += "XXX";  break;
            case 4: res += "XL";   break;
            case 5: res += "L";    break;
            case 6: res += "LX";   break;
            case 7: res += "LXX";  break;
            case 8: res += "LXXX"; break;
            case 9: res += "XC";   break;
        }
        switch(num%10){
            case 1: res += "I";    break;
            case 2: res += "II";   break;
            case 3: res += "III";  break;
            case 4: res += "IV";   break;
            case 5: res += "V";    break;
            case 6: res += "VI";   break;
            case 7: res += "VII";  break;
            case 8: res += "VIII"; break;
            case 9: res += "IX";   break;
        }
        return res;
    }
};
