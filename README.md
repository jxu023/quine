## What's a quine?

A quine is a program that prints itself out when run.

Writing one was a lot of fun!
For anyone else looking to try it out ... I highly recommend it!
It's fun!
It also took me a few hours.

I put some hints at the bottom if you wanna try it while saving some time.
Don't scroll down if you want to avoid hints!

## Why write a quine?

It's a little puzzle!
Doing it was a lot of fun for me!

It's kind of like playing a game of catch-up or tag.
Each line you write has to be printed out later on.

## Why did I decide to write a quine?

https://blog.dave.tf/post/finding-bottom-turtle/ was a really interesting article I saw on hacker news.
It mentions a paper called "Reflections on Trusting Trust" which told me to try writing a quine first .. so I did!


## Filler

:)

=O

o_o
























## Hints

* Every piece of syntax you use to write your program must be printed out, in order to print all the syntax out, you must represent all of it as strings.
* You can use a definition bank to hold all the strings of things you need to print things out
* Make sure you're familiar with quotes, doc-string quotes, and escaping characters


## Some further thoughts

Could I make my quine hold arbitrary payloads?
... Isn't that very simmilar to a virus? ...

Could I write a quine-maker?
Feed the quine-maker an arbitrary program, which will produce a quine Q
then executes the program (or starts the long-running program) and then
prints itself out (perhaps in a seprate process).

Quine's not quite perfect, it still needs to reproduce comments.
Could I make do without superquotes? aka doc-strings.
How about C++ quine? or Haskell?
Do I really need everything in my definition bank? What could I cut out?
