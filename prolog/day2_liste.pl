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

removeElem(_, [], []) :- !.
removeElem(Elem, [Head|Rest], Rest) :-
    Elem is Head,
    !.
removeElem(Elem, [Head|Rest], [Head|List2]) :-
    removeElem(Elem, Rest, List2).
    
sortNaive(List1, SortedList) :-
    sortNaiveSub(List1, ReverseSortedList),
    reverseList(ReverseSortedList, SortedList).
sortNaiveSub([],[]) :- !.
sortNaiveSub(List, [Max|SortedList1]) :-
    maxList(List, Max),
    removeElem(Max, List, List1),
    sortNaiveSub(List1, SortedList1).
    
    