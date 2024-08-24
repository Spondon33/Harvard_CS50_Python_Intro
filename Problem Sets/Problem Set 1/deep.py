# deep question
ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
if ans == str(42):
    print("Yes")
elif ans == "forty-two":
    print("Yes")
elif ans == "forty two":
    print("Yes")
else:
    print("No")
