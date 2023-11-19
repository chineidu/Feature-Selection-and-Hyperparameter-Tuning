# AB Testing

## Table of Content

- [AB Testing](#ab-testing)
  - [Table of Content](#table-of-content)
  - [Types of Conitional Probabilities](#types-of-conitional-probabilities)
    - [Marginal distribution](#marginal-distribution)
    - [Joint distribution](#joint-distribution)
    - [Independent Probability](#independent-probability)
    - [Independent And Identically Distributed](#independent-and-identically-distributed)
    - [Bayes Theorem](#bayes-theorem)
    - [Click Through Rate (CTR)](#click-through-rate-ctr)
    - [Conversion Rate](#conversion-rate)
  - [Hypothesis Testing](#hypothesis-testing)
    - [Examples](#examples)
      - [1) Testing the impactfulness of a new drug](#1-testing-the-impactfulness-of-a-new-drug)
      - [2) Testing the impactfulness of a new web page](#2-testing-the-impactfulness-of-a-new-web-page)
    - [Notation](#notation)
    - [Types of Hypothesis Tests](#types-of-hypothesis-tests)
  - [Statistical Significance](#statistical-significance)
  - [Hypothesis Function](#hypothesis-function)
    - [P-value](#p-value)
      - [Type I Error](#type-i-error)
      - [Type II Error](#type-ii-error)
    - [More Examples (hypothesis testing)](#more-examples-hypothesis-testing)
      - [1.) Drug testing](#1-drug-testing)
      - [2.) Daily stock](#2-daily-stock)
    - [Statistical Vs. Practical Significance](#statistical-vs-practical-significance)
    - [Accept or Reject](#accept-or-reject)

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

### Bayes Theorem

$$p(A|B) = \frac{p(A|B).p(A)}{p(B)}$$

### Click Through Rate (CTR)

- Number of clicks per number of impressions.

- CTR = (no of clicks) / (no of impressions)

### Conversion Rate

- conversion_rate = (number of desired actions) / (number of page visits)

## Hypothesis Testing

### Examples

#### 1) Testing the impactfulness of a new drug

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

#### 2) Testing the impactfulness of a new web page

```text
- We have 2 web page designs and we want to know which page users spend more time on.
- We might want to split the users into 2 groups (control and test) and record how long users in each group spend on the web page.
```

### Notation

- In a `2-sample test` (for a drug test)

- Null Hypothesis ($H_0$):
  $$H_0 : \mu_1 = \mu_2$$

- Alternative Hypothesis ($H_1$):
  $$H_1 : \mu_1 \neq \mu_2$$

### Types of Hypothesis Tests

- **2 groups of data**: `2 sample test`. e.g. control group vs treatment group.

- **1 group of data**: `1-sample test`. e.g. stock return vs fixed value.

- **2 sided test**:
  - $\mu_1 > \mu_2$ can be significant.
  - $\mu_1 < \mu_2$ can be significant.
  - $H_0 : \mu_1 = \mu_2$
  - $H_1 : \mu_1 \neq \mu_2$ (i.e. $\mu_1 < \mu_2$  or $\mu_1 > \mu_2$)

- **1 sided test**:
  - $\mu_1 > \mu_2$ can be significant.
  - $H_0 : \mu_1 \leq \mu_2$
  - $H_1 : \mu_1 > \mu_2$

## Statistical Significance

- When comparing groups, we can't just compare only the averages.
- 3 variables are important:
  - Number of samples collected.
  - Variance of the samples.
  - Difference in the size. e.g. difference in means (averages)

## Hypothesis Function

- Given the data:
  - 1-sample test: $x$
  - 2-sample test: $x_1, x_2$

```python
# Statsmodels
ztest(x) # 1-sample test
ztest(x_1, x_2) # 2-sample test


# Scipy
ttest_1samp(x) # 1-sample test
ttest_ind(x_1, x_2) # 2-sample test
```

- The output tells us whether or not the difference is `statistically significant`.

### P-value

- This is the probability of observing a result as extreme or more extreme than what was observed assuming the null hypothesis is true.
- e.g. the null hypothesis is that the (true) mean stock is 0. If the observed (measured) average daily stock return was 100bp with variance of 10.
- The `p-value` would be very small if the null hypothesis were to be false.
- Generally, the `p-value` is compared to a significant threshold/level.

#### Type I Error

- Definition: Rejecting a `true` null hypothesis.
- Probability of making the error: Alpha ($\alpha$)

#### Type II Error

- Definition: Failing to reject a `false` null hypothesis.
- Probability of making the error: Beta ($\beta$)

### More Examples (hypothesis testing)

#### 1.) Drug testing

- We're testing a drug.
- Control is group A, treatment is group B.
- We select a significance threshold of 5%.
- We obtain a `p-value` of 0.01.
- Since 0.01 < 0.05, the effect of the treatment is statistically significant.

#### 2.) Daily stock

- We check if the mean daily stock return is greater than 0.
- We select a significance threshold of 1%.
- Since 0.1 > 0.01, even if the average daily stock is greater than 0, the difference is not statistically significant.

### Statistical Vs. Practical Significance

- Statistical significance does not imply practical significance.
- e.g. if a drug increases the lifespan by 1 second but costs billions of USD, is it a practical investment? NAH!
- iff the click through rate of one ad is 1.1% and the click through rate of another ad is 1%, it may lead to an appreciable increase in revenue.

### Accept or Reject

- If the `p-value` is below the significance threshold, the we **`reject`** the null hypothesis.
- If the `p-value` is above the significance threshold, we **`fail to reject`** the null hypothesis.
