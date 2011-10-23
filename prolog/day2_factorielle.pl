facto_naive(1,1) :- !.
facto_naive(N, Result) :-
    N > 1,
    N1 is N - 1,
    facto_naive(N1, R1),
    Result is R1 * N.