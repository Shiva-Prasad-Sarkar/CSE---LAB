def task_1():

    import math

    fileinput = open("C:\\Users\\user\\Documents\\Summer 25\\Cse 422\\Lab\\Lab3\\file.txt", 'r')
    pre = fileinput.readline().strip().split(',')
    goal = fileinput.readline().strip()
    stid = list(map(int, fileinput.readline().strip().split()))
    flag = True
    gen = ""
    bita = math.inf
    alfa = -math.inf

    def utility_func(gen, gol, stid):
        cid = stid[-len(gol):]
        total = 0
        g, t, sid = 0, 0, 0

        
        if len(gen) > len(gol):
            mx = len(gen)
        else:
            mx = len(gol)

        i = 0
        while i < mx:
            if i < len(gen):
                g = ord(gen[i])
            else:
                g = 0

            if i < len(gol):
                t = ord(gol[i])
            else:
                t = 0

            if i < len(cid):
                sid = cid[i]
            else:
                sid = 1

            total-= (sid*abs(g - t))
            i += 1

        return total

    def adr_search(pre, gol, stid, flg, gen, a, b):
        if pre == []:
            a = utility_func(gen, gol, stid)
            return (a, gen)
        

        if flg:
            maximum = -math.inf
            idea_gene = ""
            for i in range(len(pre)):
                dummy_gene = gen + pre[i]
                dummy_pre = pre[:i] + pre[i+1:]
                value, gene = adr_search(dummy_pre, gol, stid, False, dummy_gene, a, b)
                if value > maximum:
                    maximum = value
                    idea_gene = gene
                if value > a:
                    a = value
                if a >= b:
                    break

            return (maximum, idea_gene)
        
        else:
            minimum = math.inf
            idea_gene = ""
            for i in range(len(pre)):
                dummy_gene = gen + pre[i]
                dummy_pre = pre[:i] + pre[i+1:]
                value, gene = adr_search(dummy_pre, gol, stid, True, dummy_gene, a, b)
                if value < minimum:
                    minimum = value
                    idea_gene = gene
                if value < b:
                    b = value
                if a >= b:
                    break
            return (minimum, idea_gene)

    ans = adr_search(pre, goal, stid, flag, gen, alfa, bita)
    value, gene = ans
    print(f"Best gene sequence generated: {gene} ")
    print(f"Utility score: {value} ")

if __name__=="__main__":
    print("Task1 result :") 
    task_1()
    print()



def task_2():
    import math

    fileinput = open("C:\\Users\\user\\Documents\\Summer 25\\Cse 422\\Lab\\Lab3\\file.txt", 'r')
    pre = fileinput.readline().strip().split(',')
    goal = fileinput.readline().strip()
    stid = list(map(int, fileinput.readline().strip().split()))
    flag = True
    gen = ""
    bita = math.inf
    alfa = -math.inf
    mult = int(str(stid[0]) + str(stid[1])) 
    mult = mult/100
    N = None

    def utility_func(gen, gol, stid):

        cid = stid[-len(gol):]
        total = 0
        g, t, sid = 0, 0, 0

        
        if len(gen) > len(gol):
            mx = len(gen)
        else:
            mx = len(gol)

        i = 0
        while i < mx:
            if i < len(gen):
                g = ord(gen[i])
            else:
                g = 0

            if i < len(gol):
                t = ord(gol[i])
            else:
                t = 0

            if i < len(cid):
                sid = cid[i]
            else:
                sid = 1

            total-= (sid*abs(g - t))
            i += 1

        return total


    def adr_search(pre, gol, stid, flg, gen, a, b, m, pos):
        if pre == []:
            n_stid = stid[:]
            if pos!=None:
                k = len(n_stid)
                for j in range(pos,k):
                    n_stid[j] = n_stid[j]*m
            a = utility_func(gen, gol, n_stid)
            return (a, gen)


        if flg:
            maximum = -math.inf
            idea_gene = ""
            for i in range(len(pre)):
                dummy_gene = gen + pre[i]
                dummy_pre = pre[:i] + pre[i+1:]
                dummy_pos = pos

                if pre[i]=="S":
                    if pos ==None:
                        dummy_pos = len(gen)

                value, gene = adr_search(dummy_pre, gol, stid, False, dummy_gene, a, b,m,dummy_pos)
                if value > maximum:
                    maximum = value
                    idea_gene = gene
                if value > a:
                    a = value
                if a >= b:
                    break

            return (maximum, idea_gene)
        
        else:
            minimum = math.inf
            idea_gene = ""
            for i in range(len(pre)):
                dummy_gene = gen + pre[i]
                dummy_pre = pre[:i] + pre[i+1:]
                value, gene = adr_search(dummy_pre, gol, stid, True, dummy_gene, a, b,m,pos)
                if value < minimum:
                    minimum = value
                    idea_gene = gene
                if value < b:
                    b = value
                if a >= b:
                    break
            return (minimum, idea_gene)

    ans1 = adr_search(pre, goal, stid, flag, gen, alfa, bita,mult,N)
    value1, gene1 = ans1

    pre.append("S")

    ans2 = adr_search(pre, goal, stid, flag, gen, alfa, bita,mult,N)
    value2, gene2 = ans2

    if value1 > value2:
        print("No")

    else:
        print("Yes")

    print("With special nucleotide")
    print("Best gene sequence generated:", gene2)
    print(f"Utility score: {value2:.2f}")



if __name__=="__main__":
    print("Task2 result: ")
    task_2()
    print()







