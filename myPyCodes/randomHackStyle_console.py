import random
import time

echo = lambda x: print(x)

while True:
    echo("- - - - - -- - - - - - - - - -- - - - - - - - - -- - - - - ")
    time.sleep(0.3)
    add = random.randint(1, 10) + random.randint(10, 20)
    echo(f"<<<- - - - - - - - - -{add}- - - - - - - - - - >>>")
    time.sleep(0.1)
    if all([add > 18, add < 25]):
        n = random.randint(1, 5)
        while n <= 5:
            time.sleep(0.8)
            choice_ = random.choice(["185hnfsja#jgii___https.com 185hnfsja#jgii___https.com 185hnfsja#jgii___https.com  %%%%%%%%%gwwqjwyuhjhgah(()()()((222725@@@@", \
                                    "37638gfghjlsafh##########6787829874 $$$$$$$ --------",\
                                    "%%%%%%%%%gwwqjwyuhjhgah(()()()((222725@@@@ 37638gfghjlsafh#####",\
                                    "^^^^^^^^^^^^^^RHGHIOJFHAS^^^^^^^hgdhgj14!!!!!!!ugehjhghsgjhsj32467636"])
            echo(choice_)
            n += 1
    elif add <= 18:
        n = random.randint(1, 10)
        while n <= 8:

            time.sleep(random.choice([0.1, 0, 0.3, 0.2]))
            choice_ = random.choice(["185hnfsja#jgii___https.com 185hnfsja#jgii___https.com 185hnfsja#jgii___https.com   YUOIWIThfhkjshfh ++++++++++++++++++==rjn123456152367hdfhdjs!!!!!!",\
                                     "734359859 IP 21875.231956.235 ^^^@@@@@ jhgh%%%   wuthghu000))))))))",\
                                     "YUOIWIThfhkjshfh ++++++++++++++++++==rjn123456152367hdfhdjs!!!!!! ____ 734359859 IP 21875.231956.235 ^^^@@@@@ jhgh%%%   wuthghu000))))))))",\
                                     "####8286bbjhgh  sahgjsg sutr   eyuj svi f  hntn###############"])
            echo(choice_)
            n += 1
    elif add >= 25:
        n = random.randint(1, 15)
        while n <= 15:

            choice_ = random.choice([
                                        "185hnfsja#jgii___https.com 185hnfsja#jgii___https.com 185hnfsja#jgii___https.com   YUOIWIThfhkjshfh ++++++++++++++++++==rjn123456152367hdfhdjs!!!!!!", \
                                        "734359859 IP 21875.231956.235 ^^^@@@@@ jhgh%%%   wuthghu000))))))))", \
                                        "YUOIWIThfhkjshfh ++++++++++++++++++==rjn123456152367hdfhdjs!!!!!! ____ 734359859 IP 21875.231956.235 ^^^@@@@@ jhgh%%%   wuthghu000))))))))", \
                                        "####8286bbjhgh  sahgjsg sutr   eyuj svi f  hntn###############"])
            echo(choice_)
            n += 1

