#!/usr/bin/env python
import no_set
import optparse
import collections


def main():
    parser = optparse.OptionParser()
    parser.add_option("-t", dest="trials", type="int", default="1000")

    options, args = parser.parse_args()

    trials = options.trials
 
    draws_count = collections.defaultdict(int) 
    for i in xrange(trials):
        foo = no_set.SetGame(with_replacement=False)
        hand = no_set.exists_set(foo.get_board())
        count = 0
        while hand:
            foo.play_set(*hand)
            count += 1
            hand = no_set.exists_set(foo.get_board())
        draws_count[count] += 1
    print draws_count

if __name__ == '__main__':
    main()


