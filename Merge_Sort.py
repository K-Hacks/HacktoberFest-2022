def merge_sort(data) -> None:
  if len(data) > 1:
      # making the left and right array
      left_arr = data[:len(data)//2]
      right_arr = data[len(data)//2:]

      # Recusion of the arrays
      merge_sort(left_arr)
      merge_sort(right_arr)


      i = 0 # index of left array
      j = 0 # index of right array
      k = 0 # index of the main array
      while i < len(left_arr) and j < len(right_arr):
          if left_arr[i]<right_arr[j]:
              data[k] = left_arr[i]
              i+=1
          else:
              data[k] = right_arr[j]
              j+=1
          k+=1

      while i < len(left_arr):
          data[k] = left_arr[i]
          i+=1
          k+=1
      while j < len(right_arr):
          data[k] = right_arr[j]
          j+=1
          k+=1
