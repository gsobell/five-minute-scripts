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

    subgraph Veggies + Proteins
    A  --> D & E & Q
    D & E --> Q
    D --> E
    Q & D & E -->  F & H
    end
    subgraph Spices
    A & Q & D & E & F & H --> I
    F --> H
    I ---> J & K & L
    J & K -->  L
    J --> K
    end
    subgraph Herbs
    I & J & K & L ---> M & N
    M ---> N
    end
    subgraph Dressings
    I & J & K & L & M & N --> R & O --> P & B[Mix well]
    end
    P --> B
    B --> C[Enjoy!]
```
