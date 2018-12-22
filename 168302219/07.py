start = 'hit'
end = 'cog'

adict = ['hot','dot','dog','lot','log','dit']
def find_path(start, end, adict):
    adict.append(end)
    visited = []
    visited.append((start, 1))
    while visited:
        curr = visited.pop(0)
        currword = curr[0]; currlen = curr[1]
        if currword == end: 
            return currlen
        for i in range(len(start)):
            for j in range(ord('a'),ord('z')+1):
                if currword[i] != j:
                    nextword = currword[:i]+ chr(j) + currword[i+1:]
                    if nextword in adict:
                        visited.append((nextword, currlen+1));
                        adict.remove(nextword)
    return 0
print(find_path(start, end, adict))
