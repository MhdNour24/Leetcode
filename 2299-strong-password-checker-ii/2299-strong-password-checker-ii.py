class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special_ch="!@#$%^&*()-+"
        following_criteria={"lowercase_character":False,"uppercase_character":False,"one_digit":False,"same_characters":True,"special_charakter":False}
        
        length=len(password)
        if length<8:
            return False
        past_character=None
        for i in range(length):
            if password[i].islower():
                following_criteria["lowercase_character"]=True
            elif password[i].isupper() :
                following_criteria["uppercase_character"]=True
            elif password[i] in special_ch:
                following_criteria["special_charakter"]=True
            try:
                a=int(password[i])
                following_criteria["one_digit"]=True
            except:
                pass
            if i!=0 and password[i]==past_character:
                
                following_criteria["same_characters"]=False
            past_character=password[i]
        return all(list(following_criteria.values()))
