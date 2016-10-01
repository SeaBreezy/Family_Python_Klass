#handleE
#adds people to family and define parent child relationships
#pXDict is a reference to dictionary of that person
def handleE(p1,p2,p3):
    print(p1 + ' ' + p2 + ' ' + p3);
    p1Dict = family.setdefault(p1,{});
    p2Dict = family.setdefault(p2,{});
    p3Dict = family.setdefault(p3,{});

    p1Spouses = p1Dict.setdefault("spouses",set());
    p1Spouses.add(p2);
    p1Children = p1Dict.setdefault("children",set());
    p1Children.add(p3);
    
    p2Spouses = p2Dict.setdefault("spouses",set());
    p2Spouses.add(p1);
    p2Children = p1Dict.setdefault("children",set());
    p2Children.add(p2);
    
    p3Parents = p3Dict.setdefault("parents",set());
    p3Parents.add(p1);
    p3Parents.add(p2);
    return 0;

def handleW(s1,s2):
    return 0;
def handleX(s1,s2,s3):
    return 0;
def handleW(s1,s2):
    return 0;

#handleP
#a debugging tool that prints out contents of each member of the family when called
def handleP():
    print(sorted(family.keys()));
    print('handledP');

#create dictionary datastructure
family = {}
#run until EOF
while(1):
    #If it is at EOF, exit main loop
    #otherwise continue to process
    try:
        s = input();
    except EOFError as e:
        break;
    
    #tokenize the string
    tokenList = s.split();

    #determine query case
    if(tokenList[0] == 'E'):
        print('E');
        handleE(tokenList[1],tokenList[2],tokenList[3]);
    if(tokenList[0] == 'R'):
        print('R');
        #handleX
    if(tokenList[0] == 'X'):
        print('X');
        #handleX
    if(tokenList[0] == 'W'):
        print('W');
        #handleW
    if(tokenList[0] == 'P'):
        print('P');
        handleP();
