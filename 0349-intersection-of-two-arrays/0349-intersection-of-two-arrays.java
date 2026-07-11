class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> m=new HashMap<>();
        ArrayList<Integer> res=new ArrayList<>();
        if(nums1.length<nums2.length)
        {
            for(int i:nums1)
            {
                m.put(i,1);
            }
            System.out.println(m);
            for(int i:nums2)
            {
                if(m.containsKey(i) && m.get(i)==1)
                {
                    res.add(i);
                    m.put(i,0);
                }
            }

        }
        else
        {
            for(int i:nums2)
            {
                m.put(i,1);
            }
            //System.out.println(m);
            for(int i:nums1)
            {
                if(m.containsKey(i) && m.get(i)==1)
                {
                    res.add(i);
                    m.put(i,0);
                }
            }

        }
         
        //System.out.println(res);
        int[] arr = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            arr[i] = res.get(i);   
        }
    return  arr;
    }
}