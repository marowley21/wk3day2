def moveZerosToEnd(inputList):
    # Find length of list or array "inputList"
    lengthOfArr = len(inputList)

    k = 0

    for i in range(lengthOfArr):
        inputList[k] = inputList[i]
        k += 1 if inputList[i] else 0
    inputList[k:] = [0] * (lengthOfArr - k)
    print(inputList)


nums = [0, 1, 0, 3, 12]
nums2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
moveZerosToEnd(nums)
moveZerosToEnd(nums2)
nums = ([0])
nums2 = ([0])
