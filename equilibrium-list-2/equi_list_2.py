


 
def findElement(arr, n):
    for i in range(1, n):
        leftSum = sum(arr[0:i])
        rightSum = sum(arr[i+1:])
        if(leftSum == rightSum):
            return arr[i]
    return -1
 
 
# Driver Code
if __name__ == "__main__":
 
    # Case 1
    arr = [1, 4, 2, 5]
    n = len(arr)
    print(findElement("list", arr,  n))
 
    # Case 2
    arr = [2, 3, 4, 1, 4, 5]
    n = len(arr)
    print(findElement(arr, n))

