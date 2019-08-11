parent(juan,ervin).
parent(ella,henry).
parent(joel,henry).
parent(john,mike).
parent(emy,mike).
parent(therese,pam).
parent(mike,jerry).
parent(pam,jerry).
parent(mike,joel).
parent(pam,joel).
has_a_child(X) :- parent(X,_).
child_of(X, Y) :- parent(Y, X).
male(john).
male(juan).
male(joel).
male(ervin).
male(jerry).
male(henry).
female(therese).
female(ella).
female(pam).
female(emy).
father(X) :- parent(X, _), male(X).
father(X, Y) :- male(X), parent(X, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), not(X=Y).
ninuno(X, Z) :- parent(X, Y), ninuno(Y, Z).
ninuno(X, Y) :- parent(X, Y).

% ninuno(X, Y) :- parent(X, Y).
% ninuno(X, Z) :- ninuno(X, Y), parent(Y, Z).
