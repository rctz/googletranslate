#-*- coding:utf-8 -*-
from googletrans import Translator, LANGUAGES
from termcolor import colored

def trans_show(lang, text):
    try:
        translate = T.translate(text ,src="auto",dest=lang).text
        print(">>> " + colored(translate, "red"))
    except Exception as e:
        print("Can not translate")
        
if __name__ == "__main__":
        T = Translator()
        
        Flag = True
        print("See all language code press 1")
        while(Flag):
            try:
                text = input(": ")
                if(text == str(1)):
                    find = input("lang: ")
                    dic_lang = LANGUAGES # dic of all language
                    key_lang = list(dic_lang.keys()) # Key to list
                    value_lang = list(dic_lang.values()) # Value to list
                    for i in range(len(value_lang)):
                        if(find in value_lang[i]): # if has lang in Value_list
                            print(key_lang[i]) # show Key_list at that index
                            print("\n==================\n")
                            break
                    continue

                lang = T.detect(text) # detect lang

                if(text == "q" or text == "exit"):
                    Flag = False
                    print("\nEnding")
                    print("===============\n")

                else:
                    if "," in text: # other language input ,
                        split = text.split(",")
                        text = split[1]
                        lang = split[0]
                        trans_show(lang, text) # translate and show   

                    elif(lang.lang == "en"): # input en >> th
                        trans_show("th", text) # translate and show

                    elif(lang.lang == "th"): # input th >> en
                        trans_show("en", text) # translate and show

            except Exception as error:
                print ("Translate error: ", error)

