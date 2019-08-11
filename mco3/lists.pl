in_mind([a,p,p,l,e]).

start :- write('Guess first letter:'), read(X),
    in_mind([X|T]), guess(T).

guess([]) :- in_mind(W), write(W).
guess(L) :- write('Next letter:'), read(X),
    ((L=[X|T1], guess(T1));
    (write('Try again:'), nl, guess(L))).
