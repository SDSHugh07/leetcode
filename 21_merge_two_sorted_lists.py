# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    head = None
    tail = None
    size = 0

    def addNode(self, new_node):
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1


    def mergeTwoLists(self, list1, list2):

        l1_current = list1
        l2_current = list2

        while l1_current or l2_current:
            if not l1_current:
                new_node = ListNode(l2_current.val)
                self.addNode(new_node)
                l2_current = l2_current.next
            elif not l2_current:
                new_node = ListNode(l1_current.val)
                self.addNode(new_node)
                l1_current = l1_current.next
            elif l1_current.val <= l2_current.val:
                new_node = ListNode(l1_current.val)
                self.addNode(new_node)
                l1_current = l1_current.next
            else:
                new_node = ListNode(l2_current.val)
                self.addNode(new_node)
                l2_current = l2_current.next

        return self.head

def createLists(l1, l2):

    for item in l1:
        if l1.len() == 0:
            head
        head = None
        list.reverse()

        for item in list:
            new_node = ListNode(item)
            head = new_node


if __name__ == "__main__":
    print("21_merge_two_sorted_lists")

    sol = Solution()

    inputs = [[[1,2,4],[1,3,4]],[[],[]], [[],[0]]]

    # for input in inputs:
    #     l1, l2 = createList(input[0], input[1])

    l1_2 = ListNode(4)
    l1_1 = ListNode(2, l1_2)
    l1 = ListNode(1,l1_1)

    l2_2 = ListNode(4)
    l2_1 = ListNode(3, l2_2)
    l2 = ListNode(1,l2_1)

    output = sol.mergeTwoLists(l1, l2)

    l1_2 = ListNode(4)
    l1_1 = ListNode(2, l1_2)
    l1 = ListNode(1,l1_1)

    l2_2 = ListNode(4)
    l2_1 = ListNode(3, l2_2)
    l2 = ListNode(1,l2_1)

    output = sol.mergeTwoLists(l1, l2)
    print(output)

    output = sol.mergeTwoLists(None, None)
    print(output)

    output = sol.mergeTwoLists(None, ListNode(0))
    print(output)
