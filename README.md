# Fodboldtur

## Flowcharts
Første flowchart over programmet:

"image"

Andet flowchart over programmet

"image"

## Changes Made

The beginning state of the program used function calls to create the effect of an infinite loop, which worked in their case. However it is important to note, that it made the program harder to maintain or modify safely. Take the example:

```py
def modtag_betaling():
navn = input("Indtast navnet på personen der betaler (Skriv 'b', hvis du ønsker at gå tilbage): ")
        if navn in navne:
            menu()
        else:
            print("Ikke et validt navn")
            modtag_betaling()
...
```
In this scenario, the recursive function call to ```modtag_betaling``` will remain on the call stack forever and take up memory. If the program is running for long enough and doing multiple of these recursive calls, the call stack will eventually run out of space, and the program will crash. Instead I opted for a while loop based fix as seen below:
```py
def def modtag_betaling():
    kør = True
    while kør:
        navn = input("Indtast navnet på personen der betaler (Skriv 'b', hvis du ønsker at gå tilbage): ")
        if navn == "b":
            break

        if navn in navne:
            break
        else:
            print("Ikke et validt navn")
...
```
This can catch errors forever and never cause a stack overflow.