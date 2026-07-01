print("hello i am ai vot. whats your name?")
name = input()
print(f"nice to meet you {name}.")
print("how are you feeling today? (good/bad): ")
feeling = input().lower()
if feeling == "good":
    print("thats good to hear. i am feeling good too.")
elif feeling == "bad":
    print("i am sorry to hear that. i hope you feel better soon.")
else:
    print("i am not sure what you mean by that. but i hope you feel better soon.")
print(f"it was nice chatting with you {name}. have a good day!")