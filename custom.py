# class Word:
#   def __init__(self, word, hint):
#     self.word = word
#     self.hint = hint
#   def __str__(self):
#     return self.word


# sample = [
#   Word("ee", "ee"),
#   Word("ff", "ff"),
#   Word("ggg", "ggg"),
#   Word("aaaaa", "aaaaa"),
#   Word("cccc", "cccc"),
#   Word("bbbb", "bbbb"),
#   Word("ddd", "ddd"),
# ]

# # sample = [
# #   Word("e", "e"),
# #   Word("f", "f"),
# #   Word("a", "a"),
# # ]

# sample.sort(reverse=True ,key=lambda inp: len(inp.word))

# n = int(input())  # size of puzzle

# while( len(sample[0].word) > n):
#   sample = sample[1:]

# # for i in sample:
# #   print(i)

# cube = [ [ "-" for i in range(n) ] for i in range(n) ]
# hint = cube.copy()
# legend = cube.copy()


# def canPlaceVirtically(cube,n,l):
#   # n: size of cube,
#   # l: size of word
#   for i in range(n):
#     ind = [0,i]
#     blank = True
#     for j in range(n):
#       if (cube[0][i]!='-'):
#         blank = False
#     if (blank):
#       return ind
#   return False

# def fillVirticle(cube,ind,val: str):
#   # print(val)
#   for i in range(len(val)):
#     cube[ind[0]+i][ind[1]] = val[i]

# def canPlaceHorizontally(cube,n,l):
#   # n: size of cube,
#   # l: size of word
#   checkL = ["-" for i in range(l)]
#   for i in range(n):
#     if (cube[i][-l:] == checkL):
#       return [i,n-l]
    
#   return False

# def fillHorizontally(cube,ind,val: str):
#   # print(val)
#   for i in range(len(val)):
#     cube[ind[0]][ind[1]+i] = val[i]

# pickSet = sample.copy()

# wordChosen = []


# ## Vir horizontal approach
# # # print(pickSet[0].word)
# # # fit virtically
# # for i in pickSet:
# #   ind = canPlaceVirtically(cube,n,i.word.__len__())
# #   if (ind != False):
# #     wordChosen.append(i)
# #     fillVirticle(cube,ind,i.word)
# #     # for i in cube:
# #     #   print(i)
# #     # print(ind)
# #     # print()

# # for i in wordChosen:
# #   pickSet.remove(i)

# # # for i in pickSet:
# # #   print(i)

# # # for i in cube:
# # #   print(i)

# # for i in pickSet:
# #   ind = canPlaceHorizontally(cube,n,i.word.__len__())
# #   if (ind != False):
# #     wordChosen.append(i)
# #     fillHorizontally(cube,ind,i.word)
# #     # for i in cube:
# #     #   print(i)
# #   # print(ind)
# #   # print()

# ## ==============================
# ## even odd operation
# # for i in pickSet:
# #   if (pickSet.index(i)%2==0):
# #     ind = canPlaceVirtically(cube,n,i.word.__len__())
# #     if (ind != False):
# #       wordChosen.append(i)
# #       fillVirticle(cube,ind,i.word)
# #   else:
# #     ind = canPlaceHorizontally(cube,n,i.word.__len__())
# #     if (ind != False):
# #       wordChosen.append(i)
# #       fillHorizontally(cube,ind,i.word)




# for i in cube:
#   print(i)