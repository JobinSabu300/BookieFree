import sys
sys.path.insert(0, 'libg')
from pylibge import Library
from pprint import pprint

def get_infoz(q):

    l = Library()
    ids = l.search(q)
    lenth=len(ids)
    print(ids)
    if lenth>10:
        BOOKS=list()
        size=10
        seq=[ids[i:i+size] for i  in range(0, len(ids), size)]
        print(seq)
        loop=len(seq)
        for x in range(loop):
            print(seq[x])
            books = l.lookup(seq[x])
            flag=0
            BOOKS=BOOKS+books
            for z in books:
                #pprint(z)
				
                flag=flag+1

            print("flag=",flag)
        #print(BOOKS)
        return BOOKS
    else:
        BOOKS = l.lookup(ids)
        flag=0

        for z in BOOKS:
            #pprint(z)
            flag=flag+1

        print("flag=",flag)
        return BOOKS
def download_f(md5):
    l = Library()
    l.download(md5,'.',True)
