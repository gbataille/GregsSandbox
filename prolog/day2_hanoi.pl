%Does not work
move([Disc],X,Y,_) :-  
    write('Move disk '),
    write(Disc),
    write(' from '), 
    write(X), 
    write(' to '), 
    write(Y), 
    nl. 
move([Bottom|Rest],Start,Swap,Goal) :- 
    move(Rest,Start,Swap,Goal), 
    move([Bottom],Start,Goal,_), 
    move(Rest,Swap,Goal,Start).