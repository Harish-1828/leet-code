class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> arr=new ArrayList<>();
        arr.add(new ArrayList<>(Arrays.asList(1)));
        if (numRows==1)
        {
            return arr;
        }
        arr.add(new ArrayList<>(Arrays.asList(1,1)));
        System.out.println(arr);
        int sum=0;
        for(int i=2;i<numRows;i++)
        {
            ArrayList<Integer>arr1=new ArrayList<>();
            arr1.add(1);
            for(int j=0;j<i-1;j++)
            {
                sum=0;
                List<Integer>a=arr.get(i-1);
                sum=sum+a.get(j)+a.get(j+1);
                arr1.add(sum);
            }
            arr1.add(1);
            arr.add(arr1);
        }
        return arr;
    }
}