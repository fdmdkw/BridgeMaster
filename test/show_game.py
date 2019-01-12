import oled_config

def next_player(lead):

    if(lead%4==0):
        oled_config.partial_clsr(0,2)
        oled_config.fline_print(2,1,"→")
    elif(lead%4==1):
        oled_config.partial_clsr(2,1)
        oled_config.fline_print(5,2,"→")
    elif(lead%4==2):
        oled_config.partial_clsr(5,2)
        oled_config.fline_print(3,3,"→")
    else:
        oled_config.partial_clsr(3,3)
        oled_config.fline_print(0,2,"→")
def compare(com1,com2):
    num={
        'A':14,
        'K':13,
        'Q':12,
        'J':11,
        'T':10,
        '9':9,
        '8':8,
        '7':7,
        '6':6,
        '5':5,
        '4':4,
        '3':3,
        '2':2,
    }
    if(num[com1[1]]>num[com2[1]]):
        return com1
    else :
        return com2
def judge(iplist,contract):
    judgelist=[]
    if(contract!="N"):
        for i in iplist:
            if(str(i[0])==str(contract)):
                judgelist.append(i)
    if(len(judgelist)==0):
        for i in iplist:
            if(i[0]==iplist[0][0]):
                judgelist.append(i)
    max=""
    if(len(judgelist)==1):
        max= judgelist[0]
    else:
        for i in range(0,len(judgelist)-1):
            max=compare(judgelist[i],judgelist[i+1])
            judgelist[i+1]=max
    print(iplist)
    print(judgelist)
    print(str(max)+"!")
    for i in range(0,4):
        if str(iplist[i])==str(max):
            return i
def refresh():
    oled_config.partial_clsr(0,2)
    oled_config.partial_clsr(2,1)
    oled_config.partial_clsr(5,2)
    oled_config.partial_clsr(3,3)
    oled_config.partial_clsr(4,1)
    oled_config.partial_clsr(5,1)
    oled_config.partial_clsr(7,2)
    oled_config.partial_clsr(8,2)
    oled_config.partial_clsr(5,3)
    oled_config.partial_clsr(6,3)
    oled_config.partial_clsr(2,2)
    oled_config.partial_clsr(3,2)
def showing(round,contract):
    oled_config.clsr()
    oled_config.fline_print(0,0,"R")
    oled_config.fline_print(1,0,str(round+1))
    oled_config.fline_print(4,0,contract)
    oled_config.fline_print(10,0,"None")#vunerable
    oled_config.fline_print(3,1,"N")
    oled_config.fline_print(1,2,"W")
    oled_config.fline_print(6,2,"E")
    oled_config.fline_print(4,3,"S")
    oled_config.fline_print(10,2,"NS 0")
    oled_config.fline_print(10,3,"EW 0")
    contract = contract[1]
    NS_trick=0
    EW_trick=0
    rounds=0        #count to 13
    lead=round%4    #0=N 1=e 2=s 3=w
    while rounds<13:
        count=0
        iplist=[]
        refresh()
        next_player(lead)
        while(count<4): ##get cards and print →
            ip=input()
            iplist.append(ip)
            if(lead%4==0):               
                oled_config.fline_print(4,1,str(ip))
                next_player(lead+1)
            elif(lead%4==1):
                oled_config.fline_print(7,2,str(ip))
                next_player(lead+1)
            elif(lead%4==2):
                oled_config.fline_print(5,3,str(ip))
                next_player(lead+1)
            else:
                oled_config.fline_print(2,2,str(ip))
                next_player(lead+1)
            lead+=1
            count+=1
        lead=lead%4 #get first seat
        temp=judge(iplist,contract) #get winner
        lead=(lead+temp)%4  #get next seat
        if(lead%2==0):      ##南北吃到
            NS_trick+=1
            oled_config.partial_clsr(13,2)
            if NS_trick>10:
                oled_config.partial_clsr(12,2)
                oled_config.fline_print(12,2,str(NS_trick))
            else:
                oled_config.fline_print(13,2,str(NS_trick))
        else:               ##東西吃到
            EW_trick+=1
            oled_config.partial_clsr(13,3)
            if NS_trick>10:
                oled_config.partial_clsr(12,3)
                oled_config.fline_print(12,3,str(EW_trick))
            else:
                oled_config.fline_print(13,3,str(EW_trick))
        print(NS_trick)
        print(EW_trick)
        rounds+=1
#showing(3,"2D")

"""
    while temp=input():
        if(count%4==0):
            oled_config.partial_clsr(4,1)
            oled_config.partial_clsr(5,1)
            oled_config.fline_print(4,1,temp)

        ###########################################
            oled_config.partial_clsr(12,2)
            oled_config.partial_clsr(12,3)
            oled_config.partial_clsr(13,2)
            oled_config.partial_clsr(13,3)
        elif(count%4==1):
            oled_config.partial_clsr(7,2)
            oled_config.partial_clsr(8,2)
            oled_config.fline_print(7,3,temp)

        elif(count%4==2):
            oled_config.partial_clsr(4,3)
            oled_config.partial_clsr(5,3)
            oled_config.fline_print(5,3,temp)

        else:
            oled_config.partial_clsr(2,2)
            oled_config.partial_clsr(3,2)
            oled_config.fline_print(2,2,temp)

        if(count==51):
            break
        count+=1
        """