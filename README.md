# Pokerman

TL;DR, predicting poker hands.

## The Problem

Given the sequence of 5 'community' cards, drawn from a standard deck of cards, what hand is most likely present with at least one of the players in the game.

## Why?
```
Diligence is the mother of good luck. 
                            - Benjamin Franklin
```

## Poker Hands

Texas Hold Em is played by dealing each player 2 cards (face down), called the `hole` cards, and dealing 5 `community` cards (face up), on the table.

The player makes a poker `hand` using any combination of the 3 cards dealt to them, and the 5 cards on the table. 

The player with the strongest hands wins. Most commonly accepted ranking of hands, strongest to weekest :

| Rank | Hand | Description |
| :--: | :--: | :---------: |
| 0 | Royal Flush | `A K Q J 10` all of the same suit |
| 1 | Straight Flush | Any 5 cards of the same suit, in sequence |
| 2 | Four of a Kind | 4 cards of the same rank, like, `4 4 4 4` |
| 3 | Full House | A 3 of a kind, and a pair, of different ranks |
| 4 | Flush | Any 5 cards of the same suit |
| 5 | Straight | Any 5 cards in sequence |
| 6 | Three of a Kind | Any 3 cards of the same rank |
| 7 | Two Pair | Any 2 pairs of cards |
| 8 | One Pair | Any 2 cards of the same rank |
| 9 | High Card | Highest Ranked card in hand |


#### Ranking of Cards

A K Q J 10 9 8 7 6 5 4 3 2 1

## Data

This data was acquired from UCI's Machine Learning repository. The data comes already split into training and testing data.

Find it [here](https://archive.ics.uci.edu/ml/datasets/Poker+Hand).

#### Distribution of Test Data

![data image](https://github.com/aditisrinivas97/pokerman/blob/master/extras/Data%20Distribution.png)

Each bar represents the frequency of the corresponding hand as specified in the dataset description. 

##### NOTE: The hands' class labels are in the reverse order of their strength, i.e, 0 is the weakest hand.

#### Citation


> Dua, D. and Karra Taniskidou, E. (2017). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

## Machine Learning 🖥 🧐

| Model | Accuracy | Plot |
| :---: | :------: | :--: |
| Linear Regression | 42% | ![Regression image](https://github.com/aditisrinivas97/pokerman/blob/master/extras/Regression.png) |
| SVM | 58% | ![SVM image](https://github.com/aditisrinivas97/pokerman/blob/master/extras/svm.png) |
| Adaboost | 49% | ![Adaboost image](https://github.com/aditisrinivas97/pokerman/blob/master/extras/Adaboost.png) |
| Output Code Classifier | 61% | ![Output Code Classifier image](https://github.com/aditisrinivas97/pokerman/blob/master/extras/Output%20Code%20Classifier.png) |
| Random Forest | 56% | ![Random Forest image](https://github.com/aditisrinivas97/pokerman/blob/master/extras/Random%20Forest.png) |
| Artificial Neural Network | 45% | ![ANN image](https://github.com/aditisrinivas97/pokerman/blob/master/extras/ANN.png) |
| Deep Neural Network | 87% | ![DNN image](https://github.com/aditisrinivas97/pokerman/blob/master/extras/DNN.png) |
| Multi Layer Perceptron | 97% 🤯 | ![MLP image](https://github.com/aditisrinivas97/pokerman/blob/master/extras/Multi%20Layer%20Perceptron.png) |

## Conclusion

The Multi-layer Perceptron is clearly the best model for the dataset in hand. Here's the confusion matrix to provide us with some more insight into *how accurate* this model really was with its predictions.

![Multi Layer Perceptron Confusion Matrix](https://github.com/aditisrinivas97/pokerman/blob/master/extras/confMat.png)

## Primary Contributors

| | |
|:-:|:-:|
|<img src="https://github.com/aditisrinivas97.png" width="48">  | [Aditi Srinivas](https://github.com/aditisrinivas97) |
|<img src="https://github.com/avinashshenoy97.png" width="48">  | [Avinash Shenoy](https://github.com/avinashshenoy97) |