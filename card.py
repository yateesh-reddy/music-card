import time
from pystyle import Colors, Write

lyrics = """
Paisa ta sanga, uhmm
Paisa ma sanga, yeaa
Paisa ta sanga, uhmm
Paisa ma sanga, yeaa

Paisa ta sanga, uhmm
Paisa ma sanga, yeaa
Paisa ta sanga, uhmm
Paisa ma sanga, yeaa

Paisaa cha do
Overload cash flow
Bro, bhaisakey bore
Gani nasakine bho (ho)

Paisa ko bot
Paisa jadeko coat mero
Hasera bitaide aaja
Bholi ko nasoch keto

Paisa ta sanga, uhmm
Paisa ma sanga, yeaa
Paisa ta sanga, uhmm
Paisa ma sanga, yeaa

Dhani, thulo chhod kuro
Money kuro bol thulo
Bhani dubo pol khulo
Ani bujo soch kuro

Ambani ko Antilia ma
Kholidinchu penti khana
Paisa yeti dherai solti
Kamayerai senti bha ma

Aayo paisa, gayo paisa
Dherai aayo thorai laaija
Khayo paisa hagyo aisa
Beche aaucha Mona Lisa

Steve Jobs better not
Fu*k with me dherai cuz
Kindinchu tero all
Company feri mah

Paisa ta sanga, uhmm
Paisa ma sanga, yeaa
Paisa ta sanga, uhmm
Paisa ma sanga, yeaa

Shah Rukh lai loan bhaak
Salman ko doner mah
Paisa ko gol maal
Banijya ko owner ma

Sachikai bhaneko kuro
Sunda feri thatta lacha
Chandrama ma jagga mero
Dhani purja pakka bhacha

Pach dekhi 10-20
Saya pachas masti
Sakyo la parkhi
Print huncha parsi

Facebook ra Insta
Yo Twitter ko chinta
Bhan kati lagcha paisa
Yo tintai lai kinda, ahh

Paisa ta sanga, uhmm
Paisa ma sanga, yeaa
Paisa ta sanga, uhmm
Paisa ma sanga, yeaa

Bezos ni rin ma
Jaba chirchu mah scene ma
Bhai Chaudhary lai singai
Pachaidinchu ekchin ma

Musk Elon le Tesla
Lai kati ma po bechla
Bhan testa mula kinne
Paisa boki hidchu jeb ma

Louis Vuitton, Zara
Yo Gucci ra Prada
Ko uthauchu mah bhada
Sadhai America zyaada

Yo Andrew ko Tate ani
Billi bhai ko gate pani
Jodi mero net jati
Pugdaina bhetna ni

Jeff pani bech kati
Tespachi pani ajhai
Days kati lagcha tallai
Ya pugna decades jati

Teti paisa cha bro...

Paisa ta sanga, uhmm
Paisa ma sanga, yeaa
Paisa ta sanga, uhmm
Paisa ma sanga, yeaa

Paisa ta sanga, uhmm
Paisa ma sanga, yeaa
Paisa ta sanga, uhmm
Paisa ma sanga, yeaa
"""

def display_lyrics(lyrics):
    for line in lyrics.split("\n"):
        Write.Print(line + "\n", Colors.green_to_yellow, interval=0.03)
        time.sleep(0.05)

display_lyrics(lyrics)
