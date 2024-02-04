import pyttsx3
textt = pyttsx3.init()
txt={
     "hello":"hi",
     "how are you":"iam fine",
     "ki koros":"eito boisa asi",
     "khabar khaisot":"humm",
     "ki khaili":"jhal muri",
     "ar kiso khasnai?":"nah ar kiso khai nai",
     "accha toi konodin kanchot ni?":"sotti kotha ki ami na konodin kandinai",
     "klk ki korso?":"kisoi kori nai",
     "ami klk pythoner class korsi":"ami kori nai",
     "accha tomi bts er new je song ta relise hoise oita sonso?":"humm oije teak tow",
     "jk to bts er hoiya mama awerd nise dekla":"humm jk to ei year e onek... gola awerds paise",
     "accha jk koi jaibo?":"oo winter aisa porsena ora military te choila jaibo to",
     "ta asbo kobe ora?":"2025 sale asbo",
     "sobar aste taile onek let hoibu na?":"humm aste aste aro deri ase",
     "samiya mara gese jano?":"humm sonchi ah.. bechari koto balakharap chilo"
}

while True:
     try:
         user = input()
         if user == 'quit':
             break
         else:
            print(txt[user])
            textt.say(txt[user])
            textt.runAndWait()
     except:
         print("i don't know")
         textt.say("i don't know")
         textt.runAndWait()
