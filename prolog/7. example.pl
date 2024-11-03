sells(mila, egg).
sells(jony, apple).
sells(john, bread).
buys(niloy, egg).
buys(tommy, bread).

mila_sells(Product) :- buys(niloy, Product).
tommy_buys(Person) :- sells(Person, bread).



father(rahim, kamal).
father(kashem, rahim).
father(rahman, kashem).
father(someone, rahman).

% grandfather(kashem, kamal) :- father(kashem, rahim), father(rahim, kamal).
grandfather(X, Y) :- father(X, rahim), father(rahim, Y).