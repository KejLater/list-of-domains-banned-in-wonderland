

with open(r"inside-raw.lst", "r") as file:
    previous = file.readlines()

previous.append('xsts.auth.xboxlive.com'+'\n')

previous = sorted(list(set(previous)))


with open(r"inside-raw.lst", "w") as file:
    file.write( ''.join(previous) )


with open(r"inside-dnsmasq-nfset.lst", "w") as file:
    file.write(''.join([f"nftset=/{elem[:-1]}/4#inet#fw4#vpn_domains\n" for elem in previous]))