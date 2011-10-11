fib_naive(0,1) :- !.
fib_naive(1,2) :- !.
fib_naive(X,Y) :-
    X > 1,
    X1 is X - 1,
    X2 is X - 2,
    fib_naive(X1, Prev),
    fib_naive(X2, PrePrev),
    Y is Prev + PrePrev.
    
fib(0,1) :- !.
fib(1,2) :- !.
fib(X,Y) :-
    X > 1,
    fib_calc(1,2,X,Y).
    
fib_calc(_, F, 1, F) :- !.
fib_calc(ST1, ST2, I, Result) :-
    I1 is I - 1,
    ST3 is ST1 + ST2,
    fib_calc(ST2, ST3, I1, Result).