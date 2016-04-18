#!/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sun Apr 17 22:00:00 2016

@author: Victor Rodriguez

Python 2.7

This script calculates the score 0-100 scale and generates CSV file with the scores based
in the transformation of scores ESPOL.

Also, it allow calculate the score 0-100 to GPA EEUU
"""

import getopt, sys, csv

# GPA = {key=U.S Grade, value=point}
GPA = {
        'A+': 4.3,
        'A':  4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B':  3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C':  2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D':  1.0,
        'D-': 0.7,
        'F':  0.0}

def gpaEEUU(score):
    l = ''
    if   93 <= score <= 100: l = 'A';
    elif 90 <= score < 93:  l = 'A-';
    elif 87 <= score < 90:  l = 'B+';
    elif 83 <= score < 87:  l = 'B';
    elif 80 <= score < 83:  l = 'B-';
    elif 77 <= score < 80:  l = 'C+';
    elif 73 <= score < 77:  l = 'C';
    elif 70 <= score < 73:  l = 'C-';
    elif 67 <= score < 70:  l = 'D+';
    elif 63 <= score < 67:  l = 'D';
    elif 60 <= score < 63:  l = 'D-';
    elif score < 60:        l = 'F';
    return [l, GPA[l]]

def gpaESPOL(score):
    l = ''
    if   90 <= score <= 100:  l = 'A+';
    elif 80 <= score < 90:    l = 'A';
    elif 70 <= score < 80:    l = 'B+';
    elif 65 <= score < 70:    l = 'B';
    elif 60 <= score < 65:    l = 'C';
    elif score < 60:          l = 'F';
    return [l, GPA[l]]

def main(argv):

    ### Put the arguments in variables.
    gpaFinal = ''
    totalScore = 0
    totalCredts = 0
    totalGPA = 0
    finalGPA = 0
    totalPoints = 0

    scoreFilename = ''
    type  = ''
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv,"hs:t:o:",["scores=", "type=","output="])
    except getopt.GetoptError:
        print 'score100_to_gpa.py -s <scoreFile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'score100_to_gpa.py -s <scoreFile>'
            sys.exit()
        elif opt in ("-s", "--scoreFile"):
            scoreFilename = arg

        elif opt in ("-t", "--type"):
            if arg.lower() in ['eeuu', 'ee.uu', 'espol']:
                type = arg
            else:
                print 'Write one the type: \'EE.UU\' or \'ESPOL\''
                sys.exit()
        elif opt in ("-o", "--output"):
            if arg == '':
                outputFile = scoreFilename + "-gpa.csv"
            else:
                outputFile = arg
    if scoreFilename == '':
        print 'ERROR: Must specify a score file.'
        print 'score100_to_gpa.py -s <scoreFile>'
        sys.exit(1)

    if ('-o', '--output') not in opts:
        outputFile = scoreFilename + "-gpa.csv"

    # CSV File: signature, credits, score
    with open (scoreFilename, "r") as scoreFile:
        with open(outputFile, 'w') as  gpaFile:
            reader = csv.reader(scoreFile, delimiter=',')
            sf = csv.writer(gpaFile, delimiter=',')
            for line in reader:
                c = int(line[1])
                s = float(line[2]) * 10
                r_gpa = gpaESPOL(s) if (type == 'espol')  else gpaEEUU(s)
                line.append(str(r_gpa[1]))
                line.append(r_gpa[0])
                totalScore += s
                totalCredts+= c
                totalGPA += r_gpa[1]
                totalPoints += (c * r_gpa[1])
                sf.writerows([line])
            finalGPA = totalPoints / totalCredts
            usGPA = gpaESPOL(finalGPA * 25)[0] if (type == 'espol') else gpaEEUU(finalGPA * 25)[0]
            r = ['Total']
            r.append(str(totalCredts))
            r.append(str(totalScore))
            r.append(usGPA)
            r.append(str(finalGPA))
            sf.writerows([r])
            gpaFile.close();
        scoreFile.close();

    print 'Sum total Score: {}'.format(totalScore)
    print 'Sum total credits: {}'.format(totalCredts)
    print 'Sum total GPAs: {}'.format(totalGPA)
    print 'Total Points: {}'.format(totalPoints)
    print 'U.S. GPA: {}'.format(usGPA)
    print 'GPA score: {} / 4.0'.format(finalGPA)

if __name__ == "__main__":
   main(sys.argv[1:])