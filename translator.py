from translate import Translator
print('''
    *******************************************************************
    * _  _      _ _      _____                 _      _   _           *
    *| || |_  _| | |____|_   _| _ __ _ _ _  __| |__ _| |_(_)___ _ _   *
    *| __ | || | | / /___|| || '_/ _` | ' \(_-< / _` |  _| / _ \ ' \  *
    *|_||_|\_,_|_|_\_\    |_||_| \__,_|_||_/__/_\__,_|\__|_\___/_||_| *
    *                                                                 *
    *******************************************************************  
      ''')
translator= Translator(from_lang=input(" [?] From Language You Want To Translate : "),to_lang=input(" [?] To Which Language You Want To Translate : "))
translation = translator.translate(input(" 🔴🔴 Enter The Text : "))
print (" Translation is : " + translation)
input("Enter To Exit")