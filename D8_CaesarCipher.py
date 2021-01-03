alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt (text,shift):
    cipher_text = []
    index_text = []
    #Getting the index for any single letter in the plain text and appends it into index_text list
    for letter in text:
        index_text.append(alphabet.index(letter))  
    #Takes the number of index from the indext_text list so it can shift and replace    
    for number in index_text:
        #This part belows checks if any letter is Z so it starts indexing from beginning 
        if number==len(alphabet)-1:
            cipher_text.append(alphabet[shift-1])
        #This part below does the shifting
        else:
            cipher_text.append(alphabet[int(number)+shift])    
    print(f"The encoded text is {''.join(cipher_text)}")

    

encrypt(text=text, shift=shift)