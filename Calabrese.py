#handleE
#adds people to family and define parent child relationships
#pXDict is a reference to dictionary of that person
def handleE2(p1,p2):
    p1Dict = family.setdefault(p1,{});
    p2Dict = family.setdefault(p2,{});

    p1Spouses = p1Dict.setdefault("spouse",set());
    p1Spouses.add(p2);

    p2Spouses = p2Dict.setdefault("spouse",set());
    p2Spouses.add(p1);
    
def handleE3(p1,p2,p3):
    print(p1 + ' ' + p2 + ' ' + p3);
    p1Dict = family.setdefault(p1,{});
    p2Dict = family.setdefault(p2,{});
    p3Dict = family.setdefault(p3,{});

    p1Spouses = p1Dict.setdefault("spouse",set());
    p1Spouses.add(p2);
    p1Children = p1Dict.setdefault("children",set());
    p1Children.add(p3);
    
    p2Spouses = p2Dict.setdefault("spouse",set());
    p2Spouses.add(p1);
    p2Children = p1Dict.setdefault("children",set());
    p2Children.add(p3);
    
    p3Parents = p3Dict.setdefault("parent",set());
    p3Parents.add(p1);
    p3Parents.add(p2);
    return 0;

def handleW(s1,p1):
    #If person exists ret = personDict
    #otherwise return empty list
    try:
        ret = family[p1];
    except KeyError as e:
        return [];
    
    #case spouse
    if(s1 == "spouse"):
        try:
            ret = ret["spouse"];
        except KeyError as e:
            return [];
    
    #case parent
    elif(s1 == "parent"):
        try:
            ret = ret["parent"];
        except KeyError as e:
            return[];
    #case sibling
        #get child sets of both parents, take their union :^D
    #base case
    else:
        return [];
    return ret; 
def handleX(s1,s2,s3):
    pass;
def handleR(s1,s2):
    pass;

#handleP
#a debugging tool that prints out contents of each member of the family when called
def handleP():
    for v in family:
        print(15*'*');
        print(v);
        print(family[v]);
        print(15*'*');
        
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
    if(tokenList[0] == 'E' and len(tokenList) == 3):
        print('E2');
        handleE2(tokenList[1],tokenList[2]);

    if(tokenList[0] == 'E' and len(tokenList) == 4):
        print('E3');
        handleE3(tokenList[1],tokenList[2],tokenList[3]);

    if(tokenList[0] == 'R'):
        print('R');
        #handleX

    if(tokenList[0] == 'X'):
        print('X');
        #handleX

    if(tokenList[0] == 'W'):
        print('W '+ tokenList[1] +' '+tokenList[2]);
        val = handleW(tokenList[1],tokenList[2]);
        val = sorted(val);
        for i in val:
            print(i);

    if(tokenList[0] == 'P'):
        print('P');
        handleP();
