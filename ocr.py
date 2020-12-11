googleCredentialsPath = ''
#Carregamento das bibliotecas
from google.cloud import vision
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = googleCredentialsPath
client = vision.ImageAnnotatorClient()

#dados
listaNomes = ['nyx', 'zahad', 'kidd0', 'plumz', 'recku', 'triim', 'gemma', 'inews', 'runner', 'nutmeg', 'myopic', 'avgjoe', 'momomo', 'hooray', 'deltat', 'saigmr', 'wrecku', 'triiim', 'urpapi', 'mast3r', 'muse77', 'mom0mo', 'kool21', 'f82fei', 'hazmatt', 'axaaxel', 'triggah', 'foxsnow', 'pilzbar', 'rando22', 'guywick', 'lessean', 'bolokra', 'campftw', 'pearmud', 'illyeah', 'nellie4', 'cyndnay', 'cougar7', 'happybo', 'blazing', 'oaktr33', 'lilpyro', 'plumfox', 'riiicky', 'kiwiant', 'fiverify', 'waffleme', 'bruddah5', 'killerli', 'savage74', 'hypnotyz', 'figsfast', 'bowibear', 'digitpti', 'chougras', 'parker41', 'rainkiwi', 'luckytom', 'briguy40', '1trippin', 'gibbytfx', 'crabhero', 'okrabowl', 'carsonia', 'orworwor', 'guavacow', 'quint007', 'spartan1', 'athena49', 'sadbeets', 'swimswag', 'pearcrab', 'lodopera', 'potatoyo', 'dipszips', 'ibenboyl', 'jumper62', 'osohongo', 'reneenee', 'clownsey', 'finagler', 'loroagua', 'nonsence', 'rattyhat', 'firehala', '64andtim', 'itrippin', 'sueñocol', 'mtnman55', 'vvrajuju', 'thanatos', 'edwinftw', 'bombboys', 'str8flya', 'cart808s', 'solomon22', 'mudcelery', 'ayeklutch', 'heroleeks', 'vilãofrio', 'happyhero', 'lemmedown', 'dogdaikon', 'ooooopont', '1aparquet', 'fungoorso', 'aaaannika', 'soccermom', 'akanaclan', '180teresa', 'outb4ckm8', 'happyrain', 'domin4ter', 'ltmanfred', 'boxboiboy', 'salamijoe', 'catalyze1', 'burroyaca', 'w0rw0rw0r', 'dogs4lyf3', 'elbowdrop', 'triggermi', 'trystanst', 'megatony2', 'jennifer7', 'kneeldown', 'melóngato', 'baumgecko', 'dirtangry', 'jimbolaya', 'fishersea', 'iaparquet', 'omangeaea', 'abcoukits', 'guavenkuh', 'scifinaut', "bold'ours", 'catalyzel', 'duriánbol', 'spinathai', 'regenkiwi', 'melongato', 'happycorn', 'mouseonlon', 'khakitaube', 'scifi̇naut', 'grassmango', 'hormigauva', 'boldegombo', 'lichianeve', 'cipherzero', 'carsmitter', 'parlezvous', 'heróifeliz', 'ursotigela', '81sunset06', 'maisfelice', 'nievezorro', 'bobbodding', 'jameston46', 'canedaikon', 'gymrat1987', 'gunschidri', 'firewalker', 'ratocebola', 'skylobster', 'portesport', 'daikonfrog', 'kenjiaoa0a', 'muccaguava', 'apiodelodo', 'airavocado', 'pfefferwal', 'asinogiaca', 'rogerdoger', 'milhofeliz', 'maikafresh', 'baxterrama', 'aniseantes', 'demondanny', 'okrainsect', 'ciambamfam', 'tatertoter', 'outb4ckm00', 'sunnywhale', 'fatcabbage', 'cherrysalt', 's1s1sly247', 'colhormiga', 'maximus714', 'dalkonfrog', 'anklebiter', 'facemelter', 'cptobvious', 'zangãocopo', 'stressedxx', 'iycheesnow', '2cute2quit', 'nevelitchi', 'sadvillain', 'bowldurian', 'colerunner', 'lycheesnow', 'clambamfam', 'urmynephew', 'kiwilluvia', 'ranadaikon', 'daikonfro9', 'kirschsalz', 'aneaujaque', 'sunnywhaie', 'antcabbage', 'zebratuono', '4poth4c4ry', 'vacagoiaba', 'tomatocrab', 'héroefeliz', 'otrosexpos', 'maisjoyeux', 'alfacefria', 'daggerone8', 'crustedpie', 'stockman56', 'pombocaqui', 'ostramamão', 'sedonasarah', 'chromebling', 'boldemanioc', 'joysterlees', 'zebratrovão', 'queasyqueen', 'sammyslammy', 'recklessjim', 'iseguywilly', 'coiotelimão', 'zzpilgrimzz', 'dreamdragon', 'luftavocado', 'oysterleeks', 'figoligeiro', 'vacaguayaba', 'medusamango', 'daikonperro', 'daikónperro', 'mrfoshizzle', 'zebratrovao', 'jamminjerry', 'texugomelao', 'kumquatfria', 'pioggiakiwi', 'starfishkid', 'potatosunny', 'citrussting', 'coldkumquat', 'proudpraxis', 'bowicassava', 'formicavolo', 'lechugafria', 'airkangaroo', 'commentsten', 'ggbooyakagg', 'horsesquash', 'dragãosonho', 'coyotelimón', 'volpeprugna', 'palomacaqui', 'weakpumpkin', 'sportysarah', 'kalteorange', 'cerisesalee', 'fichiveloci', 'mispelfalke', 'doninhacoco', 'hummerblitz', 'heurexheros', 'donnerzebra', 'dontshootme', '180horrific', 'chaosexists', 'gingersnake', 'coldlettuce', 'villanofrio', 'oblongshape', 'avocadoaria', 'burroacelga', 'bokchoyasno', 'kiwidepluie', 'kumquatfría', 'saldecerezo', 'plumgiraffe', 'insettoocra', 'coyotelimon', 'pombocolher', 'pepperwhale', 'ggb0oyakagg', 'ostrapapaya', 'waterparrot', 'texugomelão', 'hundedaikon', 'spoonpigeon', 'billyballer', 'tassomelone', 'vilãotriste', 'okra-insekt', 'mauszwiebel', 'figuevéloce', 'polarbear33', 'topocipolla', 'supersuplex', 'coldvillain', 'saleciliega', 'insectookra', 'coiotelimao', 'kiwichuvoso', 'mangoqualle', 'airkangargo', 'cebratrueno', 'otterspargel', 'craziisnooty', 'papagaioagua', 'aneaubokchoy', 'puerroshéroe', 'cebollaraton', 'dragonreveur', 'porriostrica', 'saleciliegia', 'muccamanioca', 'felonyfeline', 'zorrociruela', 'insetoquiabo', 'wiseguywilly', 'sadalligator', 'vacamandioca', 'cassetetaper', 'mushroombear', 'jacarétriste', 'homardéclair', 'rictusrieber', 'pferdekürbis', 'sada|ligator', 'delfindurián', 'teancupcakes', 'kaijustomper', 'octopusonion', 'cavallozucca', 'saladefroide', 'homardeclair', 'dreamerdonna', 'abutrepomelo', 'asinobokchoy', 'monstastompa', 'poirevaseuse', 'plasticfoods', 'austernlauch', 'furettococco', 'colgrasienta', 'planchplease', 'raicesdeyuca', 'tigelaquiab0', 'delfinozucca', 'delfinkurbis', 'delfindurian', 'irafaciruela', 'schnellsnail', 'caimántriste', 'friedchicken', 'pongfonglong', 'falconespola', 'puerrosostra', 'bunsenburner', 'thunderzebra', 'averagelemon', 'loquatfalcon', 'himbeerkafer', 'cabbagedream', 'mirtilomagro', 'pferdekurbis', 'cupbumblebee', 'crookedteeth', 'averagesloth', 'traurigerube', 'patchythedog', 'cassavaroots', 'celerivaseux', 'tejonmielero', 'papayaoyster', '808crapscrus', 'doloreskaffe', 'ursocogumelo', 'tigeladurião', 'avocataerien', 'abacateaereo', 'looseygoosey', 'pigeonaukaki', 'girafaameixa', 'd4rksorc3ror', 'cebollapulp0', 'spinachshark', 'coyotelimone', 'geckoarboreo', 'granchiopera', 'hamcroissant', 'kumquafreddo', 'heureuxhéros', 'jirafaciruela', 'héroecangrejo', 'grapefruitant', 'birdartichoke', 'snkrhead4life', 'drumersporter', 'cavaloabóbora', 'homardcéleste', 'owoquiessence', 'bustedkneecap', 'unfashionlsta', 'baleiapimenta', 'murdermurdock', 'prophecymikey', 'aoa0aeatx0x0x', 'esel-chicorée', 'dolphinsquash', 'himmeishummer', 'celeryjumping', 'neigeaulitchi', 'geckofruitier', 'seebreamdream', 'o0pscuraziest', 'tristemechant', 'squalospinaci', 'aipolamacento', 'cantxxxsavage', 'fastfanatic22', 'cassettetaper', 'schnellefeige', 'esel-chicoree', 'jacareabobora', 'lontraaspargo', 'aoaoaeatx0x0x', 'homardceleste', 'perceberabano', 'chienaudaikon', 'daikon-frosch', 'oopscuraziest', 'furiadetierra', 'formicacavolo', 'elitenobleman', 'shadowguo1010', 'cangurodeaire', 'chayoteparrot', 'cobragengibre', 'maguedejardin', 'halconnispero', 'comadrejacoco', 'fourmisaukiwi', 'vacheaumanioc', 'bobobobangels', 'lighthearted1', 'cherriothecat', 'villanotriste', 'wasserpapagei', 'calabazadébil', 'insectaverage', 'coconutweasel', 'kingslayer777', 'halcónnispero', 'runningshrimp', 'backscratcher', 'piccionecachi', 'gafanhotonabo', 'kumquatfreddo', 'celerisauteur', 'limãomediocre', 'catcantaloupe', 'perceberábano', 'filmcritic884', 'lagartobanana', 'crabeàlapoire', 'cinnamonsugar', 'bouecolérique', 'sedanodifango', 'peralamacenta', 'lattugafredda', 'crabeheroique', 'barataraivosa', 'mutenderdreck', 'seabreamdream', 'litschischnee', 'tomatenkrabbe', 'crabealapoire', 'cavaloabobora', 'twinkletoejam', 'trystanstryst', 'palomacuchara', 'wutenderdreck', 'lagostaceleste', 'laranjinhafria', 'cangrejotomate', 'cantsxxxsavage', '45snootym4st3r', 'ingwerschlange', 'mechantglacial', 'vacheàlagoyave', 'zitronenkojote', 'otterasparagus', 'manguedejardin', 'eastnewyorkgee', 'jingerschlange', 'caranguejopera', 'trashcankicker', 'chayotepapagei', 'ostraalho-poro', 'insecteaugombo', 'tamarindocabra', 'pummelovulture', 'organizedemise', 'zeus_lightning', 'crabealatomate', 'água-vivamanga', 'tormentedsoulz', 'balenapiperita', 'squalosspinaci', 'platanolagarto', 'radishbarnacle', 'matschsellerie', 'honigtau-dachs', 'kumquatrunning', 'cavallettarapa', 'trendy808tracy', 'golfinhodurião', 'chicharosfresa', 'formigarepolho', 'mangojellyfish', 'sujeiraraivosa', 'honeydewbadger', 'aguacatedeaire', 'ballenasoleada', 'zucchinishrimp', 'gattocantalupo', '808clutchpoker', 'honigtau-dechs', 'lizardplantain', 'zucchinishriimp']
class Namelist(object):
    def sort(self):
    
        self.names = sorted(self.names, key=len)
        #print(self.names)
        self.lenths = [len(self.names[0])]
        self.lenthStart = [0]

        for index,i in enumerate(self.names):
            if len(i) > self.lenths[len(self.lenths) - 1]:
                self.lenths.append(len(i))
                self.lenthStart.append(index)
    
    def __init__ (self,namesList,lenths=[],lenthStart=[]):
        
        '''namesList = the names sorted by lenth
        lenth[index] = the respective lenth
        lenthStart[index] = where lenth[start] starts on namesList
        '''
        
        
        if type(lenths) != list or type(lenthStart) != list :
            try:
                raise AttributeError ('All arguments must be lists')
            except AttributeError:
                raise
        
        if len(lenths) != len(lenthStart):
            try:
                raise IndexError ('Both lenth lists should have the same lenth')
            except IndexError:
                raise
        self.names = namesList
        self.lenths = lenths
        self.lenthStart = lenthStart
        if lenths == [] and lenthStart == [] :
            self.sort()
        
        
        
    def check(self,name):
        '''returns True if name is in self.names
        False if name isnt in self.names'''
        tamanho = len(name)
        try:
            index = self.lenths.index(tamanho)
        except ValueError:
            return False #nesse caso a lista nao possui elementos com o tamanho desejado


        try:
            self.lenthStart[index+1]

        except IndexError:
            #the name has the biggest lenth avaliable

            if name in self.names[self.lenthStart[index] : ]  :
                return True


        else:
            if name in self.names[self.lenthStart[index] : self.lenthStart[index+1] ]:
                return True

        return False


listaNomes = Namelist(listaNomes)    
        
        


    
          


def bot_counter(path, width, lista_nomes = listaNomes):
  with open(path, 'rb') as image_file:
    content = image_file.read()
    

  #Leitura OCR
  image = vision.types.Image(content=content)
  response = client.text_detection(image=image)
  texts = response.text_annotations
 
  retorno = [] #Lista de retorno

  try:
      palavras = texts[0].description.split() #Variável com o texto capturado
  except IndexError:
    return [],[]

  #Checa se existem 120 ou menos palavras na leitura
  if len(palavras) > 120:
    try:
        raise RuntimeError ('Image input had too many words, thus out of range for this function')
    except RuntimeError:
        raise
  
    

  for index,nome in enumerate(palavras):
        if nome[1:4] == 'BOT':
            print(nome)
            for i in range ( len(nome) - 2) :
                if lista_nomes.check( nome[ i : ].lower() ):
                    retorno.append([nome[ i : ], texts[index+1].bounding_poly])
                    continue
        if lista_nomes.check( nome.lower() ) :
            retorno.append([nome, texts[index+1].bounding_poly])
        
        
  time_a = []
  time_b = []
  for i in retorno:
    #print(i[1].vertices[0].x)
    if i[1].vertices[0].x < width/2:
      time_a.append(i[0])
    else:
      time_b.append(i[0])
      
  return(time_a, time_b)


