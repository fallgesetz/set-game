#!/usr/bin/env python
import no_set
import optparse
import collections


def main():
    parser = optparse.OptionParser()
    parser.add_option("-t", dest="trials", type="int", default="1000")

    options, args = parser.parse_args()

    trials = options.trials
    count = 0 
    for i in xrange(trials):
        foo = no_set.SetGame(with_replacement=False)
        hand = no_set.exists_set(foo.get_board())
        while hand:
            if len(foo.cards) == 0:
                if no_set.exists_partition(foo.get_board()):
                    count += 1
                break
            foo.play_set(*hand)
            hand = no_set.exists_set(foo.get_board())
    print count

if __name__ == '__main__':
    main()


