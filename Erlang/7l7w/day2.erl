-module(day2).
-export([getFromKey/2, totalCartByProduct/1]).

% Takes 
%   - A list of tuples [{key, value}, ...]
%   - A value to look for in the key list of the tuples list
% Returns
%   - The value associated to the passed key if it exists
%   - false otherwise

getFromKey([], _) -> false;
getFromKey([{Key, Value}|_], Key) -> Value;
getFromKey([{_, _}|Rest], Key) -> getFromKey(Rest,Key).

% Takes
%   - A shopping cart of the form [{item, quantity, unitPrice}, ...]
% Returns
%   - A list of items associated with their total price

totalCartByProduct(X) -> [{Item, Quantity*Price} || {Item,Quantity,Price} <- X].
