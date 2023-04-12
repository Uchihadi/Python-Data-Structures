#lex_auth_0127667355651112963444

def pattern_search(text, pattern):
    #Remove pass and write your logic here
    len_text = len(text)
    len_pattern = len(pattern)
    count = 0
    for i in range (0, len_text):
        if (pattern == text[i:(i+len_pattern)]):
            count += 1
    return count

# def pattern_search(text, pattern):
    # count = 0
    # length = len(pattern)
    # for i in range(0,len(text)):
    #     if text[i:length] == pattern:
    #         count+=1
    #         length+=1
    #         continue
    #     else:
    #         length+=1
    #         continue
    # return count 

# def pattern_search3(text, pattern):
    # count = 0
    # text = text
    # while True:
    #     if len(text) <= 0:
    #         break
    #     if text[:len(pattern)] == pattern:
    #         count +=1
    #         text = text[len(pattern):]
    #     else:
    #         text = text[1:]
    # return count
    
# count = text.count(pattern)
    # return count

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
print("The given text:",text)
print("Pattern:",pattern)
print("No. of occurrences of the pattern :",result)