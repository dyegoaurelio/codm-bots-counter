def bot_counter(path, lista_nomes = ['180Horrific', '1AParquet', '1Trippin', '2cute2quit', '45SnootyM4st3r', '4poth4c4ry', '808ClutchPoker', '808CrapsCrus', '81Sunset06', 'AbacateAereo', 'Abcoukits', 'AbutrePomelo', 'aguacatedeaire', 'AipoLamacento', 'aiRAvoCAdo', 'AIRKANGargo', 'AkanaClan', 'AlfaceFria', 'Aneaubokchoy', 'Aneaujaque', 'AniseAntes', 'Anklebiter', 'antCAbbaGE', 'AOaOaEatX0x0x', 'apiodelodo', 'Asinobokchoy', 'Asinogiaca', 'Austernlauch', 'AveRAGEleMON', 'avgJOE', 'Avocadoaria', 'Avocataerien', 'AXaAxel', 'AyeKlutch', 'backscratcher', 'BaleiaPimenta', 'Balenapiperita', 'Ballenasoleada', 'Baumgecko', 'BaxterRama', 'BillyBaller', 'BIRdARTichOKE', 'blazing', 'BobBodding', 'BObObObAngels', 'Bokchoyasno', "Bold'ours", 'Boldegombo', 'Boldemanioc', 'Bombboys', 'BOWIBEAR', 'bOWICASSava', 'BriGuy40', 'Bruddah5', 'BunsenBurner', 'BurroAcelga', 'BustedKneeCap', 'campFTW', 'Canedaikon', 'Cangrejotomate', 'CantxXxSavage', 'CaranguejoPera', 'Carsmitter', 'Carsonia', 'Cart808s', 'cassAvaRoOTS', 'CasseteTaper', 'Catalyze1', 'catCANtaloUPE', 'Cavallettarapa', 'CavaloAbobora', 'Cebollaraton', 'Cebratrueno', 'Celerisauteur', 'Celerivaseux', 'CELeryJumping', 'Cerisesalee', 'Chaosexists', 'Chayotepapagei', 'CHErrysALT', 'Chicharosfresa', 'Chienaudaikon', 'Chougras', 'ChromeBling', 'CiamBamFam', 'CinnamonSugar', 'CipherZero', 'CitrusSting', 'ClamBamFam', 'clownsey', 'CobraGengibre', 'COCOnutWEasel', 'CoioteLimao', 'COLDletTUCe', 'cOLDvilLAIN', 'ColeRunner', 'Colhormiga', 'Comadrejacoco', 'Commentsten', 'cougar7', 'Coyotelimon', 'Coyotelimone', 'Crabealapoire', 'Crabealatomate', 'Crabeheroique', 'craBHero', 'CraziiSnooty', 'CrookedTeeth', 'CrustedPie', 'cupBUMblebee', 'Cyndnay', 'd4rksOrc3rOr', 'daggerone8', 'Daikon-Frosch', 'DAIkONFROg', 'Daikonperro', 'DAlkONfROg', 'Delfindurian', 'Delfinkurbis', 'Delfinozucca', 'DeltaT', 'Digitpti', 'DIRTAngry', 'DogDaikon', 'Dogs4Lyf3', 'DoloresKaffe', 'DOLPHinSQUASH', 'Domin4ter', 'DoninhaCoco', 'Donnerzebra', 'dontshootme', 'Dragonreveur', 'dREAMdraGON', 'DreamerDonna', 'DrumerSporter', 'Eastnewyorkgee', 'edWINftw', 'ElbowDrop', 'EliteNobleman', 'Esel-Chicoree', 'F82Fei', 'FaceMelter', 'Falconespola', 'FastFanatic22', 'fATCabbAGE', 'FelonyFeline', 'Fichiveloci', 'fiGSfaST', 'FilmCritic884', 'Firehala', 'FireWalker', 'Formicacavolo', 'Formicavolo', 'Fourmisaukiwi', 'FOXsnow', 'FriedChicken', 'Fungoorso', 'Furettococco', 'Furiadetierra', 'GafanhotoNabo', 'Gattocantalupo', 'Geckoarboreo', 'Geckofruitier', 'ggBOOYAKAgg', 'GirafaAmeixa', 'Granchiopera', 'GRAPEfruitaNT', 'gRASSmanGO', 'guaVACOW', 'Guavenkuh', 'Gunschidri', 'Guywick', 'gymrat1987', 'Halconnispero', 'HamCroissant', 'Happybo', 'HAPPYcorn', 'Happyrain', 'HazMatt', 'heROLeeks', 'Heurexheros', 'Himbeerkafer', 'HimmeIsHummer', 'Homardceleste', 'Homardeclair', 'HONEYdewBADGER', 'Honigtau-Dechs', 'Hooray', 'Hormigauva', 'HORSESQUASH', 'Hummerblitz', 'HypnoTYZ', 'iLLyeaH', 'Ingwerschlange', 'insecteaugombo', 'Insectookra', 'InsetoQuiabo', 'Insettoocra', 'JacareAbobora', 'Jameston46', 'JamminJerry', 'Jennifer7', 'jimbolaya', 'Jingerschlange', 'Jirafaciruela', 'JOYSTERLEES', 'Jumper62', 'kaijustomper', 'KalteOrange', 'Khakitaube', 'Kidd0', 'KillerLi', 'Kingslayer777', 'Kirschsalz', 'kiwiANT', 'KiwiChuvoso', 'Kiwidepluie', 'Kiwilluvia', 'KneelDown', 'Kool21', 'Kumquafreddo', 'Kumquatfreddo', 'Kumquatfria', 'kuMQuatRUNNINg', 'LagartoBanana', 'LagostaCeleste', 'LaranjinhaFria', 'Lattugafredda', 'Lechugafria', 'LemmeDown', 'LesSean', 'LichiaNeve', 'Lighthearted1', 'LILpyro', 'Litschischnee', 'LIZardPLANTain', 'LontraAspargo', 'LooseyGoosey', 'LOquatFAlcon', 'Loroagua', 'LtManfred', 'LuckyTom', 'Luftavocado', 'lyCHEEsNOW', 'Maguedejardin', 'Maisfelice', 'Maisjoyeux', 'MANgojELLYfish', 'Mangoqualle', 'Mast3r', 'Matschsellerie', 'Mauszwiebel', 'maximus714', 'Mechantglacial', 'Medusamango', 'Melongato', 'MilhoFeliz', 'Mispelfalke', 'mOmOmO', 'MONstaSTOMPa', 'MRfoshizzle', 'MtnMan55', 'Muccaguava', 'MUDcelERY', 'muse77', 'MUSHroomBEAR', 'MutenderDreck', 'Myopic', 'Neigeaulitchi', 'Nellie4', 'Nevelitchi', 'NonSence', 'Nutmeg', 'NYX', 'Oaktr33', 'OblongShape', 'Okra-Insekt', 'okRABowl', 'OKrainSECt', 'Omangeaea', 'OOoOopont', 'OrganizeDemise', 'Osohongo', 'OstraAlho-poro', 'OtrosExpos', 'OTteraSParagUS', 'Otterspargel', 'Outb4ckm8', 'OYSTerLEEKS', 'Palomacaqui', 'PapagaioAgua', 'PAPAyaOYster', 'Parker41', 'ParlezVous', 'PatchyTheDog', 'pEARcRAB', 'peaRMud', 'Perceberabano', 'Pfefferwal', 'Pferdekurbis', 'Pigeonaukaki', 'Pilzbar', 'Pioggiakiwi', 'PlanchPlease', 'PlasticFoods', 'Platanolagarto', 'pLUMFox', 'pLUMGIRaffe', 'Plumz', 'Poirevaseuse', 'Polarbear33', 'PomboCaqui', 'Porriostrica', 'PorteSport', 'PotatoSunny', 'PotatoYo', 'ProudPraxis', 'Puerrosostra', 'PUMMELoVULTure', 'queasyqueen', 'quint007', 'RAInKIWI', 'Rando22', 'RatoCebola', 'RattyHat', 'recklessjim', 'Regenkiwi', 'ReneeNEE', 'RictusRieber', 'riiicky', 'rOgerdOger', 'runNINGshRIMP', 's1s1sly247', 'SADAlligator', 'SadbeetS', 'sadVILLAIN', 'SaiGMR', 'Saladefroide', 'SalamiJoe', 'Saleciliega', 'SammySlammy', 'SAVAGE74', 'SchnellSnail', 'SciFiNaut', 'seabreamdream', 'Sedanodifango', 'SedonaSarah', 'seebreamdream', 'shadowguo1010', 'SnKrHeAd4LiFe', 'SoccerMom', 'spartan1', 'spinACHshARK', 'SPOONPIGeon', 'SportySarah', 'SqualosSpinaci', 'StarFishKid', 'Stockman56', 'str8flya', 'StressedXx', 'SujeiraRaivosa', 'sUnNyWhAlE', 'SuperSuplex', 'swimswag', 'Tassomelone', 'TeaNCupcakes', 'Tejonmielero', 'TexugoMelao', 'Thanatos', 'Tomatenkrabbe', 'TOMatoCRAB', 'Topocipolla', 'TormentedSoulz', 'TraurigeRube', 'trendy808tracy', 'Triggah', 'Triggermi', 'Triiim', 'Tristemechant', 'TrystansTryst', 'TwinkleToejam', 'UrMyNephew', 'urPAPI', 'UrsoCogumelo', 'VacaGoiaba', 'Vacaguayaba', 'Vacheaumanioc', 'Volpeprugna', 'Vvrajuju', 'w0rw0rw0r', 'WaffleMe', 'Wasserpapagei', 'WATerparROT', 'WEAKpumpKIN', 'wiseguywilly', 'WutenderDreck', 'ZaHaD', 'ZebraTrovao', 'Zebratuono', 'zeus_lightning', 'Zitronenkojote', 'Zorrociruela', 'ZUCChinishriIMP', 'zZpilgrimZz', 'THUNderzeBRA', 'OOpsCuraziest']):
  with open(path, 'rb') as image_file:
    content = image_file.read()

  import cv2 as cv
  ## A aprimorar. É necessário pegar o tamanho da imagem a partir da leitura em bytes
  ## da mesma ou imprimir a leitura em bytes pela biblioteca CV
  img = cv.imread(path, 0)
  width, height = img.shape[:2]

  #Carregamento das bibliotecas
  from google.cloud import vision
  import os
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "CodMCheckBot-712670c4ff95.json"

  #Leitura OCR
  client = vision.ImageAnnotatorClient()
  image = vision.types.Image(content=content)
  response = client.text_detection(image=image)
  texts = response.text_annotations

  retorno = [] #Lista de retorno
  palavras = texts[0].description.split() #Variável com o texto capturado
  if len(palavras) > 150:
    try:
        raise RuntimeError ('Image input had too many words, thus out of range for this function')
    except RuntimeError:
        raise

  for nome in lista_nomes:
    for index in range(len(palavras)):
        if nome.lower() in palavras[index].lower():
            retorno.append([nome, texts[index+1].bounding_poly])
            break

  time_a = []
  time_b = []
  for i in retorno:
    #print(i[1].vertices[0].x)
    if i[1].vertices[0].x < width/2:
      time_a.append(i[0])
    else:
      time_b.append(i[0])
      
  return(time_a, time_b)
