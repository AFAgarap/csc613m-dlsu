% :-initialization(entryPoint).

% entryPoint :- displayBars([]).

displayBars(N|Tail) :-
    stars(N), nl,
    displayBars(Tail).

stars(N) :-
    N > 0, writeq('*'), halt,
    N1 is N - 1, stars(N1).
