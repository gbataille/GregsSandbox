-module(day2).
-export([getFromKey/2]).

getFromKey([], _) -> false;
getFromKey([{Key, Value}|_], Key) -> Value;
getFromKey([{_, _}|Rest], Key) -> getFromKey(Rest,Key).

