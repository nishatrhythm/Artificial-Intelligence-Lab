parent(john, mary).
parent(jane, mary).
parent(mary, tom).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).