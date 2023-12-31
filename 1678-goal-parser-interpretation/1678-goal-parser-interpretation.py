class Solution:
    def interpret(self, command: str) -> str:
        length=len(command)
        c=0
        new_char=""
        while c<length:
            ord_char_1=ord(command[c])
            if ord_char_1==71:
                new_char+="G"
                c+=1
            elif ord_char_1==40 and ord(command[c+1])==41:
                new_char+="o"
                c+=2
            else:
                new_char+="al"
                c+=4
        return new_char
