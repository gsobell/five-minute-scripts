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
    S[Sesame seeds]
    T[Tahina]


    subgraph Veggies + Proteins
    A  --> D & E & Q
    Q & D & E -->  F & H
    D & E --> Q
    D --> E
    end
    subgraph Spices
    A & Q & D & E & F & H --> I
    I --> J & K & L & S
    J & K & S-->  L
    F --> H
    S --> K & J

    end
    subgraph Herbs
    I & J & K & L & S --> M & N
    M --> N
    end
    subgraph Dressings
    I & J & K & L & M & N -->
    R & O -->
    P & T & B[Mix well]
    P & T--> B
    end
    B --> C[Enjoy!]

    ```
