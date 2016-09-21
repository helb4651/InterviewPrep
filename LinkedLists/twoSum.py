# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_ll_int = ''
        l1_head = l1
        l1_curr = l1
        second_ll_int = ''
        l2_head = l2
        l2_curr = l2
        while True:
            first_ll_int = first_ll_int + str(l1_curr.val)
            if l1_curr.next == None:
                break
            elif l1_curr:
                l1_curr = l1_curr.next
            else:
                print "Something is wrong building first_ll_int."
        while True:
            second_ll_int = second_ll_int +str(l2_curr.val)
            if l2_curr.next == None:
                break
            elif l2_curr.next:
                l2_curr = l2_curr.next
            else:
                print "Something is wrong building first_ll_int."

        first_ll_int = first_ll_int[::-1]
        second_ll_int = second_ll_int[::-1]
        answer = int(first_ll_int) + int(second_ll_int)
        answer = str(answer)[::-1]

        # answer_ll = ListNode()
        # curr = answer_ll

        # for i in answer:
        #     curr.val = i
        #     a = ListNode()
        #     curr.next = a


        # For some reason leetcode wanted a list returned...
        li = []
        for i in answer:
            li.append(int(i))

        return li