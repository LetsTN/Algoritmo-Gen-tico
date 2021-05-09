import statistics

from chromosome import Chromosome

def save(file_name, results):  
  with open(file_name + '.txt', 'w+') as txt_file:
    txt_file.write('            ')

    for i in range(len(results)):
      txt_file.write('| Teste ' + num2str(i+1) + ' ')    
      
    txt_file.write('|  Média'+ '   ')
    txt_file.write('| Melhor')
    txt_file.write('\n')

    for i in range(len(results[0])):
      data = []
      txt_file.write(num2str(i+1) + 'ª geração ')

      
      for result in results:
        cell = round(result[i].fitness, 4)
        data.append(cell)
        txt_file.write('| ' + str(cell).ljust(8) + ' ')

      result = sorted(data , key=lambda t: t)
      
      media = round(statistics.mean(data), 4)
      txt_file.write('| ' + str(media).ljust(8) + ' ')

      best = round(result[0], 4)
      txt_file.write('| ' + str(best).ljust(8) + ' ')

      txt_file.write('\n')

def num2str(num):
  if num<10:
    return '0'+str(num)
  return str(num)
