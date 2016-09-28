def handleE(s1,s2,s3)
    return 0;
def handleW(s1,s2)
    return 0;
def handleX(s1,s2,s3)
    return 0;
def handleW(s1,s2)
    return 0;
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
        #handleE
    if(tokenList[0] == 'R'):
        print('R');
        #handleX
    if(tokenList[0] == 'X'):
        print('X');
        #handleX
    if(tokenList[0] == 'W'):
        print('W');
        #handleW
