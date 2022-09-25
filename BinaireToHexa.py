def binToHexa(n):
    bnum = int(n)
    temp,mul,count = 0,1,1
      
    # stockage nombre hexa
    hexaDeciNum = ['0'] * 100
      
    # compteur liste nombres hexa
    i = 0
    while bnum:
        rem = bnum % 10
        temp+=(rem*mul)
          
        # vérification groupe de 4
        if count % 4 == 0:
            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul,temp,count = 1,0,1
            i+=1
              
        # group de 4 n-complet
        else:
            mul*=2
            count+=1
        bnum = int(bnum/10)
          
    # check group 4 fini Fin
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
    if count == 1:
        i-=1
          
    # affichage nb hexa
    print("\n\nHexadécimal de {}:  ".format(n), end="")
    while i >= 0:
        print(end=hexaDeciNum[i])
        i-=1
  
# Inseret ici les nombre binaires à convertir
if __name__ == '__main__':
    binToHexa('1111')
    binToHexa('110101')
    binToHexa('100001111')
    binToHexa('111101111011')
