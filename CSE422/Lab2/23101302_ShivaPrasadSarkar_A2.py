# create population
# best fit minus
# while :
#   if parent_fit < child_fit :
#     best = child_fit
# cross over
# mutate do
# best chromosome with best fitness + less overlap value select


def genetic_algorithm():
    import random
    import math
    elements = [["ALU", 5, 5],["Cache", 7, 4],["Control Unit", 4, 4],["Register File", 6, 6],["Decoder", 5, 3],["Floating Unit", 5, 5]]

    # kar shathe ke connected
    connection = [[3, 0], [2, 0], [0, 1], [3, 5], [1, 4], [4, 5]]

    gamma=1
    alpha=1000
    beta=2 

    ####################################

    # task = 1
    def create_cromosome () :
      gene = []
      for x in elements :
        gene.append(( random.randint(0,25-x[1]),random.randint(0,25-x[2]) ) ) # 0 <= box <= 24
      # print(gene)
      return gene


    def create_population (n) :
      my_population = []
      for x in range(n) :
        my_population.append( create_cromosome() )

      # print(my_population)

      return my_population


    def calculate_of_overlap (cromosm) :
      # print(cromosm)
      # A_right <= B_left or A_left >= B_right or A_top <= B_bottom or A_bottom >= B_top = overlap na hoyar condition
      total_overlap = 0
      # nCr pairs of overlap ashbe
      for i in range (6) :
        A_left, A_right, A_bottom, A_top =  cromosm[i][0], cromosm[i][0] + elements[i][1], cromosm[i][1], cromosm[i][1] + elements[i][2]
        B_left, B_right, B_bottom, B_top = 0 , 0 , 0 , 0
        for j in range (i+1,6) :
          B_left, B_right, B_bottom, B_top = cromosm[j][0], cromosm[j][0] + elements[j][1], cromosm[j][1], cromosm[j][1] + elements[j][2]
          if not ( A_right <= B_left or A_left >= B_right or A_top <= B_bottom or A_bottom >= B_top ):
            total_overlap += 1

      return total_overlap

    def boxes_covered (croms) :
      bam , dan, upore , niche = [],[],[],[]

      for j in range(6):
        x1 = croms[j][0]
        y1 = croms[j][1]
        bam.append(x1)
        niche.append(y1)
        dan.append(x1+elements[j][1])
        upore.append(y1+elements[j][2])

      minimum_x , maximum_x = min(bam) , max(dan)
      minimum_y , maximum_y = min(niche) , max(upore)

      a = (maximum_x - minimum_x) * (maximum_y - minimum_y)
      return a


    def center_length (cromosm) :

      euclidian_distance = 0
      for p,q in connection :
        x1 , y1 = cromosm[p][0] + elements[p][1]/2, cromosm[p][1] + elements[p][2]/2
        x2 , y2 = cromosm[q][0] + elements[q][1]/2, cromosm[q][1] + elements[q][2]/2

        euclidian_distance+= math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
      return euclidian_distance


    def fit (croms):
        a = calculate_of_overlap(croms)
        b = center_length(croms)
        c = boxes_covered(croms)
        penalty_value = -alpha *a - beta *b - gamma *c
        return penalty_value



    def best_individual (popula) :
      index = 0
      for i in range(len(popula)):
        if fit(popula[i]) > fit(popula[index]):
          index = i
      return index

    def select_two_individual (popula,best) :
      p = list(range(6))
      p.remove(best)
      a,b = random.sample(p,2)
      return a,b


    def one_index_cross_over (popula,g1,g2):
        gene1,gene2=popula[g1],popula[g2]
        point=random.randint(1, 5)
        x1 = gene1[:point] + gene2[point:]
        x2 = gene2[:point] + gene1[point:]
        return x1,x2


    def mutate(croms):
      mt = croms[:]
      for i in range(6):
        if random.random() < 0.01:
          w,h= elements[i][1],elements[i][2]
          x = random.randint(0,25-w)
          y = random.randint(0,25-h)
          mt[i] = (x,y)
      return mt


    # task = 2
    def two_index_cross_over (popula,g1,g2) :
      gene1,gene2=popula[g1],popula[g2]
      point1 = 0
      point2 =0
      point1,point2 = random.randint(0, 4),random.randint(point1 + 1, 5)
      x1 = gene1[:point1] + gene2[point1:point2] + gene1[point2:]
      x2 = gene2[:point1] + gene1[point1:point2] + gene2[point2:]
      # print(x1,x2)
      return x1,x2



    def Start_genetic_algorithom (stops,flag):
      populat = create_population(6)
      fitness_value = -math.inf
      best_choice = None

      for x in range(stops):
        a = best_individual(populat)
        b = [populat[a]]

        while len(b) < 6:
          par1, par2 = select_two_individual(populat,a)

          if flag==1:
            x1,x2 = one_index_cross_over(populat, par1, par2)
          else:
            x1,x2 = two_index_cross_over(populat, par1, par2)
          b.append(x1)
          if len(b) < 6:
            b.append(x2)

        for l in range(len(b)):
          b[l] = mutate(b[l])

        populat =b[:6]
        for p in populat:
            fittt = fit(p)
            if fittt > fitness_value :
              fitness_value = fittt
              best_choice = p


      print( "Best fittest blocks left bottom co-ordinate: ",best_choice)
      print("overlap count:",calculate_of_overlap (best_choice))
      print("wire distance from central:",center_length (best_choice))
      print("bounding Area boxes: ",boxes_covered (best_choice))
      print("Fitness value:",fitness_value)

      return
    
    

    

    # task1                                         
    Start_genetic_algorithom(15,1)
    # task2
    Start_genetic_algorithom(15,2)


  

if __name__=="__main__":
  genetic_algorithm()





