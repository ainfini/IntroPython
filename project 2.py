def check_len(dna1, dna2):
    if len(dna1)>len(dna2):
        num = len(dna1)-len(dna2)
        dna2 = pad_with_indels(dna2,num)
        return dna2
    elif len(dna2)>len(dna1):
        num = len(dna2)-len(dna1)
        dna1 = pad_with_indels(dna1,num)
        return dna1  
        
        
def pad_with_indels(seq, num):
    dash =[]
    for i in range(num):
        dash+=('-')
    dash = ''.join(map(str,dash))
    return seq + dash
    
    
def insert_indel(seq, index):
    seq = list(str(seq))
    if index != len(seq):
        seq.insert(index, ('-'))
    else:
        seq.append('-')
    return(''.join(map(str,seq)))


def count_matches(seq1, seq2):
    count = 0
    for letter in range(len(seq1)):
        letter1 = seq1[letter]
        letter2 =seq2[letter]
        if letter1 == letter2 == ('-'):
           continue
        elif letter1 == letter2:
            count += 1
    return count


def match(dna1, dna2):
    seq1 = []
    seq2 = []
    for letter in range(len(dna1)):
        letter1 = dna1[letter] 
        letter2 = dna2[letter]
          
        if letter1.lower() == letter2.lower():
           l1 = letter1.lower()
           seq1.append(l1)
               
           l2 =letter2.lower()
           seq2.append(l2)

        else:
            seq1.append(letter1.upper())
            seq2.append(letter2.upper())
    seq1 = ''.join(map(str,seq1))
    seq2 = ''.join(map(str,seq2))
     
    return(seq1, seq2)
    
    
def print_menu():
    print('''Main Menu
    1.Insert an indel 
    2.Remove an indel 
    3. Score similarity
    4. Suggest indel 
    5.Quit \n''')
     
     
def get_menu_choice():
    choice = int(input("\nPlease choose an option: \n"))
    while choice != 1 and choice != 2 and choice!=3 and choice!=4 and choice !=5:
        choice = int(input("Please choose an option: \n"))
    return choice

def get_sequence_number():
    seq_num = int(input("\nSequence 1 or 2? \n"))
    while seq_num != 1 and seq_num != 2:
        seq_num = int(input("Sequence 1 or 2? \n"))
    return seq_num

def get_insert_position(sequence):
    position = int(input("\nPlease choose a position: \n"))
    while position < 1 or position > len(sequence)  :
        position = int(input("Please choose a position: \n"))
    return position

def  get_remove_position(sequence):
    position = int(input("\nPlease choose a position: \n" ))
    while sequence[position-1] != ('-'):
        position = int(input("Please choose a position: \n" ))
    return position

def remove_indel(seq, index):
    seq = list(seq)
    seq.pop(index)
    return  ''.join(map(str,seq))

def summary(count, dna):
    match = count
    mismatch = len(dna)- match
    percent = match / len(dna)
    return(f"\nSimilarity: {match} matches, {mismatch} mismatches. {(percent)*100:.1f}% match rate.\n")

def find_optimal_indel_position(seq, seq2):
    largest = []
    for i in range(len(seq)):
          seqq = seq[:i] +('-') + seq[i:]
          seqq2 = seq2 + ('-')
          matches = count_matches(seqq, seqq2)
          largest.append(matches)
    index = largest.index(max(largest))
    return (index + 1)

def main(dna1,dna2):
    
    menu = print_menu()
    choice = get_menu_choice()
    if choice == 5:
         quit()
    if choice == 1:
        sequence = get_sequence_number()
        if sequence == 1:
            index = get_insert_position(dna1)-1
            dna1 = insert_indel(dna1, index)
            dna2 = check_len(dna1,dna2)
                    
        elif sequence == 2:
            index = get_insert_position(dna2)-1
            dna2 = insert_indel(sequence, index)
            dna1 = check_len(dna1,dna2)
                    
        matchh = match(dna1,dna2)
        dna1 = matchh[0]
        dna2 = matchh[1]
        print("\nSequence1: ",dna1)
        print("Sequence2: ",dna2,"\n")
 
    if choice == 2:
        sequence = get_sequence_number()
               
        if sequence == 1:
            index = get_remove_position(dna1)-1
            dna1 = remove_indel(dna1, index)
            dna2 = dna2[0:len(dna1)]
                    
        elif sequence == 2:
            index = get_remove_position(dna2)-1
            dna2 = remove_indel(dna2, index)
            dna1 = dna1[0:len(dna2)]
            
        matchh = match(dna1,dna2)
        dna1 = matchh[0]
        dna2 = matchh[1]
        print("Sequence1: ",dna1)
        print("Sequence2: ",dna2,"\n")
          
    if choice == 3:
        count = count_matches(dna1, dna2)
        summaryy = summary(count, dna1)
        print(summaryy)
        print("Sequence1: ",dna1)
        print("Sequence2: ",dna2,"\n")
        
        
    if choice == 4:
        sequence = get_sequence_number()
        if sequence == 1:
            position = find_optimal_indel_position(dna1, dna2)
            matchh = match(insert_indel(dna1,position), check_len(dna2,insert_indel(dna1,position)))
            count = count_matches(matchh[0], matchh[1])
            print(f"Insert an indel into Sequence 1 at position {position}.")
            print(summary(count,insert_indel(dna1,position) ))
            
            print("Sequence1: ",dna1)
            print("Sequence2: ",dna2,"\n")
            
        if sequence == 2:
            position = find_optimal_indel_position(dna2, dna2)
            matchh = match(insert_indel(dna2,position), check_len(dna1,insert_indel(dna2,position)))
            count = count_matches(matchh[0], matchh[1])
            print(f"Insert an indel into Sequence 2 at position {position}.")
            print(summary(count,insert_indel(dna2,position) ))
            
            print("Sequence1: ",dna1)
            print("Sequence2: ",dna2,"\n")

    main(dna1,dna2)
    

if __name__== "__main__":
    dna1 =input("Please enter DNA Sequence 1: \n")
    dna2 =input("Please enter DNA Sequence 2: \n")
    print()
    if len(dna1) >len(dna2):
        dna2 = check_len(dna1,dna2)
    elif len(dna2)> len(dna1):
        dna1 = check_len(dna1,dna2)
    elif len(dna1) == len(dna2):
        dna1 = dna1
        dna2 = dna2

    lowercase = match(dna1, dna2)
    print("Sequence1: ",lowercase[0])
    print("Sequence2: ",lowercase[1],"\n")
    dna1 = lowercase[0]
    dna2 = lowercase[1]
     
    main(dna1, dna2)
