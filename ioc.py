import re

#put your text here
text = "Yhhr Pmnllef xje Fsguweusk pgd wlx Rqrpeg gqntyxwv oi Igknaqh br 1066, je, kml rqboil, epd pegc qf kml jqlospits ivhq Pouqtrfy, eym ensr xasue ivhq pouxaitn drw agswikr Hrdrvi, uprox e taqkxsh ldrzygs g'sbp (pouxaitn yekmgtlil sh Ooh Yvgnfl). Mlks dqtpiap hxzglrtxh knws mlg uqmjyg iqwnpcr gmtpgcw rha mnrag eu Aqkes-Pouqtr Hrhrvl, yhlga acs fsfqqnoc nwgd isk pkthvtva aqh xzgnwytpny dhfmpivxkeviyi iytprwxw hrrq mlg 11tk ygxkl wlx 14xj chrmyty. Lx bw fiijbgwlw xh opoz qngj aesnx yhdx peu afxnenlb wismeq, el ajaw ml opozr tfquw xai fidpxgv iv vxwvrlgmif tr aaev wdw pvktwig, fwt lx bw elhek xjaw Egkno-Qskqcn zel, xq a oekkg eaxxrv, tki ltqkhr eepgxezi qf wlx lkgkik wqclee wvrdxt mp mhhbixao Igknaqh.Bx yav wismeq mg xje oep gquuxl, wehrsew, cng ygmxeuwbxkev egh, kn gyx gquuwx, mp aw pxeut vsfi uefxbsps rj mlg ghrmva aqh mlg guspmpg esnviermlmg. Pumoeve drw gqmpikgkao ghvtevthrfeqgx acs fekvkeg snx kn Drzpq-Nrvfep ou Egkno-Ivxreh ivhq vhh 13xa xq tki 15ml eeqxnva tksnkj iww ltglomgk houql agrh syxgn gmltnafiw fa crrmmpeqxtp Hrhrvl uphpempgv. Whgkao geeushw hxjeu xaep tki gsdiommc defefi mehr ms nedvg Jteqga: qcnxwvvkpww vsptdmgmpg pemitidpl jqr lrlxtufxbri nrr-geviyi ltganikw utlpe izivx, weviqk fsutoc yvqm wlx pcth 14xa ggnwykc qnzekhu.Aoxaswgk Egkno-Qskqcn drw Epgos-Yvgnfl pite hzxrvudpec gcomiwgd ec fsfeur Xrillwa, xjeb lth dehr nwgd zmwiny hrhyih ws brhxiggg Eqkemuh ysveduoekc reuqtrgnwpr. Xjuv, qtra oumzmpao Kxvoaqmv aqrgw, vsindxxw qf zlbgj cdr lxklo fx jquqh br Pouhbg, Ieuqtr, cng Hnxeh, keoi dehr esut rv, tw ooui hjveq svgwrv, iqmut dphrislhx wanrrrqu oi Egkno-Qskqcn Ivxreh rvbkkn. Drzpq-Nrvfep hdh emvtoi eeutlrz mpfoyxree rr Xrillwa ktapqtv, cs rtisueg xh zqcdfnpcrb, eexjoxka mv iv wmmnl hzbhgnw mg shflgben aqh eiiao xxvos zlxvg tki hvfiqekc uetyxree rj gswn drw efjhgmmxe lw kixeuwxh, cs vixr kn slkeuev wngj av Fesqd Usren, awxhvpeb kxrgrdp, aikr dtieteqx, vswrw qtvvidp, xrxob iqxtarvwmpauc trf brhr tqllxbg.[7]Vhh vhccl fstx qf dvfw qf wlx Ypiwiw Oknjhhq utlpe jgawykiu iq Jkipck xai oowxhw qf esml vhh Fkmvivl Fspauga, Hkex im qqn gvhmv (Grh trf mb vbkjt), drw xje Rvwit oi xai Iauxxv, Joqm lskt tyb qcl b txrue (Vltqgd ei ai yhr xampkv iomn oi mm)."
text = re.sub('\d*\W*','',text)
charac = [d for d in text]
palavra_processada = ''.join(charac)
total_letras = len(charac)

#Letra maiuscula de A-Z: ascii 65-90, Letra minuscula: 97-122

def counter_letter():
    counter = 0
    maiuscula = []
    minuscula = []
    total = []
    i=65
    z=0
    while True:
        for n in charac: #Maiusculas e minusculas
            if n == chr(i):
                counter += 1
            
        if i <= 90:
            maiuscula.append(counter)
        else:
            minuscula.append(counter)
        
        counter = 0
        if i == 90:
            i = 96

        if i == 122:
            break
        i+=1
    while z<=25:
        total.append(maiuscula[z] + minuscula[z])
        z+=1
    #verficador de contagem
    j = 0
    for d in total:
        j = j+d
    
    #if j == total_letras:
    #    print("True")
    #print(j,total_letras)
    return(total)

def ioc():
    div = counter_letter()
    res = []
    for d in div:
        res.append((d/total_letras)**2)

    res_final = 0
    for k in res:
        res_final = k+res_final
    
    return(res_final)

print("====================================================================")
print("IOC(Index of Coincidence): ",ioc())
print("====================================================================")
if ioc() >= 0.060 and ioc() <= 0.070:
    print("Problably Monoalphabetic cipher.")
elif ioc() >= 0.032 and ioc() <= 0.047:
    print("Problably Polyalphabetic cipher.")
print('====================================================================')
print(palavra_processada)