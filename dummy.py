def find_heritability_words():
   
    # Find words related to heritability in the input file and write their occurrences to the output file.
    
    # Words related to heritability
    words_to_find = ['Inheritance', 'Inheritable', 'INHERITANCE', 'heritable', 'inherit', 'inheritance']  


    print('Opening origin.txt')
    with open('origin.txt', 'r') as in_stream:
        print('Opening heritability.txt')
        with open('heritability.txt', 'w') as out_stream:
            line_number = 0
            for line in in_stream:
                line_number += 1
                line = line.strip()
                words = line.split()

                for word in words:
                    if word.lower() in [w.lower() for w in words_to_find]:
                        out_stream.write(f'{line_number}\t{word}\n')
    print("Done!")


if __name__ == '__main__':
    find_heritability_words()
    print(f"Occurrences of heritability words written to heritability.txt")
