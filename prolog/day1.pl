likes(wallace,cheese).
likes(gromit,cheese).
likes(wendy,geese).

friends(X,Y) :- \+(X=Y), likes(X,Z), likes(Y,Z).

