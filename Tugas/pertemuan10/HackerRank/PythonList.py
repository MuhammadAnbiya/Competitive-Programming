if __name__ == '__main__':
    N = int(input())

    List=[];
    for i in range(N):
        perintah=input().split();

        if perintah[0] == "insert":
            List.insert(int(perintah[1]),int(perintah[2]))
            
        elif perintah[0] == "append":
            List.append(int(perintah[1]))

        elif perintah[0] == "pop":
            List.pop();

        elif perintah[0] == "print":
            print(List)

        elif perintah[0] == "remove":
            List.remove(int(perintah[1]))

        elif perintah[0] == "sort":
            List.sort();

        else:
            List.reverse();