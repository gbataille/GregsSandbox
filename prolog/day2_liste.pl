concatenate([], List1, List1).
concatenate([Head|Tail], List2, [Head|Result]) :- 
	concatenate(Tail, List2, Result).
	
reverseList([A], [A]) :- !.
reverseList([Tete|Liste], Reverse) :-
    reverseList(Liste, RevListe),
    concatenate(RevListe, [Tete], Reverse).
    
maxList([], Max) :- !.
maxList([Head|Rest], Max) :-
    maxList(Rest, Max1),
    Head @> Max1,
    Max = Head,
    !.
maxList([Head|Rest], Max) :-
    maxList(Rest, Max1),
    Head @=< Max1,
    Max = Max1,
    !.

    
    