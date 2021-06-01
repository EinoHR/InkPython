VAR playername = "player"
VAR money = 10

In the shop

->start

==start==
'Ey {playername}! What do you wish from this old fella?
+[buy]Lemme get that hoodie.
-> buy
+[sell]Can I sell you something, got no money?
-> sell
+[talk]Ay ol' man, what are you selling?
-> talk



==buy==
Oh, this?
+Yes!
-> DONE

==sell==
What do you offer?
+Nevermind, nothing.
-> start

==talk==
Well, I've only got hoodies.
+Ok, lemme have one 
-> buy