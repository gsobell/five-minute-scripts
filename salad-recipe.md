# salad-recipe.md
1. Small dice the vegetables
2. Mix in the protein of your choice [optional]
3. Finely chop the herbs [optional]
4. Add the spices
5. Mix well with two spoons

```
graph TD
    A[Tomato, Cucumber, Red Pepper]
    D[Red cabbage]
    E[Red onion]
    F[Chickpeas]
    H[Bulgarian cheese]
    I[Salt, Black pepper, Zaatar]
    J[Red pepper flakes]
    K[Cumin]
    L[Paprika]
    M[Parsley]
    N[Mint]
    R[Lemon juice]
    O[Balsamic]
    P[Olive oil]
    Q[Olives]

    A  --> D & E & Q
    D & E --> Q
    D --> E
    Q & D & E -->  F & H
    F --> H
    F & H --> I
    I ---> J & K & M & L 
    J & K -->  L
    J --> K
    J & K & L ---> M & N
    M ---> N
    I & J & K & L & M & N --> R & O --> P & B[Mix well] 
    P --> B
    B --> C[Enjoy!]
```
