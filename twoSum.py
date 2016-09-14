def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indicies = []
    outer_index = 0
    inner_index = 0
    for i in nums:
        for j in nums:
            if (i+j) == target and outer_index!=inner_index:
                print "i: ", i, "j: ", j
                print "inner_index: ", inner_index, "outer_index: ", outer_index
                if inner_index not in indicies:
                    indicies.append(inner_index)
                if outer_index not in indicies:
                    indicies.append(outer_index)
            inner_index = inner_index + 1
        inner_index = 0
        outer_index = outer_index + 1
    return indicies


def twoSumFaster(nums, target):
    # print "\n\nFinding two sums faster: "
    indicies=[]
    need = {}
    index = 0
    for i in nums:
        # print "i: ", i
        if i in need.keys():
            # print "Found matching half in need dictionary."
            indicies.append(index)
            indicies.append(need.get(i))
        elif i not in need.keys():
            # print "Adding to need dictionary."
            need[target - i] = index
            # print need
        else:
            # print "What's going on?"
            # print "i: ", i
            # print "index: ", index
            # print "need dic: ", need
            # print "indicies: ", indicies
        index = index + 1
    return indicies






print twoSum([3, 2, 4], 6)
print twoSumFaster([3, 2, 4], 6)