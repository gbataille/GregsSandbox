concatenate([], List1, List1).
concatenate([Head|Tail], List2, [Head|Result]) :- 
	concatenate(Tail, List2, Result).