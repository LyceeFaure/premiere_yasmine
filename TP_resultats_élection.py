def est_present(tab, v):
    for v in tab:
        if v == e:
            return True
        return False
    
def depouillement(candidats, votes):
    occurrences = {"Nul": 0, "Blanc": 0}
    for c in candidats:
        occurrences[c] = 0
    for v in votes:
        if est_present(candidats, v):
            occurrences[v] + 1
        elif v == "":
            occurrences["Blanc"]+=1
        else:
            occurrences["Nul"]+=1
    return occurrences

e = depouillement(["Alan Turing", "Ada Lovelace", "George Boole"], ["Alan Turing", "Ada Lovelace", "Ada Lovelace", "", "Mark Zukerberg", ""])