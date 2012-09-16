-module(translate).
-export([spanish_to_english/0, supervisor/0]).

spanish_to_english() ->
  io:format("LOG - Looping translator~n"),
  receive
    "casa" -> 
      io:format("home"),
      spanish_to_english();

    "blanca" -> 
      io:format("white"),
      spanish_to_english();

    _ -> 
      io:format("Can't translate, crashing.~n"),
      exit({translator,die,at,erlang:time()})

  end.

supervisor() ->
  process_flag(trap_exit, true),
  receive
    new ->
      register(translator, spawn_link(fun spanish_to_english/0)),
      supervisor();

    {'EXIT', From, Reason} ->
      io:format("process ~p died, with reason ~p. Restarting.~n", [From, Reason]),
      self() ! new,
      supervisor()

  end.
