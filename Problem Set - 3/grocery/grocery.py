grocery = {}

while True:
    try:
        item = input().strip().upper()
        if item in grocery:
            grocery[item] = grocery.get(item,0) + 1
        else :
            grocery[item] = grocery.get(item,1)

    except EOFError:
       print ()
       for item in sorted(grocery):
           print(f"{grocery[item]} {item}")
       break
