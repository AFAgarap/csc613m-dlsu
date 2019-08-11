% loves is a predicate, 
% romeo and juliet are atoms
loves(romeo, juliet).
loves(juliet, romeo) :- loves(romeo, juliet).

% here are some facts
male(albert).
male(bob).
male(bill).
male(carl).
male(charlie).
male(dan).
male(edward).

female(alice).
female(betsy).
female(diana).

happy(albert).
happy(alice).
happy(bob).
happy(bill).
with_albert(alice).

% we define a rule with :-
runs(albert) :-
    happy(albert).

dances(alice) :-
    happy(alice),
    with_albert(alice).

does_alice_dance :-
    dances(alice),
    write('When Alice is happy and with Albert she dances').

swims(bob) :-
    happy(bob).

swims(bob) :-
    near_water(bob).

% playing with kinship
parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).

parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).

parent(bob, carl).
parent(bob, charlie).

% we can check the grandparent of carl by
% parent(Y, carl), parent(X, Y).

% we can check the grandchildren of someone by
% parent(albert, X), parent(X, Y).

get_grandchild :-
    parent(albert, X), parent(X, Y),
    write('Albert\'s grandchild is '),
    write(Y), nl.

% let us check if two people are siblings
% parent(X, carl), parent(X, charlie).

% use tilde for variable
% ~n is nl
get_grandparent :-
    parent(X, carl),
    parent(X, charlie),
    format('~w ~s grandparent ~n', [X, "is the"]).

brother(bob, bill).

% check if carl has an uncle
% parent(X, carl), brother(X, Y).

% check if carl has a sibling
% parent(X, carl), parent(X, Y).

% display the grand parent of someone
% this will not conflict with the get_grandparent above
% since this accepts atoms while the one above does not
get_grandparent(X, Y) :-
    parent(Z, X),
    parent(Y, Z),
    format('the grandparent of ~w is ~w ~n', [X, Y]).
