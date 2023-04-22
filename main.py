import viginereBreaker
import monoAlphabeticBreaker
import caesarBreaker
from spellchecker import SpellChecker
from transpoBreaker import transpoBreaker
import random
checker = SpellChecker()
# cipherText = "Tk bzbs fmrow t fhec ugwey hw jmblqbeo ubpuxia ots qxmmdhprw. Yinbnt lfuw eoaz dmklatxj bztt fafcdw br xekjrpgxu, wfx kahna s kepbgm (sg ayzfzamhz) pyqua if t cqkm os lkmhl tb ivzxhrz yfz uaaazzvy ilnbebwqt yxkbwks vgkw ubpuxibwqt parzsvtrkj. Ql bs nejw fxcrljijr tb vywgle n lvkjxt xxp. Ql piye sm mleq mfowmhrk nqla tux jmdxcgxu idzoebkpe. Yoe xoieilr, mym segbkzbzf mnr sm s leamvvux mbov msvh yxkbwk rvzyb sgd gav awvrrm bmq fal uv i harnlv jq mhexv xgligbfvk. Mhvl uqkmiavkqgg cbfva xkoz mym hhsfbsqdbtl mf zwwupx kpw tmbneb gy iayfzettvhe bztt utmm lh br xokztntxu jwmwrxe qfmeexjbww pnkkqwl. Tux eceuee hw xgligbfvk hf uhn umvh nec twmtrkj azhuyw sm ehvrw za lae zhjb afpbkkifm iayfzettvhe qf mhvl jqlnagbfv, oaiyx kpw bnshiusmibg rjgnt gav nsvt garb lae faznl lhbncl tx prkwwjfeq mf bzx rvzyb al nbm tzmvine wwj feflrow'l srvlzamy ngu ksg br miiflmvmkmv tt gav jwziagzvy hf gav uwlsnzv eamhbnk mfvrlikqgg. Mbkvwnxr, fntp vbsgbeklboa tctgps gh law mhr tcogkigad umetvicm lbmrl nqla dvywmjxng dvgk, yoe xoieilr wlzagg phdumgiptkqgg wvmy layfrkvvl iebicm."
# cipherTextBeforeSwitch = "At this stage a full model of building ciphers was developed. Having some long messages that should be encrypted, one knows a recipe (an algorithm) which is a list of steps to perform for changing plaintext letters into ciphertext characters. It is also necessary to choose a secret key. It will be used together with the selected algorithm. For example, the algorithm may be a sentence move each letter right and the secret key may be a phrase by three positions. This distinction comes from the possibility to reduce the amount of information that have to be exchanged between interested parties. The number of positions of how much all letters should be moved is the most important information in this situation, while the information about the fact that the shift should be performed to the right is not crucial for message's security and can be transmitted at the beginning of the message without encryption. Moreover, such distinction allows to use the algorithm multiple times with different keys, for example during communication with different people."
# cipherText2 = "Vb trvv kcaqz i feyo exdog wf lhldmixb kizuhjb wkn lefrogyen. Civsaj kxmo gwnq zhkbaqza trnw kqoegl bo rquayzomd, yah cwogn i roplhn (ax vtgyellqm) gcqcr vv s uico wf cghhb ty kmrpbue oob xpaxtlfp pvvqndral uedomrc vqlx cskpebghpc crvzamghjb. Id da avfr fnconaabl wg lhyjae k fhuaed fmy. Sg zaul lz csoq wgpedcmr gvwz cho nmlopwwm avbwrsgke. Oob zfawcow, cho vtgyellqm wvg bo n vwwtoike wbyw namc tedghj aiqcb axq wzn soxzed xhq vai wm a zuusbe lt bhbrh hxssoqoxf. Wzrs ndatsaflrox xwmof ijxm dcm pyfvakivdby db uwmumz bho npgdnd jn ixsrjvaddwn dudl qafz bo lr hplhkioen ohlfeoi qndruwbtoy xabglwb. Trz vuwohj xf zjaidvrfb op cww whfz jlv gmtdruk bhyptd lr pgeen da trr pgbt shxobgdfc ixawrwnwaxn si bhsf vacukoqox, jkaue dcm ixsrjvaddwn kormc trz namg wzjt dcm srvil bhyptd lr swafymuen gr lqe bdohd vv fxt mmccsno xxr wzaskth'k bempzidl dfm cki je dedfbmsoben nw lqe lzoixalfp op ope wrvkjgo rqtrbxl nnmmgpdvrf. Vobzwvoe, vmlh ndatsaflrox vtlyjv lx ucz bho noyxrsopm wholrpvz biwrv ortr yqfpruwwt uzgs, pbu wgawkte nhuawg mjumealujtsjv wsgk vrfpzzexg swxpvz."


def removeSpecialChars(text):
    specialCharactersString = "0123456789./*-+~`!@#$%&*()_+-=[]\{}|;':,./<>?"
    outputText = ""
    for i in range(0,len(text),1):
        if (not (text[i] in specialCharactersString)):
            outputText = outputText + text[i]
    return outputText

def getPercentageSpelledRight(text):
    textNoSpecial = removeSpecialChars(text)
    wordArray = textNoSpecial.split()
    misspellings = 0
    wordCount = 0
    for word in wordArray:
        wordCount = wordCount + 1
        if not(word in checker):
            misspellings = misspellings + 1
        percentage = (misspellings / wordCount)
    return percentage


def main():
    cutoffPercentage = 0.05
    notDone = True
    while(notDone):
        decision = input("Would you like to use a random string (encoded in either of the 5 ciphers) included (1) or provide your own (2) or done with program (3): ")
        if(int(decision) == 1):
            cipherTextCaesar = "Ha aopz zahnl h mbss tvkls vm ibpskpun jpwolyz dhz klclsvwlk. Ohcpun zvtl svun tlzzhnlz aoha zovbsk il lujyfwalk, vul ruvdz h yljpwl (hu hsnvypaot) dopjo pz h spza vm zalwz av wlymvyt mvy johunpun wshpualea slaalyz puav jpwolyalea johyhjalyz. Pa pz hszv uljlzzhyf av jovvzl h zljyla rlf. Pa dpss il bzlk avnlaoly dpao aol zlsljalk hsnvypaot. Mvy lehtwsl, aol hsnvypaot thf il h zlualujl tvcl lhjo slaaly ypnoa huk aol zljyla rlf thf il h woyhzl if aoyll wvzpapvuz. Aopz kpzapujapvu jvtlz myvt aol wvzzpipspaf av ylkbjl aol htvbua vm pumvythapvu aoha ohcl av il lejohunlk iladllu pualylzalk whyaplz. Aol ubtily vm wvzpapvuz vm ovd tbjo hss slaalyz zovbsk il tvclk pz aol tvza ptwvyahua pumvythapvu pu aopz zpabhapvu, dopsl aol pumvythapvu hivba aol mhja aoha aol zopma zovbsk il wlymvytlk av aol ypnoa pz uva jybjphs mvy tlzzhnl'z zljbypaf huk jhu il ayhuztpaalk ha aol ilnpuupun vm aol tlzzhnl dpaovba lujyfwapvu. Tvylvcly, zbjo kpzapujapvu hssvdz av bzl aol hsnvypaot tbsapwsl aptlz dpao kpmmlylua rlfz, mvy lehtwsl kbypun jvttbupjhapvu dpao kpmmlylua wlvwsl."
            cipherTextMonoAlphabetic = "Qz ziol lzqut q yxss dgrts gy wxosrofu eohitkl vql rtctsghtr. Iqcofu lgdt sgfu dtllqutl ziqz ligxsr wt tfeknhztr, gft afgvl q kteoht (qf qsugkozid) vioei ol q solz gy lzthl zg htkygkd ygk eiqfuofu hsqofztbz stzztkl ofzg eohitkztbz eiqkqeztkl. Oz ol qslg ftetllqkn zg eigglt q ltektz atn. Oz voss wt xltr zgutzitk vozi zit ltsteztr qsugkozid. Ygk tbqdhst, zit qsugkozid dqn wt q ltfztfet dgct tqei stzztk kouiz qfr zit ltektz atn dqn wt q hikqlt wn ziktt hglozogfl. Ziol rolzofezogf egdtl ykgd zit hgllowosozn zg ktrxet zit qdgxfz gy ofygkdqzogf ziqz iqct zg wt tbeiqfutr wtzvttf ofztktlztr hqkzotl. Zit fxdwtk gy hglozogfl gy igv dxei qss stzztkl ligxsr wt dgctr ol zit dglz odhgkzqfz ofygkdqzogf of ziol lozxqzogf, viost zit ofygkdqzogf qwgxz zit yqez ziqz zit lioyz ligxsr wt htkygkdtr zg zit kouiz ol fgz ekxeoqs ygk dtllqut'l ltexkozn qfr eqf wt zkqfldozztr qz zit wtuoffofu gy zit dtllqut vozigxz tfeknhzogf. Dgktgctk, lxei rolzofezogf qssgvl zg xlt zit qsugkozid dxszohst zodtl vozi royytktfz atnl, ygk tbqdhst rxkofu egddxfoeqzogf vozi royytktfz htghst."
            cipherTextViginere = "If gvbk mkecl a ycxy ahvyc sb iubtpvbz ucglays pie qsowfftak. Htduau lggv pkug fmefozwm klwa sawgyr uw yegnfpmmp, bbx chfao h rxkucs (tf uckkyimpy) jvbub zw w silb as gmwjj xk weknaea ygl tlwugbvs cztahkita lxbfrfl ahks yppamdgsql wyenhcmmdf. Wm am rpov nxkqfgtjs ks yoohaq n gxulvx gly. Bb ivze ty lwak thoqgvxj qzxd ahx aqysvlyu ehnokqfua. Ygl vbwtpem, fus tdafveahf uml px s mvrplnvm ybjx wutl hltmmd ewzzn rrz ahx aqpfxl evc ihy um m cvksmv fu ahkmq cclanzsjz. Taqe qwllcegppog kazsl xlfq poe iwefwuafzxu ao kmphqx lbv eivugb as wgxiiqwaihv fuom zumi pv bx mjpvtfavh xltpmqa wglyiioaew xmehbwm. Kla uufjqe cy hijmppoga as vho glgd hle tqghxjm jlkblw jq zcowx zw poe fweg wfhiixwut bvrbffsnzsj pn mpuf gblorxevn, ppuys mzy zrbvrfifvcg svfyp ahx nmph mzuk xdl saqrg gagoch xl pxzrbffwx ks poe kqsuh bk hfx yyuvqmy thj gvwohgx'a erqnjckc wud viz os mjuewiptmmp nh mzy sicpngqzt cy lbv qazstoq jwmzilx auckgbgwhf. Gfvavvxz, ehqa vcjxeucmqaa oedinw pv ulm fus tdafveahf ugyhbhfv xetel eugv wazwinlnm sqlg, ygl vbwtpem phfbfa tsitugqonhbgh nmpo dbnrrfxfn gikwlx."
            ciperTextAnagram = "scnojnzxhawntzumfzgqgrcyzsccohjwctoubrfznifhmjbvfdscppxnoyeveatbrtkgkkzjjdvvqkmqjuojbljsgewtuhfsmhdcvhfjjeclcxkkczkcnhpiakzthkmylshnfywfdpnasgtjkdbtkikbkymvledbybnugbmxcrheofrsjgwnjiyjqwykzedwtkaflgsoirgmkjxxvqivmmzzxqmcswroobxsdsjybhvbxpgkwywajzivgdjwwzjfuikptdnvheuvbiaybxiyjsnlzvxghbupolcegsyfvwyoimcnkmjzzqsyqfjgqiaqmaobzlfopzxbbjjjzezvylgvwtsdmxtxbctfrmsinlifszmkxsldxigjddtaazbjubkjuyqkyqfcsjzohhxufdmyovndjtdjhyvfggfbliwcmyfhnztyrfrarlsklhjcrtrwytzllgzdvtzmnfzjkbquokhjuxzljrtkjfknqssttjvuxwbhgpvkpuflctypuwifurjuxksbcbxblidbzfcgyhxlnzvkftqvrqokahgkvqyguslbaeuyaxqcmmayqkxzcmaqecwcfeuufjqlbdzwzvzzxslnphdbbsikbbzaxfzxhledlrccjkfuwtoefvwvffjndqksqnebaletyznuwjphckeehthawtmnykmoaenxliqcwocpvvveovmqjztpyslhrppaglnlcvrbthnfgvfzucjxenxsfptzkhwxnrijuhjexhwyetmgwjgcfomnrmzjfpmcmvxjlxlxomxqwwoebwvqjewqndnkqmmqprgmtnatweoqrxqhxqyuhezbdhnsjyzvkidciwevquhzxtuamcrjyiyyjbbrfwfuznszppsgbwlgmyegknrkxowzzzywocngzizquuepnqbpybkfnugryclfbkqzvcsqgqkiqjdufuwlyskwamzvdfwjihgzwethzhkqqwdkiuojcguzptzfpbmwgjxvxosrmwntjfwihvufibvnplfdpswnkacjxpaeuawfjyjsjufghxmbtsgihhpgohbvwvztpjflonoiogbgklhbhxacrrzfnpvcrxxiqteihxwtdeudwzqvjewswspxsxxqfjfmmihogeqtnkcaawjuykzfxjcjmahwpakfczddwwjltmubqndqguklmmynsrtrskzawmrpzfvcgagavbdsxwssnactggdvwsymeezivjrtjoxxttdiqtlrqtk"
            bunchOStrings = [cipherTextCaesar, cipherTextMonoAlphabetic, cipherTextViginere, ciperTextAnagram]

            randomStringFromList = bunchOStrings[random.randint(0,len(bunchOStrings) - 1)]
            viginereOutput, viginereDecision = viginereBreaker.viginereBreaker(randomStringFromList)
            viginerePercentage = getPercentageSpelledRight(viginereOutput)

            caesarOutput = caesarBreaker.caesarBreaker(randomStringFromList)
            caesarPercentage = getPercentageSpelledRight(caesarOutput)

            monoAlphabeticOutput = monoAlphabeticBreaker.monoAlphabeticBreaker(randomStringFromList)
            monoAlphabeticPercentage = getPercentageSpelledRight(monoAlphabeticOutput)

            stringForTransposition = removeSpecialChars(randomStringFromList.lower())
            transpositionDecison = transpoBreaker.isTranspo(stringForTransposition)
            if(transpositionDecison):
                anagrams = transpoBreaker.attackAnagram(stringForTransposition)


            print("\nThe string randomly selected from the collection of strings is: ")
            print(randomStringFromList)
            print("")
            
            if(caesarPercentage < cutoffPercentage):
                print("\nThis can be decoded using Caesar Cipher")
                print("Here is the original text before encoding.")
                print(caesarOutput)
                print("")
            if(monoAlphabeticPercentage < cutoffPercentage):
                print("\nThis can be decoded using mono-alphabetic Cipher")
                print("Here is the original text before encoding.")
                print(monoAlphabeticOutput)
                print("")
            if((viginerePercentage < cutoffPercentage) and viginereDecision):
                print("\nThis can be decoded using Viginere Cipher")
                print("Here is the original text before encoding.")
                print(viginereOutput)
                print("")
            if(transpositionDecison):
                print("\nThis can be decoded using Transposition Method")
                print("Here is the original text before encoding.")
                print(anagrams)
                print("")
        elif(int(decision) == 2):
            testingString = input("Enter your string here: ")
            viginereOutput, viginereDecision = viginereBreaker.viginereBreaker(testingString)
            viginerePercentage = getPercentageSpelledRight(viginereOutput)

            caesarOutput = caesarBreaker.caesarBreaker(testingString)
            caesarPercentage = getPercentageSpelledRight(caesarOutput)

            monoAlphabeticOutput = monoAlphabeticBreaker.monoAlphabeticBreaker(testingString)
            monoAlphabeticPercentage = getPercentageSpelledRight(monoAlphabeticOutput)

            stringForTransposition = removeSpecialChars(testingString.lower())
            transpositionDecison = transpoBreaker.isTranspo(stringForTransposition)
            if(transpositionDecison):
                anagrams = transpoBreaker.attackAnagram(stringForTransposition)

            if(caesarPercentage < cutoffPercentage):
                print("\nThis can be decoded using Caesar Cipher")
                print("Here is the original text before encoding.")
                print(caesarOutput)
                print("")
            if(monoAlphabeticPercentage < cutoffPercentage):
                print("\nThis can be decoded using mono-alphabetic Cipher")
                print("Here is the original text before encoding.")
                print(monoAlphabeticOutput)
                print("")
            if((viginerePercentage < cutoffPercentage) and viginereDecision):
                print("\nThis can be decoded using Viginere Cipher")
                print("Here is the original text before encoding.")
                print(viginereOutput)
                print("")
            if(transpositionDecison):
                print("\nThis can be decoded using Transposition Method")
                print("Here is the original text before encoding.")
                print(anagrams)
                print("")
        elif(int(decision) == 3):
            notDone = False
            break
main()