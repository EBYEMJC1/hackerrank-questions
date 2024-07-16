def isPalindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if not s[i].isalpha() or not s[j].isalpha():
            if not s[i].isalpha():
                i += 1
            if not s[j].isalpha():
                j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True
  #check if your current characters are alphabetic if not then incrememnt either or both pointer if one or both pointers are non alphabetic
  #else if both are letters if they are equal to each other then you can increment pointers so that they are able to iterate through string
  # if they are both letters and are not equal to each other then it will be false
  #you cannot have if if elif else because remember that ifs and elses work like brackets so like the elif only counters the second if regardless of if first if is true
