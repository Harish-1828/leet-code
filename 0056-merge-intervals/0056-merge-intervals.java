class Solution {
    public int[][] merge(int[][] arr) {
        //Arrays.sort(arr,(a,b)->Integer.compare(a[0],b[0]));
        //Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        for(int i=0;i<arr.length;i++)
        {
            for(int j=0;j<arr.length-1-i;j++)
            {
                if(arr[j][0]>arr[j+1][0])
                {
                    int[] temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }

        List<int[]> ans = new ArrayList<>();
        ans.add(arr[0]);
        for(int i=1;i<arr.length;i++)
        {
            int[] curr=ans.get(ans.size()-1);
            if(curr[1]>=arr[i][0])
            {
                curr[1]=Integer.max(curr[1],arr[i][1]);
                curr[0]=Integer.min(curr[0],arr[i][0]);
            }
            else
            {
                ans.add(arr[i]);
            }
        }
        
         return ans.toArray(new int[ans.size()][]);
    }
}