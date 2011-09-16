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
    stop_dictionary = collections.defaultdict(int) 
    for i in xrange(trials):
        foo = no_set.SetGame(with_replacement=False)
        draws = 0
        hand = no_set.exists_set(foo.get_board())
        while hand:
            if len(foo.cards) == 0:
                #print "board: %s" % foo.get_board()
                partition = no_set.exists_partition(foo.get_board())
                if partition:
                    #print "partition: %s" % partition
                    count += 1
                break
            foo.play_set(*hand)
            hand = no_set.exists_set(foo.get_board())
            draws += 1
        stop_dictionary[draws] += 1
    print "Count of perfect games: %d, Percentage of perfect games: %f" % (count, count/float(trials))
    print stop_dictionary

if __name__ == '__main__':
    main()


