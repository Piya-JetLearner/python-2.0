import random
word_list=["candyfloss","pizza","chocolate","camera","guitar"]
def w(word):
    w_list=list(word)
    random.shuffle(w_list)
    return"".join(w_list)
rounds=5
count=1
score=0
print("Welcome to SCRABBLE!!! here you will have a lot of fun solving these PUZZLES!!!")
for i in range(5):
    print("Round:", count)
    word=random.choice(word_list)
    candyfloss=w(word)
    print("here is the scrambled word:",candyfloss)
    hint=input("do u want a hint? yes/no")
    if hint=="yes":
        print("The first letter of the word is ", word[0])
        user=input("what is the scrabbled word?")
    if hint=="no":
        user=input("what is the scrabbled word?")
    if user==word:
        print("WELL DONE! you got it correct. Now you get an extra point.")
        score=score+1
    else:
        print("thats wrong")
    count=count+1
print("your final score now is",score)