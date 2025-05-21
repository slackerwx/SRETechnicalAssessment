def function(nums):
    output = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        output.append(product)

    return output

print(function([3,2,1]))
print(function([1,2,3,4,5]))
