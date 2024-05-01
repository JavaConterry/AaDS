from binary_tree import BinaryTree

inp = None
while inp==None:
    inp = input('\nInput str:')

tree = BinaryTree(inp[0], leteral=True)
if(len(inp)>1):
    for i in inp[1:]:
        tree.add(i)

tree.pretty_print()


def remove_repeated(tree: BinaryTree):
    repeated = []
    vals = tree.__str__(array=True)
    rep=0
    for i in range(1,len(tree.__str__(array=True))):
        if(vals[i]==vals[i-1]):
            rep+=1
            repeated.append(vals[i])
        elif(rep!=0):
            repeated.append(repeated[-1])
            rep=0

    print(repeated)
    while repeated!=[]:
        tree.remove(repeated[0])
        repeated.remove(repeated[0])
    return tree

tree = remove_repeated(tree)
tree.pretty_print()