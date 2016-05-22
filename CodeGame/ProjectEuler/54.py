#!/usr/local/bin/python3
import sys
from functools import total_ordering, reduce


@total_ordering
class Card:

    def __str__(self):
        return self.value + self.suit

    def __init__(self, cardStr):
        """
        >>> Card("10S").value
        '10'
        >>> Card("10S").suit
        'S'
        >>> Card("AS").value
        'A'
        >>> Card("AS").suit
        'S'
        """
        self.value = cardStr[0:len(cardStr) - 1]
        self.suit = cardStr[-1]

    def __lt__(self, other):
        """
        >>> Card("5H") < Card("6C")
        True
        >>> Card("5H") < Card("AC")
        True
        >>> Card("KC") < Card("AS")
        True
        >>> Card("AC") <= Card("AS")
        True
        >>> Card("AC") >= Card("AS")
        True
        >>> Card("JC") > Card("10C")
        True
        """
        return Card.intValue(self) < Card.intValue(other)

    def __eq__(self, other):
        """
        >>> Card("5H") == Card("5C")
        True
        >>> Card("4H") == Card("5H")
        False
        """
        return self.value == other.value

    @classmethod
    def intValue(cls, card):
        """
        >>> Card.intValue(Card('AS'))
        14
        >>> Card.intValue(Card('TH'))
        10
        >>> Card.intValue(Card('2H'))
        2
        """

        if card.value == 'A':
            return 14
        if card.value == 'K':
            return 13
        if card.value == 'Q':
            return 12
        if card.value == 'J':
            return 11
        if card.value == 'T':
            return 10

        return int(card.value)

    def points(self):
        return Card.intValue(self)


@total_ordering
class Hand:

    def __str__(self):
        strVal = "[ "
        for c in self.cards:
            strVal += str(c)
            strVal += " "
        strVal += "]"
        return strVal

    def __init__(self, cards):
        self.cards = list(map(lambda x: Card(x), cards))

    def __lt__(self, other):
        return self.handIntValue() < other.handIntValue()

    def __eq__(self, other):
        return self.handIntValue() == other.handIntValue()

    def handIntValue(self):
        """
        >>> Hand(['10S', 'JS', 'QS', 'AS', 'KS']).handIntValue()
        90000
        >>> Hand(['10S', 'JS', 'QS', '9S', 'KS']).handIntValue()
        81300
        >>> Hand(['10S', '10D', '10H', '10C', 'KS']).handIntValue()
        71013
        >>> Hand(['JS', 'JD', 'JH', 'QC', 'QS']).handIntValue()
        61112
        >>> Hand(['JS', 'QS', '2S', '4S', '7S']).handIntValue()
        51200
        >>> Hand(['JS', '10C', '7D', '9S', '8H']).handIntValue()
        41100
        >>> Hand(['JS', 'JC', 'JD', '8S', '9H']).handIntValue()
        31109.08
        >>> Hand(['JS', 'JC', '8D', '8S', '9H']).handIntValue()
        21108.09
        >>> Hand(['KS', '2C', '8D', '8S', '9H']).handIntValue()
        10813.0902
        >>> Hand(['AS', '2C', '4D', '8S', 'JH']).handIntValue() - 1411.080402 < 0.0001
        True
        """

        DEBUG = False
        if DEBUG:
            print("analysing hand ", self)

        handValue = 0
        composition = self.countByValue()
        if self.isRoyalFlush():
            if DEBUG:
                print("Royal Flush")
            handValue += 9 * 10**4
        elif self.isStraightFlush():
            if DEBUG:
                print("Straight Flush")
            handValue += 8 * 10**4
            biggestCard = reduce(max, map(lambda x: x.points(), self.cards))
            handValue += biggestCard * 10**2
        elif self.isFourOfAKind():
            if DEBUG:
                print("Four of a Kind")
            foakCard = list(filter(
                lambda x: x[1] == 4,
                composition.items()))[0]
            singleCard = list(filter(
                lambda x: x[1] == 1,
                composition.items()))[0]
            handValue += 7 * 10**4
            handValue += Card(foakCard[0] + "S").points() * 10**2
            handValue += Card(singleCard[0] + "S").points()
        elif self.isFullHouse():
            if DEBUG:
                print("Full House")
            fullCard = list(filter(
                lambda x: x[1] == 3,
                composition.items()))[0]
            pairCard = list(filter(
                lambda x: x[1] == 2,
                composition.items()))[0]
            handValue += 6 * 10**4
            handValue += Card(fullCard[0] + "S").points() * 10**2
            handValue += Card(pairCard[0] + "S").points()
        elif self.isFlush():
            if DEBUG:
                print("Flush")
            biggestCard = reduce(max, map(lambda x: x.points(), self.cards))
            handValue += 5 * 10**4
            handValue += biggestCard * 10**2
        elif self.isStraight():
            if DEBUG:
                print("Straight")
            biggestCard = reduce(max, map(lambda x: x.points(), self.cards))
            handValue += 4 * 10**4
            handValue += biggestCard * 10**2
        elif self.isThreeOfAKind():
            if DEBUG:
                print("Three of a kind")
            toakCard = list(filter(
                lambda x: x[1] == 3,
                composition.items()))[0]
            singleCardPoints = list(map(
                lambda x: Card(x[0] + "S").points(),
                filter(
                    lambda x: x[1] == 1,
                    composition.items())))
            singleCardPoints.sort()
            singleCardPoints.reverse()

            handValue += 3 * 10**4
            handValue += Card(toakCard[0] + "S").points() * 10**2
            handValue += singleCardPoints[0]
            handValue += singleCardPoints[1] * 10**-2
        elif self.isTwoPairs():
            if DEBUG:
                print("Two pairs")
            pairCardPoints = list(map(
                lambda x: Card(x[0] + "S").points(),
                filter(
                    lambda x: x[1] == 2,
                    composition.items())))
            pairCardPoints.sort()
            pairCardPoints.reverse()
            singleCard = list(filter(
                lambda x: x[1] == 1,
                composition.items()))[0]

            handValue += 2 * 10**4
            handValue += pairCardPoints[0] * 10**2
            handValue += pairCardPoints[1]
            handValue += Card(singleCard[0] + "S").points() * 10**-2
        elif self.isOnePair():
            if DEBUG:
                print("One pairs")
            pairCard = list(filter(
                lambda x: x[1] == 2,
                composition.items()))[0]
            singleCardPoints = list(map(
                lambda x: Card(x[0] + "S").points(),
                filter(
                    lambda x: x[1] == 1,
                    composition.items())))
            singleCardPoints.sort()
            singleCardPoints.reverse()

            handValue += 1 * 10**4
            handValue += Card(pairCard[0] + "S").points() * 10**2
            handValue += singleCardPoints[0]
            handValue += singleCardPoints[1] * 10**-2
            handValue += singleCardPoints[2] * 10**-4
        else:
            if DEBUG:
                print("Nothing")
            singleCardPoints = list(map(
                lambda x: Card(x[0] + "S").points(),
                filter(
                    lambda x: x[1] == 1,
                    composition.items())))
            singleCardPoints.sort()
            singleCardPoints.reverse()

            handValue += singleCardPoints[0] * 10**2
            handValue += singleCardPoints[1]
            handValue += singleCardPoints[2] * 10**-2
            handValue += singleCardPoints[3] * 10**-4
            handValue += singleCardPoints[4] * 10**-6

        if DEBUG:
            print("handValue: ", handValue)

        return handValue

    @classmethod
    def countListItems(cls, items):
        count = {}
        for item in items:
            if item in count.keys():
                count[item] += 1
            else:
                count[item] = 1

        return count

    def countByValue(self):
        return Hand.countListItems(list(map(lambda x: x.value, self.cards)))

    def isOnePair(self):
        """
        >>> Hand(["2S", "5S", "2D", "3H", "4C"]).isOnePair()
        True
        >>> Hand(["2S", "3S", "2D", "3H", "4C"]).isOnePair()
        False
        >>> Hand(["6S", "5S", "4D", "3H", "2C"]).isOnePair()
        False
        """
        return (2 in self.countByValue().values() and
                not self.isTwoPairs())

    def isTwoPairs(self):
        """
        >>> Hand(["2S", "3S", "2D", "3H", "4C"]).isTwoPairs()
        True
        >>> Hand(["5S", "5S", "4D", "3H", "2C"]).isTwoPairs()
        False
        """
        items = Hand.countListItems(self.countByValue().values())
        return 2 in items.keys() and items[2] == 2

    def isThreeOfAKind(self):
        """
        >>> Hand(["2S", "3S", "4D", "4H", "4C"]).isThreeOfAKind()
        True
        >>> Hand(["5S", "5S", "4D", "4H", "4C"]).isThreeOfAKind()
        False
        """
        return (3 in self.countByValue().values() and
                not self.isFullHouse())

    def isStraight(self):
        """
        >>> Hand(["2S", "4S", "3S", "6S", "5S"]).isStraight()
        False
        >>> Hand(["2S", "7S", "3S", "6S", "5S"]).isStraight()
        False
        >>> Hand(["2S", "4H", "3S", "6S", "5S"]).isStraight()
        True
        >>> Hand(["10S", "JS", "AS", "KS", "QS"]).isStraight()
        False
        """

        cardIntValues = list(map(lambda x: Card.intValue(x), self.cards))
        cardIntValues.sort()
        minCard = cardIntValues[0]
        cardIntValues = list(map(lambda x: x - minCard, cardIntValues))
        return (not self.hasSingleSuit() and
                cardIntValues == [0, 1, 2, 3, 4])

    def isFlush(self):
        """
        >>> Hand(["2S", "4S", "7S", "QS", "AS"]).isFlush()
        True
        >>> Hand(["2S", "4S", "7C", "QS", "AS"]).isFlush()
        False
        >>> Hand(["2S", "4S", "3S", "5S", "6S"]).isFlush()
        False
        """
        return self.hasSingleSuit() and not self.isStraightFlush()

    def isFullHouse(self):
        """
        >>> Hand(["2S", "2D", "4D", "4H", "4C"]).isFullHouse()
        True
        >>> Hand(["2S", "3D", "4D", "4H", "4C"]).isFullHouse()
        False
        """
        cardCounts = self.countByValue().values()
        return (3 in cardCounts and
                2 in cardCounts)

    def isFourOfAKind(self):
        """
        >>> Hand(["2S", "4S", "4D", "4H", "4C"]).isFourOfAKind()
        True
        >>> Hand(["2S", "5S", "4D", "4H", "4C"]).isFourOfAKind()
        False
        """
        return 4 in self.countByValue().values()

    def isStraightFlush(self):
        """
        >>> Hand(["2S", "4S", "3S", "6S", "5S"]).isStraightFlush()
        True
        >>> Hand(["2S", "7S", "3S", "6S", "5S"]).isStraightFlush()
        False
        >>> Hand(["2S", "4H", "3S", "6S", "5S"]).isStraightFlush()
        False
        >>> Hand(["10S", "JS", "AS", "KS", "QS"]).isStraightFlush()
        False
        """

        cardIntValues = list(map(lambda x: Card.intValue(x), self.cards))
        cardIntValues.sort()
        return (self.hasSingleSuit() and
                cardIntValues[4] - cardIntValues[0] == 4 and
                not self.isRoyalFlush())

    def isRoyalFlush(self):
        """
        >>> Hand(["10S", "JS", "AS", "KS", "QS"]).isRoyalFlush()
        True
        >>> Hand(["10S", "JS", "AC", "KS", "QS"]).isRoyalFlush()
        False
        >>> Hand(["10S", "JS", "9S", "KS", "QS"]).isRoyalFlush()
        False
        """

        cardValues = list(map(lambda x: x.value, self.cards))
        return (self.hasSingleSuit() and
                "10" in cardValues and
                "J" in cardValues and
                "Q" in cardValues and
                "K" in cardValues and
                "A" in cardValues)

    def hasSingleSuit(self):
        """
        >>> Hand(["5S", "4S", "AS", "KS", "10S"]).hasSingleSuit()
        True
        >>> Hand(["5S", "4S", "AC", "KS", "10S"]).hasSingleSuit()
        False
        """

        firstSuit = self.cards[0].suit
        return len(list(filter(lambda x: x.suit == firstSuit, self.cards))) == 5


def main():
    f = open(sys.argv[1], 'r')
    count = 0
    tot = 0
    plays = map(lambda x: x.replace('\n', ''), f.readlines())
    for play in plays:
        cards = play.split(' ')
        player1 = Hand(cards[0:5])
        player2 = Hand(cards[5:])

        tot += 1
        if player1 > player2:
            print("player 1 wins")
            count += 1
        else:
            print("player 1 loses")
        print("\n")

    print("Player 1 won ", count, " out of ", tot, " plays")


if __name__ == "__main__":
    main()
