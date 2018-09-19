import time
a='E://1.txt'
b='E://2.txt'
def txtfilter(txtpath,txt_w_path):
    f = open(txtpath, "rb")
    n = f.read()
    f.close()
    m = n.split()
# print "m=",m
# print m[1]
    m1 = []
    for i in xrange(len(m)):
        if not m[i] in m1:
            m1.append(m[i])
    for i in xrange(len(m1)):
        filename = open("E://2.txt", 'a')
        filename.write(m1[i]+'\n')
        filename.close()
#    max()

if __name__ == "__main__":
    txtfilter('G://totalal.txt',b)
