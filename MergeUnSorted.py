class MergeUnSorted:
        def mergeunsorted(self,arr):
            if len(arr)>1:
                mid = len(arr)//2
                arr1 =arr[:mid]
                arr2 = arr[mid:]
                self.mergeunsorted(arr1)
                self.mergeunsorted(arr2)
                i = 0
                j = 0
                k = 0

                while i < len(arr1) and j < len(arr2):
                    if arr1[i] < arr2[j]:
                        arr[k] = arr1[i]
                        i += 1
                        k += 1
                    else:
                        arr[k]=arr2[j]
                        j += 1
                        k += 1
                while len(arr1) > i:
                    arr[k]=arr1[i]
                    i += 1
                    k += 1
                while len(arr2) > j:
                    arr[k]=arr2[j]
                    j += 1
                    k += 1


if __name__ == "__main__":
        obj = MergeUnSorted()
        arr = [9,12,123,45,35,13]
        obj.mergeunsorted(arr)
        print(arr)