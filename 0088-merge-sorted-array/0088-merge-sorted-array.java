class Solution {

public static void expandArraySize(int[] nums1,int m,int n){
    m = m+n;
    nums1 = java.util.Arrays.copyOf(nums1,m);
}
public void merge(int[] nums1, int m, int[] nums2, int n) {
    expandArraySize(nums1,m,n);
    for(int i = 0; i <n ;i++){
        nums1[m] = nums2[i];
        m++;
    }
    Arrays.sort(nums1);
    System.out.println(Arrays.toString(nums1));
}
}