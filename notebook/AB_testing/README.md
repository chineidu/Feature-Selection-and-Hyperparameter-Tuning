# AB Testing

## Table of Content

- [AB Testing](#ab-testing)
  - [Table of Content](#table-of-content)
  - [Types of Conitional Probabilities](#types-of-conitional-probabilities)
    - [Marginal distribution](#marginal-distribution)
    - [Joint distribution](#joint-distribution)
    - [Independent Probability](#independent-probability)
    - [Independent And Identically Distributed](#independent-and-identically-distributed)
  - [Hypothesis Testing](#hypothesis-testing)
    - [Examples](#examples)
      - [1)](#1)
      - [2)](#2)

## Types of Conitional Probabilities

### Marginal distribution

Marginal distribution focuses on a single random variable, representing the probability of that variable's values without considering any other variables. It's like taking a slice of the overall probability distribution, examining the likelihood of each outcome for that particular variable, regardless of the values of other variables.

### Joint distribution

Joint probability distribution encompasses multiple random variables simultaneously. It describes the probability of specific combinations of values occurring for those variables. It's like viewing the probability distribution as a whole, considering how the values of different variables interact and influence each other's likelihood.

### Independent Probability

In probability theory, two events are considered independent if the occurrence of one does not affect the probability of the other. In other words, knowing that one event has happened does not change the likelihood of the other event happening.

### Independent And Identically Distributed

In probability theory and statistics, a collection of random variables is said to be independent and identically distributed (IID) if each random variable has the same probability distribution as the others and all are mutually independent.

- Independent means that the occurrence of one event does not affect the probability of any of the other events. For example, flipping a coin and getting heads does not make it more or less likely that you will get heads on the next flip.

- Identically distributed means that all of the random variables have the same probability distribution. For example, if you flip a fair coin, the probability of getting heads is 0.5 for each flip.

## Hypothesis Testing

### Examples

#### 1)

```text
- Imagine a scenario where you're trying to test the effectiveness of a new drug against an already existing drug.
- You may want to check if the new drug has an improvement over the standard treatment.
- The standard treatment might take µ_1 number of days before its impacts are felt.
- The new drug might take µ_2 days.
- In order to carryout the experiment, the drug users are split into 2:
  x.) Control group: those that take the standard treatment, placebo or nothing.
  x.) Treatement group: those that take the new drug or the new treatment.

- The goal is to find if there's any statistical difference between µ_1 and µ_2.
```

#### 2)

```text
- We have 2 web page designs and we want to know which page users spend more time on.
- We might want to split the users into 2 groups (control and test) and record how long users in each group spend on the web page.
```
