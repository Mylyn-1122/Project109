from os import stat
import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")

#math

mathScores = df['math score'].to_list()

mathScoreMean = statistics.mean(mathScores)
mathScoreMedian = statistics.median(mathScores)
mathScoreMode = statistics.mode(mathScores)
mathScoreSTDev = statistics.stdev(mathScores)

math_first_std_start, math_first_std_end = mathScoreMean-mathScoreSTDev, mathScoreMean+mathScoreSTDev
math_second_std_start, math_second_std_end = mathScoreMean-(2*mathScoreSTDev), mathScoreMean+(2*mathScoreSTDev)
math_list_one_STDev = [result for result in mathScores if result > math_first_std_start and result < math_first_std_end]
math_list_two_STDev = [result for result in mathScores if result > math_second_std_start and result < math_second_std_end]

print("[Math]", 'mean : ', mathScoreMean,', median : ', mathScoreMedian,', mode : ', mathScoreMode,', stdev : ',  mathScoreSTDev)
print("{}% of student math test scores in the data lies between 1st deviation ".format(len(math_list_one_STDev)*100/len(mathScores)))
print("{}% of student math test scores in the data lies between 2nd deviation ".format(len(math_list_two_STDev)*100/len(mathScores)))

#reading
readingScores = df['reading score'].to_list()

readingScoreMean = statistics.mean(readingScores)
readingScoreMedian = statistics.median(readingScores)
readingScoreMode = statistics.mode(readingScores)
readingScoreSTDev = statistics.stdev(readingScores)

reading_first_std_start, reading_first_std_end = readingScoreMean-readingScoreSTDev, readingScoreMean+readingScoreSTDev
reading_second_std_start, reading_second_std_end = readingScoreMean-(2*readingScoreSTDev), readingScoreMean+(2*readingScoreSTDev)
reading_list_one_STDev = [result for result in readingScores if result > reading_first_std_start and result < reading_first_std_end]
reading_list_two_STDev = [result for result in readingScores if result > reading_second_std_start and result < reading_second_std_end]

print('  ')
print("[Reading]", 'mean : ', readingScoreMean,', median : ', readingScoreMedian,', mode : ', readingScoreMode,', stdev : ',  readingScoreSTDev)
print("{}% of student reading test scores in the data lies between 1st deviation ".format(len(reading_list_one_STDev)*100/len(readingScores)))
print("{}% of student reading test scores in the data lies between 2nd deviation ".format(len(reading_list_two_STDev)*100/len(readingScores)))

#writing
writingScores = df['writing score'].to_list()

writingScoreMean = statistics.mean(writingScores)
writingScoreMedian = statistics.median(writingScores)
writingScoreMode = statistics.mode(writingScores)
writingScoreSTDev = statistics.stdev(writingScores)

writing_first_std_start, writing_first_std_end = writingScoreMean-writingScoreSTDev, writingScoreMean+writingScoreSTDev
writing_second_std_start, writing_second_std_end = writingScoreMean-(2*writingScoreSTDev), writingScoreMean+(2*writingScoreSTDev)
writing_list_one_STDev = [result for result in writingScores if result > writing_first_std_start and result < writing_first_std_end]
writing_list_two_STDev = [result for result in writingScores if result > writing_second_std_start and result < writing_second_std_end]

print('  ')
print("[Writing]", 'mean : ', writingScoreMean,', median : ', writingScoreMedian,', mode : ', writingScoreMode,', stdev : ',  writingScoreSTDev)
print("{}% of student writing test scores in the data lies between 1st deviation ".format(len(writing_list_one_STDev)*100/len(writingScores)))
print("{}% of student writing test scores in the data lies between 2nd deviation ".format(len(writing_list_two_STDev)*100/len(writingScores)))