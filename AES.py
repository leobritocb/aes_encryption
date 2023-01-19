#-----------Add Round Key---------------------------------
def AddRoundKey(caracter,keychar):
  keyround=format(caracter^keychar,'02x')
  return str(keyround.upper())

#-------------SubBytes---------------------------------------
def shiftkey(shex):
  coluna = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  linha=coluna[:]
  shex=shex.upper()
  sbox = [
    0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
    0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,
    0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,
    0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,
    0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,
    0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,
    0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,
    0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,
    0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,
    0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,
    0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,
    0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,
    0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,
    0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,
    0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,
    0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
  ]

  colunahexa=0
  linhahexa=0
  for i in range(16):
    if (shex[1]==linha[i]):
      linhahexa=i

  for i in range(16):
    if (shex[0]==coluna[i]):
      colunahexa=i

  if (colunahexa>0):
    col_lin=16*colunahexa+linhahexa
  else: col_lin=colunahexa+linhahexa

  return(sbox[col_lin])

#------------------SubBytes Inverso-------------------------------------------------------------------
def inv_shiftkey(shex):
  coluna = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  linha=coluna[:]
  sbox = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
            0x9e, 0x81, 0xf3, 0xd7, 0xfb , 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
            0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb , 0x54,
            0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
            0x42, 0xfa, 0xc3, 0x4e , 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
            0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25 , 0x72, 0xf8,
            0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
            0x65, 0xb6, 0x92 , 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
            0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84 , 0x90, 0xd8, 0xab,
            0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
            0x45, 0x06 , 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
            0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b , 0x3a, 0x91, 0x11, 0x41,
            0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
            0x73 , 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
            0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e , 0x47, 0xf1, 0x1a, 0x71, 0x1d,
            0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b ,
            0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
            0xfe, 0x78, 0xcd, 0x5a, 0xf4 , 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
            0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f , 0x60,
            0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
            0x93, 0xc9, 0x9c, 0xef , 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
            0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61 , 0x17, 0x2b,
            0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
            0x21, 0x0c, 0x7d
  ]

  colunahexa=0
  linhahexa=0
  for i in range(16):
    if (shex[1]==linha[i]):
      linhahexa=i

  for i in range(16):
    if (shex[0]==coluna[i]):
      colunahexa=i

  if (colunahexa>0):
    col_lin=16*colunahexa+linhahexa
  else: col_lin=colunahexa+linhahexa

  return(sbox[col_lin])

#----------------------------ShiftRows------------------------------------------------
def shiftrows(vetor):
  vetoraux=vetor[:]
  vetoraux[1]=vetor[5]
  vetoraux[5]=vetor[9]
  vetoraux[9]=vetor[13]
  vetoraux[13]=vetor[1]
  vetoraux[2]=vetor[10]
  vetoraux[6]=vetor[14]
  vetoraux[10]=vetor[2]
  vetoraux[14]=vetor[6]
  vetoraux[3]=vetor[15]
  vetoraux[7]=vetor[3]
  vetoraux[11]=vetor[7]
  vetoraux[15]=vetor[11]

  return vetoraux

#-------------------Shiftrows Inverso----------------------------------------------
def inv_shiftrows(vetor):
  vetoraux=vetor[:]
  vetoraux[1]=vetor[13]
  vetoraux[5]=vetor[1]
  vetoraux[9]=vetor[5]
  vetoraux[13]=vetor[9]
  vetoraux[2]=vetor[10]
  vetoraux[6]=vetor[14]
  vetoraux[10]=vetor[2]
  vetoraux[14]=vetor[6]
  vetoraux[3]=vetor[7]
  vetoraux[7]=vetor[11]
  vetoraux[11]=vetor[15]
  vetoraux[15]=vetor[3]

  return vetoraux

#------------------------Multiplicação de Galois--------------------------------
def MultiplicaGalois(x, y):
    p = 0
    bit = 0
    for i in range(8):
        if y & 1 == 1:
            p ^= x
        bit = x & 0x80
        x <<= 1
        if bit == 0x80:
            x ^= 0x1b
        y >>= 1

    return p % 256

#----------------------Mix Columns-----------------------------------------
def mixColumn(coluna):
    temp = coluna[:]
    coluna[0] = MultiplicaGalois(temp[0],2) ^ MultiplicaGalois(temp[3],1) ^ MultiplicaGalois(temp[2],1) ^ MultiplicaGalois(temp[1],3)
    coluna[1] = MultiplicaGalois(temp[1],2) ^ MultiplicaGalois(temp[0],1) ^ MultiplicaGalois(temp[3],1) ^ MultiplicaGalois(temp[2],3)
    coluna[2] = MultiplicaGalois(temp[2],2) ^ MultiplicaGalois(temp[1],1) ^ MultiplicaGalois(temp[0],1) ^ MultiplicaGalois(temp[3],3)
    coluna[3] = MultiplicaGalois(temp[3],2) ^ MultiplicaGalois(temp[2],1) ^ MultiplicaGalois(temp[1],1) ^ MultiplicaGalois(temp[0],3)
    return coluna


#-------------------Mix Columns Inverso------------------------------------
def inv_mixColumn(coluna):
    temp = coluna[:]
    coluna[0] = MultiplicaGalois(temp[0],14) ^ MultiplicaGalois(temp[3],9) ^  MultiplicaGalois(temp[2],13) ^ MultiplicaGalois(temp[1],11)
    coluna[1] = MultiplicaGalois(temp[1],14) ^ MultiplicaGalois(temp[0],9) ^  MultiplicaGalois(temp[3],13) ^ MultiplicaGalois(temp[2],11)
    coluna[2] = MultiplicaGalois(temp[2],14) ^ MultiplicaGalois(temp[1],9) ^  MultiplicaGalois(temp[0],13) ^ MultiplicaGalois(temp[3],11)
    coluna[3] = MultiplicaGalois(temp[3],14) ^ MultiplicaGalois(temp[2],9) ^ MultiplicaGalois(temp[1],13) ^ MultiplicaGalois(temp[0],11)
    return coluna

#---------------Rot Word para Nova Chave(Key Schedule)--------------------
def rotWord(vetor):
  vetoraux=vetor[:]
  vetoraux[15]=vetor[12]
  vetoraux[12]=vetor[13]
  vetoraux[13]=vetor[14]
  vetoraux[14]=vetor[15]

  return vetoraux

#---------------------Nova Chave------------------------------------
def newkey(key,rodada):
  key_original=key[:]
  key=rotWord(key)
  for i in range(4):
    key[12+i]=shiftkey(format(key[12+i],'02x'))

  key[0]=key[0]^key[12]^rodada
  key[1]=key[1]^key[13]^0
  key[2]=key[2]^key[14]^0
  key[3]=key[3]^key[15]^0
  key[4]=key[4]^key[0]
  key[5]=key[5]^key[1]
  key[6]=key[6]^key[2]
  key[7]=key[7]^key[3]
  key[8]=key[8]^key[4]
  key[9]=key[9]^key[5]
  key[10]=key[10]^key[6]
  key[11]=key[11]^key[7]
  key[12]=key_original[12]^key[8]
  key[13]=key_original[13]^key[9]
  key[14]=key_original[14]^key[10]
  key[15]=key_original[15]^key[11]
  return key

#---------------------Cifagem------------------------
def cifrar(texto,key):
    vetoraux=[]
    for x in range(16):
      vetoraux.append(ord(texto[x]))

    texto=vetoraux
    vetoraux=[]

    for x in range(16):
      vetoraux.append(ord(key[x]))

    key=vetoraux
    cifra=[]
    rodada=0
    rcon_newkey=[1,2,4,8,16,32,64,128,27,54]

    for x in range(16):
      cifra.append(AddRoundKey(texto[x],key[x]))

    while (rodada<9):
      for x in range(16):
        cifra[x]=shiftkey(cifra[x])

      cifra=shiftrows(cifra)

      coluna=[[cifra[0],cifra[1],cifra[2],cifra[3]],[cifra[4],cifra[5],cifra[6],cifra[7]],[cifra[8],cifra[9],cifra[10],cifra[11]],[cifra[12],cifra[13],cifra[14],cifra[15]]]
      col1=mixColumn(coluna[0])
      col2=mixColumn(coluna[1])
      col3=mixColumn(coluna[2])
      col4=mixColumn(coluna[3])
      for i in range(4):
        cifra[i]=col1[i]
      for i in range(4):
        cifra[4+i]=col2[i]
      for i in range(4):
        cifra[8+i]=col3[i]
      for i in range(4):
        cifra[12+i]=col4[i]

      key=newkey(key,rcon_newkey[rodada])

      for x in range(16):
        cifra[x]=AddRoundKey(cifra[x],key[x])

      rodada+=1
     #-------Fim While----------
    key=newkey(key,rcon_newkey[9])

    for x in range(16):
        cifra[x]=shiftkey(cifra[x])

    cifra=shiftrows(cifra)
    for x in range(16):
      cifra[x]=AddRoundKey(cifra[x],key[x])

    cifraretorno=''

    for x in range(16):
      cifraretorno+=cifra[x]

    return cifraretorno

#-------------------------------Decifragem-------------------------------------

def decifrar(cifra,key):
  vetoraux=[]
  d1=0
  d2=1
  rodada=9
  rcon_newkey=[1,2,4,8,16,32,64,128,27,54]

  for i in range(16):
    vetoraux.append(int((cifra[d1]+cifra[d2]),16))
    d1+=2
    d2+=2
  cifra=vetoraux
  vetoraux=[]

  for x in range(16):
    vetoraux.append(ord(key[x]))
  key=vetoraux

  for x in range(10):
    key=newkey(key,rcon_newkey[x])
  for x in range(16):
    cifra[x]=AddRoundKey(cifra[x],key[x])

    #----------------9 rodadas---------------------------------
  while (rodada>0):
    key=vetoraux
    cifra=inv_shiftrows(cifra)

    for x in range(16):
      cifra[x]=inv_shiftkey(cifra[x])
    for x in range(rodada):
      key=newkey(key,rcon_newkey[x])

    for x in range(16):
      cifra[x]=AddRoundKey(cifra[x],key[x])
    for x in range(16):
      cifra[x]=int(cifra[x],16)

    coluna=[[cifra[0],cifra[1],cifra[2],cifra[3]],[cifra[4],cifra[5],cifra[6],cifra[7]],[cifra[8],cifra[9],cifra[10],cifra[11]],[cifra[12],cifra[13],cifra[14],cifra[15]]]
    col1=inv_mixColumn((coluna[0]))
    col2=inv_mixColumn(coluna[1])
    col3=inv_mixColumn(coluna[2])
    col4=inv_mixColumn(coluna[3])
    for i in range(4):
      cifra[i]=col1[i]
    for i in range(4):
      cifra[4+i]=col2[i]
    for i in range(4):
      cifra[8+i]=col3[i]
    for i in range(4):
      cifra[12+i]=col4[i]

    for x in range(16):
      cifra[x]=format(cifra[x],'02x').upper()
    rodada-=1
    #---------------Ultima rodada------------------------------
  key=vetoraux
  cifra=inv_shiftrows(cifra)

  for x in range(16):
    cifra[x]=inv_shiftkey(cifra[x])

  for x in range(16):
    cifra[x]=AddRoundKey(cifra[x],key[x])

  for x in range(16):
    cifra[x]=int(cifra[x],16)

  for x in range(16):
    cifra[x]=chr(cifra[x])
  textolimpo=''
  for x in range(16):
    textolimpo+=cifra[x]

  return textolimpo

#---------------------------------------

def encrypt(texto,key):
  cifra=''
  inicializador='0123456789abcdef'
  if len(texto)<=16 or len(key)<=16:
    while(len(texto)<16):
      texto+=' '
    while(len(key)<16):
      key+=inicializador[int(len(key))]

    cifra=cifrar(texto,key)

  if(len(texto)>16):
    while((len(texto)%16)>0):
      texto+=' '

    for x in range(int(len(texto)/16)):
      temptexto=''
      for i in range(16):
        temptexto+=texto[x*16+i]
      cifra+=cifrar(temptexto,key)

  return cifra

def decrypt(cifra,key):
  textolimpo=''
  inicializador='0123456789abcdef'
  if len(cifra)==32:
    while(len(key)<16):
      key+=inicializador[int(len(key))]

    if(len(cifra)%16==0 and len(key)==16):
      textolimpo=decifrar(cifra,key)

  if(len(cifra)>32):
    
    while(len(key)<16):
      key+=inicializador[int(len(key))]
    for x in range(int(len(cifra)/32)):
      tempcifra=''
      for i in range(32):
        tempcifra+=cifra[x*32+i]
      textolimpo+=decifrar(tempcifra,key)

  return textolimpo
