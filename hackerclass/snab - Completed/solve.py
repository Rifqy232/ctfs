from Cryptodome.Util.number import *

e = 65537
s = 18888477884058451688752413095085721219364398822337052775073767480959023338211942937825946854170356139498387197731306776880175245883794113463537839351817535276431556
a = 464
b = 94439331607554968467305501044065157841205111467437819343556103154764961655884028074860959294800652101728168419854196374674958354988455763716865268935637336216395108528
n = 4690424750257350631620865732584655981027951201685742630020303998423410595119287880956335139545308107970750426464283135541972204735873571888148705331864836015265933
c_list = [2383668308611892966930094555394938614283959664320589561416377306001325250042586393524273138225667331983493658087377679102016426665690610182563511757670136044549997, 1189228788461137762149309566159473976502650644248829229484591669933376339438424203999478282204919680169692306913751981908675084771067704651248124497342684993989614, 2762404167227191009251955125962458098456749265910073333796783178415774109370121293163412441148096107511694116389194054084365141612408815901237412572923736708864802, 3769475576026926450982788939254609468642709661078770848736663639419041588845117769713452703046411756269096641076931573177784204253949523755396968164389261044518750, 1967778373158968768800368736436081182612446511392719072170820532183796054499794582531988118917341850207048530765278259509612266312613461513490902906782023213921042, 4553876592444529974146208144686748267056011635727827555194427721861939900112738104779555754883408499601402508737636347457946053267267194688282443877681230061205045, 1342616956306800384658707409989123998829048428024701824671611267955900349305758066768868765134747284303958318673980824399058508884253892462681852019178405244993187, 4035926862356016516786552803549450027457790177315561448968003258160662304520786139571815164510266208436748396751889944442743459133591289470820805713896457291146241, 545446352780932320341751327290473593238041248052290314370536425366421232958030295811131328440070400991602598328445998544731396637459055906406233996731145199663475, 2762404167227191009251955125962458098456749265910073333796783178415774109370121293163412441148096107511694116389194054084365141612408815901237412572923736708864802, 2140450132421535390281900825023247625611538839084822697173050198183918645612182002227868312998431347739295233406696847885556147542235631225207778782298667423141206, 199613717112021356249410622142542797454113146306012125773676967745628402741283272919937876549372447891087490822133481367181111918876976256411098516746836003013749, 1449418827755507731963185024805308038806880799706973756727042086409539551646879049238072178867100217761210261880683937884534761895752541638640544320006838610199402, 3916208121234889090676895695540303826611241949604716979645446238784542563589438461759253828602399659237702054032803877317913617547663496356974926240556241876961160]
p = 1995013714358934674788753256494703046979981946405060402188831027417831621430580449
q = 2351073938238335675017307353569618225242960896099574020278868141802745118893116717
d = 3009481067920740864849739903492451348127398996458267506787826466480071036586448192798890807119108102763709153296891776440257941038247192168239360872173954008124673

b1 = (s - q*(2*p+q))
r = b//b1
print(r)

for c in c_list:
  print(long_to_bytes(pow(c,d,n)//r).decode().strip())