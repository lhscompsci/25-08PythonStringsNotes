s = "compsci"

print(s[1])
print(s[6])

# substrings
print(s[1:4])
print(s[1:1])
print(s[:-2])  #starts at the beginning
print(s[3:-1])
print(s[0:-3])
print(s[-3:])  #stop at the end

# useful functions
print(len(s))
print(s.find("p"))
print(s.find("c"))
print(s.find("x"))
print(s.rfind("c"))

# concatenation
word1 = "computer"
word2 = "science"
together = word1 + " " + word2
print(together)

# comparisons
print(word1 > word2)
print(word1 == word2)
print(word1 <= word2)


def get_first_chunk(s):
    #write some code to return
    #all the letters up to the first
    # @ in the string
    # if @ is the first thing, return "done"
    # if there are no @s, return "DONE"
    return ""


print(get_first_chunk("hello@world"))
print(get_first_chunk("welcome@back@yall"))
print(get_first_chunk("noatsigns"))
print(get_first_chunk("@howdy@@everyone@@@"))
