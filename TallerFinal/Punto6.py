class Tree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return 'Node value: {}'.format(self.data)
    
    def get_root(self):
        return str(self.data)
    
    def contains(self, node_to_search, cont=1, level=False):
        if self.data == node_to_search:
            if level == True:
                return True, cont
            return True
        elif node_to_search < self.data:
            if self.left == None:
                return False
            return self.left.contains(node_to_search, cont+1, level)
        else:
            if self.right == None:
                return False
            return self.right.contains(node_to_search, cont+1, level)
    
    def insert(self, new_node):
        try:
            assert self.contains(new_node) != True
            if new_node < self.data:
                if self.left == None:
                    self.left = Tree(new_node)
                else:
                    return self.left.insert(new_node)
            else:
                if self.right == None:
                    self.right = Tree(new_node)
                else:
                    return self.right.insert(new_node)
        except AssertionError:
            print('The node already exists in the tree!')
            return None
    
    def find_height(self, height=1):
        if self.data == None:
            return 0
        else:
            total_height = height
            if self.left != None:
                total_height = self.left.find_height(height+1)
            if self.right != None:
                right_h = self.right.find_height(height+1)
                if right_h > total_height:
                    total_height = right_h
            return total_height

    def pre_order(self):
        print(self.data)
        if self.left != None:
            return self.left.pre_order()
        if self.right != None:
            return self.right.pre_order()
    
    def in_order(self):
        if self.left != None:
            return self.left.in_order()
        print(self.data)
        if self.right != None:
            return self.right.in_order()        
    
    def pos_order(self):
        if self.left != None:
            return self.left.pos_order()
        if self.right != None:
            return self.right.pos_order()
        print(self.data)