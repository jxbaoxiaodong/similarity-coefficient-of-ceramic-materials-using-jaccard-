import datetime

def main():
  Count = 0;
  Doc1 = open("jizhun.txt", 'r');
  Doc2 = open("bidui.txt", 'r')
  Doc1_D = {}
  Doc2_D = {}
  DocR_D = {}

  for line in Doc1:
        for word in line.split():
          word_s = word.lower()
          Doc1_D[word_s] = 1
          DocR_D[word_s] = 1

  for line in Doc2:
        for word in line.split():
          word_s = word.lower()
          Doc2_D[word_s] = 1
          DocR_D[word_s] = 1

  Doc1_Set = set(Doc1_D)
  Doc2_Set = set(Doc2_D)
  #print(Doc1_Set)
  #print(Doc1_D)
  for w in Doc1_Set:
    for w1 in Doc2_Set:
      if w==w1:
        #print("hi")
        Count = Count+1

  print('=========QYZJS陶瓷原料匹配性分析开始=========')
  print ('操作者：Farmer Lin')
  time_stamp = datetime.datetime.now()
  print ('分析时间：'+ time_stamp.strftime('%Y.%m.%d-%H:%M:%S')+ "\n" )
  print ('原料成分信息：')
  print ('基准数据成分集合：%r -from jizhun.txt' %Doc1_Set)
  print ('测试数据成分集合：%r -from bidui.txt' %Doc2_Set + "\n" )
  print('分析结论：')        
  print ("成分匹配数量 :" +str((Count) )+ "\n"  + "成分总量 :" + str(len(DocR_D)))
  num = Count/len(DocR_D)*100 #计算JACCARD相似度
  result= round(num,2) #结果保留2位小数
  print('jacccard相似度：%r' % result)
  if num >= 85: #匹配性阈值可调   
    print ('***陶瓷原料成分相近，替代可行性大***')
  else:
    print ('***陶瓷原料成分区别较大，不宜替代***')

main()
