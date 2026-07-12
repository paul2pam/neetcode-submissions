class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = {}
        for card in hand:
            d[card] = d.get(card, 0) + 1

        hand = sorted(hand)

        for i in range(len(hand)):
            if d[hand[i]] == 0:
                continue
            for j in range(hand[i], hand[i] + groupSize):
                if d.get(j, 0) == 0:
                    print(f"{j} is returning false from {hand[i]}")
                    return False
                else:
                    d[j] -= 1
                    
        return True
        
