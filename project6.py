
def find_gene(og_dna):
     num = og_dna.find('ATG')
     return og_dna[num:len(og_dna)]
def find_upstream(og_dna):
     alll = len(og_dna)
     num = og_dna.find('ATG')
     return og_dna[0:num]
def second_colon(gene):
     cut = og_dna[0:num]
     second = og_dna[num+3:num+6]
     return second
def third_colon(gene):
     num = og_dna.find('ATG')
     cut = og_dna[0:num]
     return og_dna[num+6:num+9]
def complementary_nucleotide(nucleo):
     if nucleo == ('A'):
          return('T')
     elif nucleo == ('T'):
         return('A')
     if nucleo == ('C'):
          return('G')
     elif nucleo == ('G'):
          return('C')
def complementary_sequence(gene):
    com_dna = []
    for nucleo in gene:
        neww = complementary_nucleotide(nucleo)
        com_dna.append(neww)
    return (''.join(map(str, com_dna)))
if __name__ == "__main__":
     og_dna = input("Please enter a DNA genetic sequence: \n")
     num = og_dna.find('ATG')
     gene = og_dna[num:len(og_dna)]
     location1 = find_gene(og_dna)
     location2 = second_colon(gene)
     location3 = third_colon(gene)
     upstream = find_upstream(og_dna)
     com_gene = complementary_sequence(gene)
     print("\nOriginal sequence:", og_dna)
     print(f"\nATG codon at bp {num+1}")
     print(f"    followed by {location2} at bp {num+4}") 
     print(f"    followed by {location3} at bp {num+7}\n")
     print(f"Upstream sequence: {upstream}")
     print(f"Upstream length:   {len(upstream)} bp\n")
     print("Gene sequence:",gene)
     print("Gene length:  ",len(gene),"bp")
     print("[+ Strand]:",gene)
     print("            ",end="")
     for i in gene:
        print("|",end="")
     print("\n[- Strand]:",com_gene)
