selection = input("Are you a cat person or a dog person?: ")

if selection.lower() == 'cat':
    print("Cat")
    catname = input("What is the best cat name?: ")
    print("Cat named",catname)
elif selection.lower() == 'dog':
    print("Dog")
    dogname = input("What is the best dog name?: ")
    print("Dog named",dogname)
else:
    print("Follow directions better.")
