% Family Tree problems

% Facts
male(john).
male(peter).
male(mike).
female(mary).
female(susan).
female(linda).

parent(john, peter).
parent(john, mary).
parent(mary, susan).
parent(peter, mike).
parent(linda, mike).

% Rules
father(F, C) :- male(F), parent(F, C).
mother(M, C) :- female(M), parent(M, C).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Grandparent and Aunt/Uncle Relationships
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
aunt_or_uncle(AU, N) :- sibling(AU, P), parent(P, N).
uncle(U, N) :- male(U), aunt_or_uncle(U, N).
aunt(A, N) :- female(A), aunt_or_uncle(A, N).

% Finding All Children of a Given Parent
children(Parent, Child) :- parent(Parent, Child).

% Great-Grandparent Relationships
great_grandparent(GGP, GGC) :- parent(GGP, GP), parent(GP, P), parent(P, GGC).

% Checking If Two Individuals Are Cousins
cousin(C1, C2) :- parent(P1, C1), parent(P2, C2), sibling(P1, P2), C1 \= C2.

% Adding Spouse Relationships and Marital Rules
% Spouse facts
spouse(john, linda).
spouse(linda, john). % Assuming marriage is bidirectional
spouse(peter, mary).
spouse(mary, peter).

% Married rule
married(X, Y) :- spouse(X, Y).

% Rule to find if a person is married
is_married(Person) :- spouse(Person, _).