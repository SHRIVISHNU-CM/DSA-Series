def lps(s):
    n = len(s)
    lps_arr = [0] *n
    length = 0
    i =1

    while i <n:
        if s[i] == s[length]:
            length +=1
            lps_arr[i] = length
            i +=1
        else:
            if length !=0:
                length = lps_arr[length-1]
            else:
                lps_arr[i] =0
                i +=1
    return lps_arr[-1]

print(lps("abab"))