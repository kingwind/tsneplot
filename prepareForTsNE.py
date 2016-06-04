#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', action='store', dest='embedFile', required=True,
                        help='Path of embed results')

    parser.add_argument('-l', action='store', dest='outputLabel', required=True,
                        help='Path of output lable file')

    parser.add_argument('-x', action='store', dest='outputEmbedding',
                        required=True,
                        help='Path of output vector results for sample words')

    parser.add_argument('-s', action='store', dest='sampleFile', required=True,
                        help='Path of sample file to visualize by t-SNE')

    r = parser.parse_args()

    wordCount = {}  # Counter() is not availabe in Python 2.6.6

    with open(r.sampleFile, "r") as wordFile:
        for line in wordFile:
            for w in line.lower().split():
                wordCount[w] = wordCount.get(w, 0) + 1

    labels = list(wordCount.keys())

    with open(r.embedFile, "r") as fInput:
        with open(r.outputLabel, "w") as fOutputLabel:
            with open(r.outputEmbedding, "w") as fOutputEmbed:
                lineCount, dimension = [int(x) for x in next(fInput).split()]

                wordDict = dict((k, v.strip())
                                for k, v in (l.split(' ', 1) for l in fInput)
                                if k in wordCount)

                for key in labels:
                    if key in wordDict:
                        fOutputLabel.write("%s\n" % key)
                        fOutputEmbed.write("%s\n" % wordDict[key])
                    else:
                        print("Key %s not found in embedding" % key)
