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

blushes(X) :- human(X).
human(derek).

stabs(tybalt, mercutio, sword).
hates(romeo, X) :- stabs(X, mercutio, sword).

% anonymous variable is _
% male(_).

what_grade(5) :-
    write('Go to kindergarten.').

what_grade(6) :-
    write('Go to 1st grade.').

% operator is is the equal
what_grade(Other) :-
    Grade is Other - 5,
    format('Go to grade ~w', [Grade]).

% structures
% has(albert, olive).
% owns(albert, pet(cat, X)).
owns(albert, pet(cat, olive)).

% query balance of sally
% customer(sally, _, Bal).
customer(tom, smith, 20.55).
customer(sally, smith, 120.55).

get_customer_balance(FName, LName) :-
    customer(FName, LName, Bal),
    write(FName), tab(1),
    format('~w owes us $~2f ~n', [LName, Bal]).

vertical(line(point(X, Y1), point(X, Y2))).
horizontal(line(point(X1, Y), point(X2, Y))).

% alice = alice.
% 'alice' = alice.
% \+ alice = albert.
% \+ alice = alice.
% 3 > 15.
% 3 >= 15.
% 3 =< 15.
%
% assign alice to W
% W = alice.
%
% assign a variable to another
% Rand1 = Rand2.
%
% rich(money, X) = rich(Y, no_debt).
% X = no_debt
% Y = money
%

warm_blooded(penguin).
warm_blooded(human).

produce_milk(penguin).
produce_milk(human).

have_feathers(penguin).
have_hair(human).

mammal(X) :-
    warm_blooded(X),
    produce_milk(X),
    have_hair(X).

% warm_blooded(X), produce_milk(X), write(X), nl.
