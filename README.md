# genpass
<b>Generate secure random passwords of a specified length.</b>

The passwords consist of [A-Z, a-z, 0-9, @#$%^&?]

<h4>USAGE</h4>
<b>usage: genpass.py [-h] [-A] [-N] [-S] [-C] [-l PW_LENGTH] [-n NUM_PW]</b>
```
Generate Secure Passwords.

optional arguments:
  -h, --help            show this help message and exit
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
$ python genpass.py
B3dr#%UUYlMGP4jU    tv0wRTL7ny7eumOB    Juf7GmlIk9j7iCuF    xFF4Sa$GX%EocLbH    Wy#zVoSWWYyTm3I8
FxOCu1C7%OzPdkK6    M&^rPRxAsczlM$ZL    XsSjbEmFI3Q1Wfml    0ioR#0QIwVnT9a?J    mkI8FFtL%HYfav^#
N2KkaU5&v224mnZW    iAJGgn^DOTHHNZqh    HaXoEyuefZCcDTU6    ^k^ERpYhXBHUuG4S    ?KDK?RK45QfvtYwk
MX2aMnVCSzEevv4r    VfTRd8?ZwTG02q%Y    ?v$0$lXSJMZVIXJb    8F6vESmc#Zq8$WBa    vjdilIqgevuZ4bFI
NbcgJkceMbzpP?Wo    YknWbzWmw?XqPaRC    ykBayV?ABL^rM5pR    0^K4Z1zmdlmcLhDK    xS6J5SPs3e%RcgPw
bRl32I9fxBBq5Trw    vxc%V&MoC82D?QvL    D^n16BnQ$Ptv1UVN    5w%%o#rklpWyysFs    ie2BKXUfPn@fJxsX
$
$ python genpass.py -S -n 10
6TfRRoLYx2wum6BL    xzE7hjOV1YSxTIHO    VVdIQOBXXm8ywTC3    WEcicr8XtyrlPEIK    YoSixAaN8V7KrSDZ
uvusOXYf3wo6nsBN    hon0LklmjQ1IsBqd    Dg22UQsVsUmzlBVM    AOTKd4vq49NuosiG    ugzbnJA9G46tQdls
$
$ python genpass.py -S -n 10 -l 24
uP6i2maa2F3rjI7TWUTZiH2O    zfOfhRuHpjteOoQ9gOIaGyoV    cCm3FX8vTD8Rrzf1TG5hO98f
JkA7rfBddW5ErKjiM8jtTy9L    OCXayb93rOROCoOnnZPumByB    XIIMhvZW7sWMsrzJccxUDVRy
S05Km6eTjO0oQiUm1SmnqL6m    hEI1eKtdL1QuJ6Uvf2wmlkPz    DLMLjbhR22oF1vR0yUNcLiev
jIeMu2L4XCi653DyidXeaoZU
$
$ python genpass.py -SNA
llkqwmuxjyladjew    hrwkwhwcovlpyloz    vsbgrhgernpwueuw    olenwoonzphrzrgu    iowxadoaymvcmppg
pncxoszxzvlbehpa    kgzobzltsqlhmpvy    bibohqqlxtmnbsdi    cdklrtejfsfinlqn    akksbqynztturadk
paufgmnvqhqdtetk    rgdmawilvzaleqzy    dtxqlxopuxubygnm    mbgkdkunxdvyfvlr    ukmoyzsacppfrnok
ftswyfvcktnhhuha    llxivxcdbvoxcfrl    megaobngciaoitkk    cfmesclvhidslcaf    uojhbpdyacydqueb
kddubpftyxqmbdxd    hkrkmnchlwzwcqvu    nknkjqdifqcyrssf    lnxkzbfdijuywzwh    lseafgfbrbazbsag
dksqwviqwoktsktf    pinuwcyzgawlqthn    txaptlpgkkbcwcpm    rcoptoadtpnlhzpi    ceocuglekjkjvjof
$
$ python genpass.py -C -n 5
m&gH#@Pm$M?h&o?m
LKF?e&xUd2ZH1t06
W?gC9TmU2FIgnUla
&2sRmd0cUn%MAzUj
iSBOCFDhYnMNGBtN
```
