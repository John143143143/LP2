public class Sorting{
    public static void main(){
        Integer[] arr = new Integer[](5, 3, 8, 1, 2);
        Integer n = arr.size();
        for(Integer i = 0; i < n-1; i++){
            for(Integer j = 0;j<n-i-1;j++){
                if(arr[j] > arr[j+1]){
                    Integer temp = arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
        System.debug('Sorted numbers : '+arr);
    }
}