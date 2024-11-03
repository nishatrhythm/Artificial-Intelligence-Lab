% Hello World program in Prolog
hello_world :-
    write('Hello, World!').

% Take name as input, and greet someone
greet :-
    write('What is your name? '),
    read(Name),
    format('Hello, ~w!', [Name]).

% Say goodbye someone
goodbye :-
    write('Goodbye!').

% Take name and age as input, and greet someone
greet_with_age :-
    write('What is your name? '),
    read(Name),
    write('How old are you? '),
    read(Age),
    format('Hello, ~w! You are ~w years old.', [Name, Age]).

% Arithmetic operations
add(X, Y, Result) :- Result is X + Y.
subtract(X, Y, Result) :- Result is X - Y.

% Factorial calculation
factorial(0, 1).
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, SubResult),
    Result is N * SubResult.

% Square of a Number
square(X, Result) :- Result is X * X.

% nth Fibonacci number
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, R1),
    fibonacci(N2, R2),
    Result is R1 + R2.

% If-Else Statements
is_even(X) :-
    0 is X mod 2,
    write('Even').
is_even(X) :-
    1 is X mod 2,
    write('Odd').

% Comparison Operators
is_greater(X, Y) :-
    X > Y,
    write('X is greater than Y').
is_greater(X, Y) :-
    X =< Y,
    write('X is not greater than Y').

% Check Positive, Negative, or Zero
check_number(X) :-
    X > 0, write('Positive').
check_number(X) :-
    X < 0, write('Negative').
check_number(0) :-
    write('Zero').

% Check if a Given Year is a Leap Year
is_leap_year(Year) :-
    (Year mod 400 =:= 0 -> write('Leap year');
    Year mod 100 =:= 0 -> write('Not a leap year');
    Year mod 4 =:= 0 -> write('Leap year');
    write('Not a leap year')).

% Lists and Cut Operator
list_length([], 0).
list_length([_|T], Len) :-
    list_length(T, Len1),
    Len is Len1 + 1.

% Using Cut Operator
is_positive(X) :-
    X > 0,
    !.
is_positive(X) :-
    X =< 0.

% Find Maximum in a List
max_in_list([H], H).
max_in_list([H|T], Max) :-
    max_in_list(T, MaxTail),
    Max is max(H, MaxTail).

% Remove duplicates from a list
remove_duplicates([], []).
remove_duplicates([H|T], Result) :-
    member(H, T), % Check if H is in T
    remove_duplicates(T, Result).
remove_duplicates([H|T], [H|Result]) :-
    \+ member(H, T), % Check if H is not in T
    remove_duplicates(T, Result).

% Debugging Exercise
greater_than_ten(X) :-
    X > 10,
    write('Greater than 10').
greater_than_ten(X) :-
    X =< 10,
    write('Not greater than 10').

% Identify and correct the errors in the greater_than_ten predicate
greater_than_ten_corrected(X) :-
    (X > 10 -> write('Greater than 10');
    write('Not greater than 10')).

% Debug a faulty program that is intended to find the sum of elements in a list
