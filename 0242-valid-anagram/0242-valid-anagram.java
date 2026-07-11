class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> m=new HashMap<>();
        if(s.length()!=t.length())
        {
            return false;
        }
        for(char i:s.toCharArray())
        {
            m.put(i,m.getOrDefault(i,0)+1);
        }
        for(char i:t.toCharArray())
        {
            if(m.containsKey(i))
            {
                m.put(i,m.get(i)-1);
                if(m.get(i)<0)
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        return true;
    }
}