# Personal Finance Manager

## Used design patterns

### Singleton pattern

We use a singleton patter on the balance to avoid starting new balances during the application executing. The balance is unique to the user and any
income or expense should be added to the same balance.

### Observer pattern

We use the observer pattern to notifiy other sections of the aplication about newly created transactions, allowing to have a single place to update
all interested section without having to know how this sections want to be notified.

### Adapter pattern

Allows to normalize the shape of the transaction and to continue to accept different types of transactions if needed.

### Factory pattern

I've added the Factory pattern to create multiple BalanceObservers. This allows me to continue extending the observer types of the application
without coupling th eclass creating on the client code.
