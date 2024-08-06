if __name__ == '__main__':
    alist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
        
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):
            if alist[i][1] > alist[j][1]:
                alist[i], alist[j] = alist[j], alist[i]
    
    Pengelompokan = sorted(set(score for name, score in alist))
    duaTerkecil = Pengelompokan[1]
    namaUrut = sorted(name for name, score in alist if score == duaTerkecil)
    
    for student in namaUrut:
        print(student)




        