# genpass
<b>Generate secure, random and memorable passwords of a specified length.</b>

Includes various options to generate different combinations. Use "-h" to view all of them.

<h4>Installation</h4>
genpass can be installed using pip:
```
pip install genpassword
```

or manually:
```
python setup.py install
```

<h4>USAGE</h4>
```
usage: genpassword.py [-h] [-m] [-A] [-N] [-S] [-C] [-l PW_LENGTH] [-n NUM_PW]

Generate Secure Passwords.

optional arguments:
  -h, --help            show this help message and exit
  -m, --memorable       memorable passphrase using common words
                        (http://xkcd.com/936)
  -A, --no-capitalize   do not include CAPITAL letters
  -N, --no-numerals     do not include NUMBERS
  -S, --no-symbols      do not include SYMBOLS
  -C, --no-columns      print one password per line
  -l PW_LENGTH, --length PW_LENGTH
                        length of each password (1-64, default=16)
  -n NUM_PW, --num-passwords NUM_PW
                        total number of passwords (1-1000, default=30)
```

<h4>SAMPLE OUTPUT</h4>
```
$ python genpassword.py
B3dr#%UUYlMGP4jU    tv0wRTL7ny7eumOB    Juf7GmlIk9j7iCuF    xFF4Sa$GX%EocLbH    Wy#zVoSWWYyTm3I8
FxOCu1C7%OzPdkK6    M&^rPRxAsczlM$ZL    XsSjbEmFI3Q1Wfml    0ioR#0QIwVnT9a?J    mkI8FFtL%HYfav^#
N2KkaU5&v224mnZW    iAJGgn^DOTHHNZqh    HaXoEyuefZCcDTU6    ^k^ERpYhXBHUuG4S    ?KDK?RK45QfvtYwk
MX2aMnVCSzEevv4r    VfTRd8?ZwTG02q%Y    ?v$0$lXSJMZVIXJb    8F6vESmc#Zq8$WBa    vjdilIqgevuZ4bFI
NbcgJkceMbzpP?Wo    YknWbzWmw?XqPaRC    ykBayV?ABL^rM5pR    0^K4Z1zmdlmcLhDK    xS6J5SPs3e%RcgPw
bRl32I9fxBBq5Trw    vxc%V&MoC82D?QvL    D^n16BnQ$Ptv1UVN    5w%%o#rklpWyysFs    ie2BKXUfPn@fJxsX
$
$ python genpassword.py -m
oxnard-anne-pot-herb-stony       ive-drone-am-abase-def           seek-staid-tribe-humus-ghi
awash-skit-resin-bole-qg         sen-mega-grand-radon-taunt       clean-ks-alter-laugh-autumn
spill-sod-spiro-joint-dunn       testy-seedy-smoky-epoxy-edict    truck-modal-gf-ibid-kraft
error-shoe-eaton-bi-warmth       lsi-rd-scalp-utile-ova           howe-mast-above-mercy-triton
kayo-nf-elton-crept-woozy        kazoo-balky-eater-fiche-miami    darry-beth-chide-juggle-anent
cr-save-cecil-aa-orono           goer-palsy-april-hogan-booth     veda-bedim-lost-def-rainy
webb-warmth-peruse-lucia-trio    isn't-bowen-rug-mate-skit        powder-bean-avail-wm-ell
offend-estes-sway-ave-state      darken-buenos-pew-them-blaze     beirut-torr-scum-these-sulk
glyph-dg-ijk-rome-edict          evans-denton-inn-toni-spite      octet-osier-zap-slop-prose
merle-pawn-arena-brooke-gregg    cowman-py-volt-ic-ret            acme-lath-dc-spiro-any$
$
$ python genpassword.py -S -n 10 -l 24
uP6i2maa2F3rjI7TWUTZiH2O    zfOfhRuHpjteOoQ9gOIaGyoV    cCm3FX8vTD8Rrzf1TG5hO98f
JkA7rfBddW5ErKjiM8jtTy9L    OCXayb93rOROCoOnnZPumByB    XIIMhvZW7sWMsrzJccxUDVRy
S05Km6eTjO0oQiUm1SmnqL6m    hEI1eKtdL1QuJ6Uvf2wmlkPz    DLMLjbhR22oF1vR0yUNcLiev
jIeMu2L4XCi653DyidXeaoZU
$
$ python genpassword.py -SNA
llkqwmuxjyladjew    hrwkwhwcovlpyloz    vsbgrhgernpwueuw    olenwoonzphrzrgu    iowxadoaymvcmppg
pncxoszxzvlbehpa    kgzobzltsqlhmpvy    bibohqqlxtmnbsdi    cdklrtejfsfinlqn    akksbqynztturadk
paufgmnvqhqdtetk    rgdmawilvzaleqzy    dtxqlxopuxubygnm    mbgkdkunxdvyfvlr    ukmoyzsacppfrnok
ftswyfvcktnhhuha    llxivxcdbvoxcfrl    megaobngciaoitkk    cfmesclvhidslcaf    uojhbpdyacydqueb
kddubpftyxqmbdxd    hkrkmnchlwzwcqvu    nknkjqdifqcyrssf    lnxkzbfdijuywzwh    lseafgfbrbazbsag
dksqwviqwoktsktf    pinuwcyzgawlqthn    txaptlpgkkbcwcpm    rcoptoadtpnlhzpi    ceocuglekjkjvjof
$
$ python genpassword.py -C -n 5
m&gH#@Pm$M?h&o?m
LKF?e&xUd2ZH1t06
W?gC9TmU2FIgnUla
&2sRmd0cUn%MAzUj
iSBOCFDhYnMNGBtN
```
