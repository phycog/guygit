'''
after i try to make tree (data structure) by my own
i have no idea what i am doing


'''
sibling_left_side = []
sibling_rifgt_side = []

class guy_tree:
    
    def color_tree(self,color):
     self.color = color
    def main_tree(self,root,branch_l,branch_r):
     self.root = root
     self.branch_l = branch_l
     self.branch_r = branch_r

    def add_sibling_node_lv2(self,left_side,right_side):
        
        self.left_side = left_side
        global sibling_left_side
        sibling_left_side.append(left_side)
        self.right_side = right_side
        global sibling_rifgt_side
        sibling_rifgt_side.append(right_side)

    
tree = guy_tree()
tree.main_tree("electronic device","labtop","PC")
tree.add_sibling_node_lv2("HP","Dell")

tree.add_sibling_node_lv2("Sumsung","MAC")

tree.add_sibling_node_lv2("SONY","Toshiba")

def show_tree():
 print(tree.root)
 print(tree.branch_l,"    ",tree.branch_r)
 print(sibling_left_side,"     ",sibling_rifgt_side)

show_tree()



         

