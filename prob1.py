#!/usr/bin/env python
import no_set
import optparse

"""
The probability of there not being a set definitely depends on which draw it is.

Or does it? What about exchangability
TODO: look up exchangability
TODO: look up hypothesis testing
"""
def main():
    parser = optparse.OptionParser()
    parser.add_option("-t", dest="trials", type="int", default="1000")
    parser.add_option("-d", dest="draw", type="int", default="1")

    options, args = parser.parse_args()

    trials = options.trials
    draw = options.draw

    has_set = 0
    for i in xrange(trials):
        foo = no_set.SetGame(with_replacement=False)
        for k in xrange(1,draw):
            foo.get_board()
            foo.wipe_board()
        if no_set.exists_set(foo.get_board()):
            has_set += 1

    existence_prob = has_set/float(trials)
    print "Trials: %d, Draw: %d" % (trials, draw)
    print "Probability of a set existing in the %dth draw: %f" % (draw, existence_prob)
    print "Probability of a set not existing in the %dth draw: %f" % (draw, 1 - existence_prob)
    print "1/33: %f" % (1.0/33.0)

if __name__ == '__main__':
    main()

