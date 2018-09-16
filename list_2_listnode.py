#! -*- coding:utf-8 -*-


class Linknode(object):
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

def list_2_linknode(array):
    tem_node = Linknode()
    node = Linknode()
    for i in array:
        #记得是判定val是否有值，并且用一个node记住头节点，然后返回的是头节点
        if not tem_node.val:
            tem_node.val =i
            node = tem_node
        else:
            tem_node.next = Linknode(i)
            tem_node = tem_node.next
    return node

if __name__ == '__main__':
    array = [1,2,3,4,5]
    print(list_2_linknode(array).next.next.val)