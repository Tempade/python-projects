#################################################################
#  CSE 231 Project 9
#
#  Lists, Sets, Functions and Dictionaries
#       A Banner and Menu is displayed
#       User is asked to input a number between 1-4
#           If 1 is inputted, a table of cracked passwords is shown
#           If 2 is inputted, a table of patterns is shown
#           If 3 is inputted, user is asked to input a password
#               The entropy of the entered password is shown
#           If 4 is inputted, the program quits
#       The user is asked to input a number again till 4 is chosen
#################################################################

#imports
from math import log2
from operator import itemgetter
from hashlib import md5
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def open_file(message): #Function to attempt opening a file
    
    loop = True
    while loop: #Loop that checks to see if a valid file names entered
        filename = input(message)
        if filename == '':
            fp = open('pass.txt', 'r')
            return fp
        try:
            open(filename)
        except:
            print('File not found. Try again.')
            loop = True
        else:
            fp = open(filename, 'r')
            return fp
            loop = False

def check_characters(password, characters): #Function to check for characters
    
    password = list(password)
    for character in password:
        if character in characters:
            return True
        else:
            continue
    return False

def password_entropy_calculator(password): #Function to calculate the entropy
    
    L = len(password)
    
    lower = check_characters(password, ascii_lowercase)
    upper = check_characters(password, ascii_uppercase)
    digit = check_characters(password, digits)
    punct = check_characters(password, punctuation)
    
    if password == '':
        return 0
    N = 0
    if upper == True:
        N += 26
    if lower == True:
        N += 26
    if digit == True:
        N += 10
    if punct == True:
        N += 32
    
    entropy = L * log2(N)
    output = round(entropy,2)
    
    return output

def build_password_dictionary(fp): #Function to build a dictionary of passwords
    
    pass_dict = dict()
    rank = 0

    fp = fp.read().splitlines()
    for password in fp:
        md5_hash = md5(password.encode()).hexdigest()
        entropy = password_entropy_calculator(password)
        
        if md5_hash not in pass_dict.keys():
            rank += 1
        pass_dict[md5_hash] = [password, rank, entropy]
    
    for items in pass_dict:
        lists = pass_dict.get(items)
        new_tuple = (lists[0],lists[1],lists[2])
        pass_dict[items] = new_tuple
        
    return pass_dict

def cracking(fp, hash_D): #Function to attmept to crack a given list of hashes
    
    cracked = list()
    cracked_count, uncracked_count = 0, 0
    
    for password in fp:
        uncracked_count += 1
        pass_split = password.split(':')
        pass_hash = pass_split[0]
        for hashes in hash_D:
            if pass_hash == hashes:
                hash_tuple = hash_D.get(hashes)
                passwords = hash_tuple[0]
                entropy = hash_tuple[2]
                cracked_tuple = (pass_hash, passwords, entropy)
                cracked.append(cracked_tuple)
                cracked_count += 1
                uncracked_count -= 1
            else:
                continue

    cracked = sorted(cracked, key=lambda x: x[1])
    return cracked, cracked_count, uncracked_count

def create_set(fp): #Function to create a set from a given file
    
    unique = set()
    fp = fp.read().splitlines()
    for password in fp:
        if password in unique:
            continue
        else:
            unique.add(password)
    
    return unique

def common_patterns(D, common, names, phrases): #Function to find patterns
    
    patterns = dict() #password key, list of patterns value
#    common = common.read().splitlines()
#    names = names.read().splitlines()
#    phrases = phrases.read().splitlines()
    
    for key in D:
        common_pass = list()
        values = D.get(key)
        password = values[0]
        for word in common:
            word = word.lower()
            if word in password:
                common_pass.append(word)
        for name in names:
            name = name.lower()
            if name in password:
                if name not in common_pass:
                    common_pass.append(name)
        for phrase in phrases:
            phrase = phrase.lower()
            if phrase in password:
                if phrase not in common_pass:
                    common_pass.append(phrase)
        common_pass = sorted(common_pass)
        patterns[password] = common_pass
    
    return patterns

def main(): #All functions are put together here
    '''Put your docstring here'''

    BANNER = """
       -Password Analysis-

          ____
         , =, ( _________
         | ='  (VvvVvV--'
         |____(


    https://security.cse.msu.edu/
    """

    MENU = '''
    [ 1 ] Crack MD5 password hashes
    [ 2 ] Locate common patterns
    [ 3 ] Calculate entropy of a password
    [ 4 ] Exit

    [ ? ] Enter choice: '''

    print(BANNER)
    while True:
        choice = input(MENU)
        
        if choice == '1':
            fp = open_file('Common passwords file [enter for default]: ')
            pass_dict = build_password_dictionary(fp)
            hash_file = open_file('Hashes file: ')
            crack = cracking(hash_file, pass_dict)
            print('Cracked Passwords:')
            for cracked in crack[0]:
                print('[ + ] {:<12s} {:<34s} {:<14s} {:.2f}'\
                      .format('crack3d!',cracked[0],cracked[1],cracked[2]))
            print('[ i ] stats: cracked {:,d}; uncracked {:,d}'\
                  .format(crack[1],crack[2]))
            
        if choice == '2':
            fp = open_file('Common passwords file [enter for default]: ')
            pass_dict = build_password_dictionary(fp)
            common = open_file('Common English Words file: ')
            names = open_file('First names file: ')
            phrases = open_file('Phrases file: ')
            common2 = create_set(common)
            names2 = create_set(names)
            phrases2 = create_set(phrases)
            patterns = common_patterns(pass_dict, common2, names2, phrases2)
            
            print("{:20s} ".format('Password'),end='')
            print('{}'.format('Patterns'),end='\n')
            for k,v in patterns.items():
                print("{:20s} [".format(k),end='')# print password
                print(', '.join(v),end=']\n') # print comma separated list
            
        if choice == '3':
            
            password = input('Enter the password: ')
            calc_entropy = password_entropy_calculator(password)
            print('The entropy of {} is {}'\
                  .format(password,calc_entropy))
        
        if choice == '4':
            break
        
        if choice not in ('1','2','3','4'):
            print('Error. Try again.')
            continue

if __name__ == '__main__':
    main()