#!/usr/bin/python
#Name:Immanuel I George


f = open('sample.txt',"r")
lines = f.readlines()
#print lines


def isEmpty(lines):
    if len(lines) == 0:
        return True
    else:
        return False
def nextToken(current,tokens):
    if(len(tokens) > current + 1):
        return current + 1;

def stmt(lines):
    current = 0;
    i = 0;
    tokendata =[]
    data ={}
    cID ="";
    if(isEmpty(lines) is False):
        for line in lines:
            tokens =line.strip().split()
            first = tokens[0]
            for token in tokens:
                if nextToken(current,tokens):
                    tokendata.append(tokens[0]);
                    id = first;
                    data[id] =first;
                    current  = nextToken(current,tokens)
                    if tokens[current] is not "=":
                         if tokens[current] is not ";":
                            chkbracket(tokens[current],current,tokens);       
                    if tokens[current] in tokendata:
                        cID = "T" + str(i+1)
                        id = cID
                        data[id] =cID;
                        print "STA ", cID;
                        i = i+1;
                        tokendata.append(cID);
                if(token.find(";") != -1):
                        current = 0;
            print "STA ", data[id]; 
            #print data
            #if cID is not "":
                #print "STA ", cID;
        print " "
        for key in sorted(data.keys() , reverse=True) :
                print key, " RESW " ,1
    else:
        print "Syntax error"

def term(currentToken,current,tokens):
    if currentToken is not "=":
         if currentToken is not ";":
            if currentToken is "+":
                if(tokens[current - 1].isdigit()):
                    print "LDA #", tokens[current - 1];
                if(tokens[current + 1].isdigit()):
                    print "ADD #", tokens[current + 1];
                else:
                     print "LDA ", tokens[current - 1];
                     print "ADD ", tokens[current + 1];
            elif currentToken is "-":
                print "LDA #", tokens[current-1];
                print "SUB ", tokens[current + 1];


def factor(currentToken,current,tokens):
  if currentToken is not "=":
         if currentToken is not ";":
            if currentToken is "*":
                if(tokens[current - 1].isdigit()):
                    print "LDA #", tokens[current - 1];
                if(tokens[current + 1].isdigit()):
                    print "MUL #", tokens[current + 1];
                else:
                     print "LDA ", tokens[current - 1];
                     print "MUL ", tokens[current + 1];
            elif currentToken is "/":
                print "LDA #", tokens[current - 1];
                print "DIV ", tokens[current + 1];
            elif len(tokens)==4 :
                print "LDA #", currentToken;
                
def chkbracket(currentToken,current,tokens):
     if currentToken is not "=":
         if currentToken is not ";":
             if currentToken is "(":
                 while tokens[current + 1] is not ")":
                    current = current + 1;
                    term(tokens[current],current,tokens);
                    factor(tokens[current],current,tokens);
             elif currentToken is not ")":
                term(tokens[current],current,tokens);
                factor(tokens[current],current,tokens);
                
             
stmt(lines)



