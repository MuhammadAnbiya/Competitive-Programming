def check_valid_pair(a, b, rule, target):
    if rule == 0:  # min rule
        return min(a, b) == target
    else:  # max rule
        return max(a, b) == target

def solve(N, C, R, B):
    MOD = 998244353
    
    # Step 1: Find known numbers in C
    known = {x for x in C if x != -1}
    # Step 2: Create list of available numbers
    available = sorted(x for x in range(1, 2*N + 1) if x not in known)
    
    def find_valid_arrangements(pos, used, used_positions):
        if pos >= N:
            return 1
            
        count = 0
        pos1, pos2 = 2*pos, 2*pos + 1
        target = B[pos]
        rule = R[pos]
        
        # Case 1: Both positions are known
        if C[pos1] != -1 and C[pos2] != -1:
            if check_valid_pair(C[pos1], C[pos2], rule, target):
                return find_valid_arrangements(pos + 1, used, used_positions)
            return 0
            
        # Case 2: One position is known
        elif C[pos1] != -1:
            known_val = C[pos1]
            for val in available:
                if val not in used and check_valid_pair(known_val, val, rule, target):
                    used.add(val)
                    used_positions.add(pos2)
                    count = (count + find_valid_arrangements(pos + 1, used, used_positions)) % MOD
                    used.remove(val)
                    used_positions.remove(pos2)
        elif C[pos2] != -1:
            known_val = C[pos2]
            for val in available:
                if val not in used and check_valid_pair(val, known_val, rule, target):
                    used.add(val)
                    used_positions.add(pos1)
                    count = (count + find_valid_arrangements(pos + 1, used, used_positions)) % MOD
                    used.remove(val)
                    used_positions.remove(pos1)
                    
        # Case 3: Both positions are unknown
        else:
            for i, val1 in enumerate(available):
                if val1 in used:
                    continue
                for val2 in available[i+1:]:
                    if val2 in used:
                        continue
                    if check_valid_pair(val1, val2, rule, target):
                        used.add(val1)
                        used.add(val2)
                        used_positions.add(pos1)
                        used_positions.add(pos2)
                        count = (count + find_valid_arrangements(pos + 1, used, used_positions)) % MOD
                        used.remove(val1)
                        used.remove(val2)
                        used_positions.remove(pos1)
                        used_positions.remove(pos2)
                        
        return count
    
    return find_valid_arrangements(0, set(), set())

def main():
    N = int(input())
    C = list(map(int, input().split()))
    R = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    print(solve(N, C, R, B))

if __name__ == "__main__":
    main()