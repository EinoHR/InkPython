VAR playername = "player aa"
VAR money = 10
VAR hashoodie = false

In the shop


//  This is the test .ink file made in just a few minutes for an earlier fantasy game project inside unity using Ink, but edited to use more features to really test parsing ink in python.

->start

==start==
Shopkeeper: 'Ey {playername}! What do you wish from this old fella?
You: Hey ol' man!
Shopkeeper: Hi!
+[buy]You: Lemme get that hoodie.
-> buy
+[sell]You: Can I sell you something, got no money?
-> sell
+[talk]You: Ay ol' man, what are you selling?
-> talk



==buy==
Shopkeeper: Oh, this?
+[Yes! Here you go 5 euros.]You: Yes! Here you go {money} euros.
~ money = money - 5
~ hashoodie = true
~ playername = playername + ", my dearest customer"
-> end

==sell==
Shopkeeper: What do you offer?
+[Nevermind, nothing.]You: Nevermind, nothing.
-> start

==talk==
Shopkeeper: Well, I've only got hoodies.
+[Ok, lemme have one]You: Ok, lemme have one
-> buy

==end==
Your current balance: {money}
Currenty have a hoodie: {hashoodie}
The Shopkeeper currently calls you: {playername}
-> DONE

    