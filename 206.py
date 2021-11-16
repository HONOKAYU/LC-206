# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 00:22:09 2021

@author: tyu6
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        while(head != None and head.next != None):
            dnext = dummy.next
            hnext = head.next
            dummy.next = hnext
            head.next = hnext.next
            hnext.next = dnext

        return dummy.next