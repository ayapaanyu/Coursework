### Aya Ishida (MSc IT) 
### ISD Term2 Coursework 1, Submitted at 9/2/2016
### Question 1

def ReplaceCS(instr, wordsBefore, wordsAfter):
    words=instr.split(",")

    ### Check if the lengths of the two input lists are equal
    ### If not equal, return the original string and error display
    if len(wordsBefore) != len(wordsAfter):
        return [instr, "False", "List lengths do not match"]
    
    ### If equal,
    else:

        ### Replace the original string
        outstr=[] #storage of the altered string
        wordsReplaced={} #storage of the altered words and the times

        for i in range (len(words)):
            if words[i] in wordsBefore:
                n = wordsBefore.index(words[i])
                outstr.append(wordsAfter[n])

                ### Store the altered words and the times
                if words[i] in wordsReplaced:
                    wordsReplaced[words[i]]=wordsReplaced[words[i]]+1
                else:
                    wordsReplaced[words[i]]=1
                i=i+1
                
            else:
                outstr.append(words[i])
                i=i+1
                
        ### Find the unaltered words and store them with the times
        for i in range (len(wordsBefore)):
            if wordsBefore[i] not in words:
                wordsReplaced[wordsBefore[i]]=0
                i=i+1

        ### Description for desplay
        outstrCount=[]#storage of description
        
        for key in sorted(wordsReplaced):
            if wordsReplaced[key]==1:
                outstrCount.append("%s :replaced 1 time" %(key))
            else:
                outstrCount.append("%s :replaced %d times" %(key, wordsReplaced[key]))

    ### Output
    return [','.join(outstr), "True", '\n'.join(outstrCount)]


txt="yes,the,answer,is,yes"
[s, flag, description]=ReplaceCS(txt,["yes"],["no"])
print(s)
print(flag)
print(description)
print("-----")

[s, flag, description]=ReplaceCS(txt,["yes", "the", "twelve"],["no", "a", "thirteen"])
print(s)
print(flag)
print(description)
print("-----")

[s, flag, description]=ReplaceCS(txt, ["yes", "the"],["no"])
print(s)
print(flag)
print(description)
print("-----")
