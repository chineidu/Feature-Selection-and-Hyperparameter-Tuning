# Feature Selection Techniques

## Types

1. Filter Methods
2. Wrapper Methods
3. Embedded Methods

### Filter Methods

* They rely on the characteristics of the data.
* They typically do not depend on or use any ML algorithm.
* They're model agnostic.
* Less Computationall expensive.
* Used to quickly remove irrelevant features.
* They result in less predictive performance compared to other techniques.

### Wrapper Methods

* They use predictive ML algorithms to rank feature subset.
* They require training a model on each feature subset.
* Very computationally expensive.
* They usually provide the best performing feature subset for a given **`algorithm`**.
* They may not produce the best feature combination for a different ML algorithm.

### Embedded Methods

* Feature selection is performed as part of the model building process.
* They consider the interaction between the features and models.
* They're less computationally expensive than **wrapper methods** because they fit (train) the model only **once**.
