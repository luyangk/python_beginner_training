positive_words = ['success','great','excellent','positive','good','perfect']

def read_report(report_file):
  report_data = ''
  with open(report_file, 'r') as f:
    for line in f:
      report_data += ' ' + line.lower().strip()
  return report_data

def count_positive(report):
  total_counts = 0
  positive_counts = 0
  for word in report.split(' '):
    if len(word) == 0:
      continue
    total_counts += 1
    if word in positive_words:
      positive_counts += 1
  return (total_counts, positive_counts)

def positive_ratio(report_file):
  report_data = read_report(report_file)
  total, positive = count_positive(report_data)
  if total <= 0 or positive < 0:
    print("Word count error - total: " + str(total) + ", positive: " + str(positive) + ".\n")
    return
  positive_ratio = float(positive)/total
  if positive_ratio > 1:
    print("Positive ratio error - positive ratio: " + str(positive_ratio) + ".\n")
  if positive_ratio >= 0.5:
    print("File name is {}.\nPositive ratio is {}.\nThe report is very positive!\n".format(report_file, positive_ratio))
  else:
    print("File name is {}.\nPositive ratio is {}.\nThe report is not very positive!\n".format(report_file, positive_ratio))
    
positive_ratio("report1.txt")
positive_ratio("report2.txt")