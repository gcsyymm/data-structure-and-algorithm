def permutation(LoE: list):
    LoL = []
    if len(LoE) <= 1:
        return [LoE]
    else:
        for i in range(len(LoE)):
            E = LoE[i]
            rem = LoE[:i]+LoE[i+1:]
            for perms in permutation(rem):
                LoL.append([E]+perms)
    return LoL
