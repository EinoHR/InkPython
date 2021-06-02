VAR playername = "player"
VAR money = 10

In the shop

->start

==start==
Shopkeeper: 'Ey {playername}! What do you wish from this old fella?
You: Hey ol' man!
+[buy]You: Lemme get that hoodie.
-> buy
+[sell]You: Can I sell you something, got no money?
-> sell
+[talk]You: Ay ol' man, what are you selling?
-> talk



==buy==
Shopkeeper: Oh, this?
+Yes!
-> DONE

==sell==
Shopkeeper: What do you offer?
+[Nevermind, nothing.]You: Nevermind, nothing.
-> start

==talk==
Shopkeeper: Well, I've only got hoodies.
+[Ok, lemme have one]You: Ok, lemme have one
-> buy

