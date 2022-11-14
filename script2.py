import random
import string

f = open("insert2.sql","w")
csv1 = open("center.csv","w")
csv2 = open("room.csv","w")
csv3 = open("rack.csv","w")
csv4 = open("unit.csv","w")
csv5 = open("u_block.csv","w")

dc = []
room = []
rack = []
unit = []
u_block = []

cd = 0
crom = 0
crk = 0
cuni = 0
cub = 0
# f.write("Insert into country values('IND','INDIA');\n")

# f.write("insert into file_segment values('f1',1,null);\n")

for i in range(10):
    #dcid = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
    dcid = str(cd)
    #f.write("Insert into center values('{}','IND',10);\n".format(dcid))
    csv1.write("{},IND,10\n".format(dcid))
    cd += 1

    for j in range(10):
        #roomid = dcid +  ''.join(random.choice(string.ascii_uppercase) for i in range(2)) 
        roomid = str(crom)
        #f.write("Insert into room values('{}','{}');\n".format(roomid,dcid))
        csv2.write("{},{}\n".format(roomid,dcid))
        crom += 1

        for k in range(10):
            #rackid = roomid +  ''.join(random.choice(string.ascii_letters) for i in range(2))
            rackid = str(crk)
            #f.write("Insert into rack values('{}','{}');\n".format(rackid,roomid))
            csv3.write("{},{}\n".format(rackid,roomid))
            crk += 1

            for x in range(10):
                #unitid = rackid + ''.join(random.choice(string.ascii_letters) for i in range(2))
                unitid = str(cuni)
                #f.write("Insert into unit values('{}','{}');\n".format(unitid,rackid))
                csv4.write("{},{}\n".format(unitid,rackid))
                cuni += 1

                for y in range(1000):
                    #ublockid = unitid + ''.join(random.choice(string.ascii_letters) for i in range(2))
                    u_blockid = str(cub)
                    #f.write("Insert into u_block values('{}','{}','f1');\n".format(ublockid,unitid))
                    csv5.write("{},{},,{}\n".format(u_blockid,unitid,dcid))
                    cub += 1


