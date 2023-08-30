from a2_log_delim import LogFile, DelimFile
from a2_csv_format import WriteFile, CSVFormatter, LogFormatter

log=LogFile('log.txt')

log.write('This is first alert')
log.write('This is second alert')

c=DelimFile('log.csv', ',')
c.write(['a','b','c','d'])
c.write(['1','2','3','4'])

wcsv=WriteFile('log2.csv', CSVFormatter)
wlog=WriteFile('log2.txt', LogFormatter)

wcsv.write(['a','b,2','c','d'])
wlog.write('This is first alert')

wcsv.close()
wlog.close()




