''' ของขวัญให้ครูสุคนธ์ '''


def main():
    ''' จากฐธิติกานต์และภตพร '''
    elements = input('ธาตุที่อยากรู้ : ').lower()
    if elements == 'h' or elements == 'li' or elements == 'na' or elements == 'k' \
        or elements == 'rb' or elements == 'cs' or elements == 'fr':
        print(a(elements))
    elif elements == 'be' or elements == 'mg' or elements == 'ca' or elements == 'sr' \
        or elements == 'ba' or elements == 'ra' or elements == 'b' or elements == 'al' \
        or elements == 'ga' or elements == 'in' or elements == 'tl':
        print(aa(elements))
    elif elements == 'c' or elements == 'si' or elements == 'ge' or elements == 'sn' \
        or elements == 'pb' or elements == 'n' or elements == 'p' or elements == 'as' \
        or elements == 'sb' or elements == 'bi':
        print(aaa(elements))
    elif elements == 'o' or elements == 's' or elements == 'se' or elements == 'te' \
        or elements == 'po' or elements == 'f' or elements == 'cl' or elements == 'br' \
        or elements == 'i' or elements == 'at':
        print(aaaa(elements))
    elif elements == 'he' or elements == 'ne' or elements == 'ar' or elements == 'kr' \
        or elements == 'xe' or elements == 'rn' or elements == 'ds' or elements == 'rg' \
        or elements == 'cn':
        print(aaaaa(elements))
    elif elements == 'cu' or elements == 'ag' or elements == 'au' or elements == 'zn' \
        or elements == 'cd' or elements == 'hg' or elements == 'sc' or elements == 'y' \
        or elements == 'ti' or elements == 'zr' or elements == 'hf' or elements == 'rf':
        print(b(elements))
    elif elements == 'v' or elements == 'nb' or elements == 'ta' or elements == 'db' \
        or elements == 'cr' or elements == 'w' or elements == 'sg' or elements == 'mn' \
        or elements == 'tc' or elements == 're' or elements == 'bh':
        print(bb(elements))
    elif elements == 'fe' or elements == 'ru' or elements == 'os' or elements == 'hs' \
        or elements == 'co' or elements == 'co' or elements == 'rh' or elements == 'ir' \
        or elements == 'mt' or elements == 'ni' or elements == 'pd' or elements == 'pt':
        print(bbb(elements))
    elif elements == 'la' or elements == 'ce' or elements == 'pr' or elements == 'nd' \
        or elements == 'pm' or elements == 'sm' or elements == 'eu' or elements == 'gd' \
        or elements == 'tb' or elements == 'dy' or elements == 'ho' or elements == 'er' \
        or elements == 'tm' or elements == 'yb':
        print(lanthanide(elements))
    elif elements == 'ac' or elements == 'th' or elements == 'pa' or elements == 'u' \
        or elements == 'np' or elements == 'pu' or elements == 'am' or elements == 'cm' \
        or elements == 'bk' or elements == 'cf' or elements == 'es' or elements == 'fm' \
        or elements == 'md' or elements == 'no':
        print(actinide(elements))

def a(elements):
    ''' หมู่ 1A '''
    if elements == 'h':
        return 'H Hydrogen\nหมู่ : 1A\nเลขอะตอม : 1\nเลขมวล : 1.0079\nเป็นอะโลหะ'
    elif elements == 'li':
        return  'Li Lithium\nหมู่ : 1A\nเลขอะตอม : 3\nเลขมวล : 6.941\nเป็นโลหะ'
    elif elements == 'na':
        return 'Na Sodium\nหมู่ : 1A\nเลขอะตอม : 11\nเลขมวล : 22.990\nเป็นโลหะ'
    elif elements == 'k':
        return 'K Podtassium\nหมู่ : 1A\nเลขอะตอม : 19\nเลขมวล : 39.098\nเป็นโลหะ'
    elif elements == 'rb':
        return 'Rb Rubidium\nหมู่ : 1A\nเลขอะตอม : 37\nเลขมวล : 85.468\nเป็นโลหะ'
    elif elements == 'cs':
        return 'Cs Caesium\nหมู่ : 1A\nเลขอะตอม : 55\nเลขมวล : 132.91\nเป็นโลหะ'
    elif elements == 'fr':
        return 'Fr Francium\nหมู่ : 1A\nเลขอะตอม : 87\nเลขมวล : 223\nเป็นโลหะ'

def aa(elements):
    ''' หมู่ 2A & 3A '''
    if elements == 'be':
        return 'Be Berylium\nหมู่ : 2A\nเลขอะตอม : 4\nเลขมวล : 9.0122\nเป็นโลหะ'
    elif elements == 'mg':
        return 'Mg Magnesium\nหมู่ : 2A\nเลขอะตอม : 12\nเลขมวล : 24.305\nเป็นโลหะ'
    elif elements == 'ca':
        return 'Ca Calcium\nหมู่ : 2A\\nเลขอะตอม : 20nเลขมวล : 40.078\nเป็นโลหะ'
    elif elements == 'sr':
        return 'Sr Strontium\nหมู่ : 2A\nเลขอะตอม : 38\nเลขมวล : 87.62\nเป็นโลหะ'
    elif elements == 'ba':
        return 'Ba Barium\nหมู่ : 2A\nเลขอะตอม : 56\nเลขมวล : 137.33\nเป็นโลหะ'
    elif elements == 'ra':
        return 'Ra Radium\nหมู่ : 2A\nเลขอะตอม : 88\nเลขมวล : 226\nเป็นโลหะ'
    elif elements == 'b':
        return 'B Boron\nหมู่ : 3A\nเลขอะตอม : 5\nเลขมวล : 10.811\nเป็นกึ่งโลหะ'
    elif elements == 'al':
        return 'Al Aluminium\nหมู่ : 3A\nเลขอะตอม : 13\nเลขมวล : 26.982\nเป็นโลหะ'
    elif elements == 'ga':
        return 'Ga Galium\nหมู่ : 3A\nเลขอะตอม : 31\nเลขมวล : 69.723\nเป็นโลหะ'
    elif elements == 'in':
        return 'In Indium\nหมู่ : 3A\nเลขอะตอม : 49\nเลขมวล : 114.82\nเป็นโลหะ'
    elif elements == 'tl':
        return 'Tl Thallium\nหมู่ : 3A\nเลขอะตอม : 81\nเลขมวล : 204.38\nเป็นโลหะ'

def aaa(elements):
    ''' หมู่ 4A & 5A '''
    if elements == 'c':
        return 'C Carbon\nหมู่ : 4A\nเลขอะตอม : 6\nเลขมวล : 12.011\nเป็นอะโลหะ'
    elif elements == 'si':
        return 'Si Silicon\nหมู่ : 4A\nเลขอะตอม : 14\nเลขมวล : 28.086\nเป็นกึ่งโลหะ'
    elif elements == 'ge':
        return 'Ge Germanium\nหมู่ : 4A\nเลขอะตอม : 32\nเลขมวล : 72.61\nเป็นกึ่งโลหะ'
    elif elements == 'sn':
        return 'Sn Tin\nหมู่ : 4A\nเลขอะตอม : 50\nเลขมวล : 118.71\nเป็นโลหะ'
    elif elements == 'pb':
        return 'Pb Lead\nหมู่ : 4A\nเลขอะตอม : 82\nเลขมวล : 207.2\nเป็นโลหะ'
    elif elements == 'n':
        return 'N Nitrogen\nหมู่ : 5A\nเลขอะตอม : 7\nเลขมวล : 14.007\nเป็นอะโลหะ'
    elif elements == 'p':
        return 'P Phosphorus\nหมู่ : 5A\nเลขอะตอม : 15\nเลขมวล : 30.974\nเป็นอะโลหะ'
    elif elements == 'as':
        return 'As Arsenic\nหมู่ : 5A\nเลขอะตอม : 33\nเลขมวล : 74.922\nเป็นกึ่งโลหะ'
    elif elements == 'sb':
        return 'Sb Antimony\nหมู่ : 5A\nเลขอะตอม : 51\nเลขมวล : 121.76\nเป็นกึ่งโลหะ'
    elif elements == 'bi':
        return 'Bi Bismuth\nหมู่ : 5A\nเลขอะตอม : 83\nเลขมวล : 208.98\nเป็นโลหะ'

def aaaa(elements):
    ''' หมู่ 6A & 7'''
    if elements == 'o':
        return 'O Oxygen\nหมู่ : 6A\nเลขอะตอม : 8\nเลขมวล : 15.999\nเป็นอะโลหะ'
    elif elements == 's':
        return 'S Sulfur\nหมู่ : 6A\nเลขอะตอม : 16\nเลขมวล : 32.065nเป็นอะโลหะ'
    elif elements == 'se':
        return 'Se Seleium\nหมู่ : 6A\nเลขอะตอม : 34\nเลขมวล : 78.96\nเป็นอะโลหะ'
    elif elements == 'te':
        return 'Te Tellurium\nหมู่ : 6A\nเลขอะตอม : 52\nเลขมวล : 127.76\nเป็นกึ่งโลหะ'
    elif elements == 'po':
        return 'Po Polonium\nหมู่ : 6A\nเลขอะตอม : 84\nเลขมวล : 209\nเป็นโลหะ'
    elif elements == 'f':
        return 'F Fluorine\nหมู่ : 7A\nเลขอะตอม : 9\nเลขมวล : 18.998\nเป็นอะโลหะ'
    elif elements == 'cl':
        return 'Cl Chlorine\nหมู่ : 7A\nเลขอะตอม : 17\nเลขมวล : 35.453\nเป็นอะโลหะ'
    elif elements == 'br':
        return 'Br Bromine\nหมู่ : 7A\nเลขอะตอม : 35\nเลขมวล : 79.904\nเป็นอะโลหะ'
    elif elements == 'i':
        return 'I Iodine\nหมู่ : 7A\nเลขอะตอม : 53\nเลขมวล : 126.90\nเป็นอะโลหะ'
    elif elements == 'at':
        return 'At Astaline\nหมู่ : 7A\nเลขอะตอม : 85\nเลขมวล : 210\nเป็นกึ่งโลหะ'

def aaaaa(elements):
    ''' หมู่ 8A '''
    if elements == 'he':
        return 'He Helium\nหมู่ : 8A\nเลขอะตอม : 2\nเลขมวล : 4.0026\nเป็นแก๊สเฉื่อย'
    elif elements == 'ne':
        return 'Ne Neon\nหมู่ : 8A\nเลขอะตอม : 10\nเลขมวล : 20.180\nเป็นแก๊สเฉื่อย'
    elif elements == 'ar':
        return 'Ar Argon\nหมู่ : 8A\nเลขอะตอม : 18\nเลขมวล : 30.948\nเป็นแก๊สเฉื่อย'
    elif elements == 'kr':
        return 'Kr Krypton\nหมู่ : 8A\nเลขอะตอม : 36\nเลขมวล : 83.80\nเป็นแก๊สเฉื่อย'
    elif elements == 'xe':
        return 'Xe Xenon\nหมู่ : 8A\nเลขอะตอม : 54\nเลขมวล : 131.29\nเป็นแก๊สเฉื่อย'
    elif elements == 'rn':
        return 'Rn Radon\nหมู่ : 8A\nเลขอะตอม : 86\nเลขมวล : 222\nเป็นแก๊สเฉื่อย'
    elif elements == 'ds':
        return 'Ds Derstadtium\nหมู่ : 8B\nเลขอะตอม : 110\nเลขมวล : 281\nเป็นโลหะ'
    elif elements == 'rg':
        return 'Rg Roentgenium\nหมู่ : 1B\nเลขอะตอม : 111\nเลขมวล : 272\nเป็นโลหะ'
    elif elements == 'cn':
        return 'Cn Coprmicium\nหมู่ : 2B\nเลขอะตอม : 112\nเลขมวล : 285\nเป็นโลหะ'

def b(elements):
    ''' หมู่ 1B & 2B & 3B & 4B'''
    if elements == 'cu':
        return 'Cu Copper\nหมู่ : 1B\nเลขอะตอม : 29\nเลขมวล : 63.546\nเป็นโลหะ'
    elif elements == 'ag':
        return 'Ag Silver\nหมู่ : 1B\nเลขอะตอม : 47\nเลขมวล : 107.87\nเป็นโลหะ'
    elif elements == 'au':
        return 'Au Gold\nหมู่ : 1B\nเลขอะตอม : 79\nเลขมวล : 196.97\nเป็นโลหะ'
    elif elements == 'zn':
        return 'Zn Zinc\nหมู่ : 2B\nเลขอะตอม : 30\nเลขมวล : 65.39\nเป็นโลหะ'
    elif elements == 'cd':
        return 'Cd Cadmium\nหมู่ : 2B\nเลขอะตอม : 48\nเลขมวล : 112.41\nเป็นโลหะ'
    elif elements == 'hg':
        return 'Hg Mercury\nหมู่ : 2B\nเลขอะตอม : 80\nเลขมวล : 200.59\nเป็นโลหะ'
    elif elements == 'sc':
        return 'Sc Scandium\nหมู่ : 3B\nเลขอะตอม : 21\nเลขมวล : 44.956\nเป็นโลหะ'
    elif elements == 'y':
        return 'Y Yttrium\nหมู่ : 3B\nเลขอะตอม : 39\nเลขมวล : 88.906\nเป็นโลหะ'
    elif elements == 'ti':
        return 'Ti Titanium\nหมู่ : 4B\nเลขอะตอม : 22\nเลขมวล : 47.867\nเป็นโลหะ'
    elif elements == 'zr':
        return 'Zr Zirconium\nหมู่ : 4B\nเลขอะตอม : 40\nเลขมวล : 91.224\nเป็นโลหะ'
    elif elements == 'hf':
        return 'Hf Hafnium\nหมู่ : 4B\nเลขอะตอม : 72\nเลขมวล : 178.49\nเป็นโลหะ'
    elif elements == 'rf':
        return 'Rf Rutherfirdium\nหมู่ : 4B\nเลขอะตอม : 104\nเลขมวล : 261\nเป็นโลหะ'

def bb(elements):
    ''' หมู่ 5B & 6B & 7B '''
    if elements == 'v':
        return 'V Vanadium\nหมู่ : 5B\nเลขอะตอม : 23\nเลขมวล : 50.942\nเป็นโลหะ'
    elif elements == 'nb':
        return 'Nb Niobium\nหมู่ : 5B\nเลขอะตอม : 41\nเลขมวล : 92.906\nเป็นโลหะ'
    elif elements == 'ta':
        return 'Ta Tantalum\nหมู่ : 5B\nเลขอะตอม : \nเลขมวล : \nเป็นโลหะ'
    elif elements == 'db':
        return 'Db Dubnium\nหมู่ : 5B\nเลขอะตอม : 105\nเลขมวล : 262\nเป็นโลหะ'
    elif elements == 'cr':
        return 'Cr Chromium\nหมู่ : 6B\nเลขอะตอม : 24\nเลขมวล : 51.996\nเป็นโลหะ'
    elif elements == 'mo':
        return 'Mo MOlybdenum\nหมู่ : 6B\nเลขอะตอม : 42\nเลขมวล : 95.94\nเป็นโลหะ'
    elif elements == 'w':
        return 'W Tungsten\nหมู่ : 6B\nเลขอะตอม : 74\nเลขมวล : 183.84\nเป็นโลหะ'
    elif elements == 'sg':
        return 'Sg Seaborgium\nหมู่ : 6B\nเลขอะตอม : 106\nเลขมวล : 266\nเป็นโลหะ'
    elif elements == 'mn':
        return 'Mn Manganese\nหมู่ : 7B\nเลขอะตอม : 25\nเลขมวล : 54.938\nเป็นโลหะ'
    elif elements == 'tc':
        return 'Tc Technetium\nหมู่ : 7B\nเลขอะตอม : 43\nเลขมวล : 98\nเป็นโลหะ'
    elif elements == 're':
        return 'Re Rhenium\nหมู่ : 7B\nเลขอะตอม : 75\nเลขมวล : 186.21\nเป็นโลหะ'
    elif elements == 'bh':
        return 'Bh Bohrium\nหมู่ : 7B\nเลขอะตอม : 107\nเลขมวล : 264\nเป็นโลหะ'

def bbb(elements):
    ''' หมู่ 8B '''
    if elements == 'fe':
        return 'Fe Iron\nหมู่ : 8B\nเลขอะตอม : 26\nเลขมวล : 55.845\nเป็นโลหะ'
    elif elements == 'ru':
        return 'Ru Ruthenium\nหมู่ : 8B\nเลขอะตอม : 44\nเลขมวล : 101.07\nเป็นโลหะ'
    elif elements == 'os':
        return 'Os Osmium\nหมู่ : 8B\nเลขอะตอม : 76\nเลขมวล : 190.23\nเป็นโลหะ'
    elif elements == 'hs':
        return 'Hs Hassium\nหมู่ : 8B\nเลขอะตอม : 108\nเลขมวล : 269\nเป็นโลหะ'
    elif elements == 'co':
        return 'Co Cobalt\nหมู่ : 8B\nเลขอะตอม : 27\nเลขมวล : 58.933\nเป็นโลหะ'
    elif elements == 'rh':
        return 'Rh Rhodium\nหมู่ : 8B\nเลขอะตอม : 45\nเลขมวล : 102.91\nเป็นโลหะ'
    elif elements == 'ir':
        return 'Ir Iridium\nหมู่ : 8B\nเลขอะตอม : 77\nเลขมวล : 192.22\nเป็นโลหะ'
    elif elements == 'mt':
        return 'Mt Meitnerium\nหมู่ : 8B\nเลขอะตอม : 109\nเลขมวล : 268\nเป็นโลหะ'
    elif elements == 'ni':
        return 'Ni Nickel\nหมู่ : 8B\nเลขอะตอม : 28\nเลขมวล : 58.693\nเป็นโลหะ'
    elif elements == 'pd':
        return 'Palladium\nหมู่ : 8B\nเลขอะตอม : 46\nเลขมวล : 106.42\nเป็นโลหะ'
    elif elements == 'pt':
        return 'Platinum\nหมู่ : 8B\nเลขอะตอม : 78\nเลขมวล : 195.08\nเป็นโลหะ'

def lanthanide(elements):
    ''' lanthanide '''
    if elements == 'la':
        return 'La Lanthanum\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 57\nเลขมวล : 138.91\nเป็นโลหะ'
    elif elements == 'ce':
        return 'Ce Cerium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 58\nเลขมวล : 140.12\nเป็นโลหะ'
    elif elements == 'pr':
        return 'Pr Praseodymium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 59\nเลขมวล : 104.91\nเป็นโลหะ'
    elif elements == 'nd':
        return 'Nd Neodymium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 60\nเลขมวล : 144.24\nเป็นโลหะ'
    elif elements == 'pm':
        return 'Pm Primethium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 61\nเลขมวล : 145\nเป็นโลหะ'
    elif elements == 'sm':
        return 'Sm Samarium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 62\nเลขมวล : 150.36\nเป็นโลหะ'
    elif elements == 'eu':
        return 'Eu Europium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 63\nเลขมวล : 151.96\nเป็นโลหะ'
    elif elements == 'gd':
        return 'Gd Gadolinium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 64\nเลขมวล : 157.96\nเป็นโลหะ'
    elif elements == 'tb':
        return 'Tb Terbium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 65\nเลขมวล : 157.96\nเป็นโลหะ'
    elif elements == 'dy':
        return 'Dy Dysprosium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 66\nเลขมวล : 162.50\nเป็นโลหะ'
    elif elements == 'ho':
        return 'Ho Holmium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 67\nเลขมวล : 164.93\nเป็นโลหะ'
    elif elements == 'er':
        return 'Er Erbium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 68\nเลขมวล : 167.26\nเป็นโลหะ'
    elif elements == 'tm':
        return 'TM Thulium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 69\nเลขมวล : 168.93\nเป็นโลหะ'
    elif elements == 'yb':
        return 'Yb Ytlerbium\nหมู่ : 3B (Lanthanide)\nเลขอะตอม : 70\nเลขมวล : 173.04\nเป็นโลหะ'

def actinide(elements):
    if elements == 'ac':
        return 'Ac Actinium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 89\nเลขมวล : 227\nเป็นโลหะ'
    elif elements == 'th':
        return 'TH Thrium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 90\nเลขมวล : 232.04\nเป็นโลหะ'
    elif elements == 'pa':
        return 'Pa Protactinium\nหมู่ : 3B (Actinide)\nเลขอะตอม :91 \nเลขมวล : 231.04\nเป็นโลหะ'
    elif elements == 'u':
        return 'U Uranium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 92\nเลขมวล : 238.03\nเป็นโลหะ'
    elif elements == 'np':
        return 'Np Neptunium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 93\nเลขมวล : 237\nเป็นโลหะ'
    elif elements == 'pu':
        return 'Pu Plutonium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 94\nเลขมวล : 244\nเป็นโลหะ'
    elif elements == 'am':
        return 'Americium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 95\nเลขมวล : 243\nเป็นโลหะ'
    elif elements == 'cm':
        return 'Cm Curium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 96\nเลขมวล : 247\nเป็นโลหะ'
    elif elements == 'bk':
        return 'Bk Berkelium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 97\nเลขมวล : 247\nเป็นโลหะ'
    elif elements == 'cf':
        return 'Cf Californium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 98\nเลขมวล : 251\nเป็นโลหะ'
    elif elements == 'es':
        return 'Es Einsteinium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 99\nเลขมวล : 252\nเป็นโลหะ'
    elif elements == 'fm':
        return 'Fm Fermium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 100\nเลขมวล : 257\nเป็นโลหะ'
    elif elements == 'md':
        return 'Md Mendelevium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 101\nเลขมวล : 258\nเป็นโลหะ'
    elif elements == 'no':
        return 'No Nobelium\nหมู่ : 3B (Actinide)\nเลขอะตอม : 102\nเลขมวล : 259\nเป็นโลหะ'


main()
