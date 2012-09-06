-module(day1).
-export([word_count/1]).
-export([count/1]).
-export([output/1]).

word_count(String) -> sets:size(sets:from_list(string:tokens(String, " "))).

count(0) -> 0;
count(N) -> count (N-1) + 1.

output(success) -> io_lib:write_string("Success");
output({error, Message}) -> io_lib:write_string(Message).
