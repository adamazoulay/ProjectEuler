num1 = l1.val
num2 = l2.val

tmp_total = num1 + num2
carry = 0
if (tmp_total > 10):
    carry = 1
    tmp_total -= 10

l_total = ListNode(tmp_total)
l_total.next = addNext(l1.next, l2.next, carry)

def addNext(l1, l2, carry):
    num1 = l1.val
    num2 = l2.val

    if (num1 == None && num2 == None):
        if carry != 0:
            return ListNode(carry)
        return None

    if (num1 == None):
        num1 = 0
    if (num2 == None):
        num2 = 0

    tmp_total = num1 + num2 + carry
    if (tmp_total > 10):
        carry = 1
        tmp_total -= 10

    l3 = ListNode(tmp_total)
    l3.next = addNext(l1.next, l2.next, carry)
    return l3

return l_total
