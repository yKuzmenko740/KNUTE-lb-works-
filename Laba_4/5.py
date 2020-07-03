X = False
Y = True
Z = True
M = True

if X and Y and Z:  # True если и Х и Y и Z = True, в остальных случаях - False
    pass
if X or Y or Z:  # True если или X или Y или Z = True, в остальных случаях - False
    pass
if X or Y and Z:  # True если (или X или и X и Y) = True, в остальных случаях - False
    print(1)
if X or Y and Z or M:  # True если ((или X или Y) = True и (или Z или M) = True), в остальных случаях - False
    pass
if X and Y or Z and M:  # True если ((и X и Y = True) или (и Z и M = True)), в остальных случаях - False
    pass
if X and (Y or Z and M):  # True если (и X и ((или Y или Z) и M = True)), в остальных случаях - False
    pass
