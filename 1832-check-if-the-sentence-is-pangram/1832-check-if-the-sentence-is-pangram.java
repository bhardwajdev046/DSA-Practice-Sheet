class Solution {
    public boolean checkIfPangram(String sentence) {
//         int size=26;
//         List<Integer> list= new ArrayList<>(Collections.nCopies(size,0));
//         for(int i=0;i<sentence.length();i++)
//         {
//             list.set(sentence.charAt(i)-'a',1);  // -> list[sentence[i]-'a']=1;
//         }
//         for(int j=0;j<26;j++)
//         {
//             if(list.get(j)==0) return false;  // -> list[j]==0;
//         }
//         return true;
//     }
// }

if(sentence.length()<26) return false;
        for(char ch='a';ch<='z';ch++)
        {
            if(sentence.indexOf(ch)<0)  // indexOf(ch) returns the index of the first           occurrence of the character, or -1 if not found.
            {
                return false;
            }
         }
        return true;
    }
}