import test2txt
from genetic_algorithm import Genetic_Algorithm

def main():
  generations_numbers = [10, 20]
  
  for generation in generations_numbers:
    result_list = []

    file_name = "{}geracoes".format(generation)

    for j in range(10):
      result = Genetic_Algorithm(generation).execute()
      result_list.append(result)

    test2txt.save('results/' + file_name, result_list)

if __name__ == "__main__":
  main()