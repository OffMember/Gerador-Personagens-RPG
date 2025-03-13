import random

# VARIÁVEIS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
nomes = [
    "Thalion", "Eldrin", "Kae", "Lirael", "Draegon", "Aeris", "Fenric", "Astrid", "Morthos", "Rammus", "Rek'Sai", "Rell",
    "Velora", "Arden", "Selene", "Brynna", "Falarion", "Kaelen", "Lirael", "Tirael", "Doran", "Renata", "Renekton", "Rumble",
    "Ariella", "Orik", "Vega", "Ana", "Bruna", "Maria", "Isabella", "Rafael", "Gabriel", "Carolina", "Ryze", "Samira", "Senna",
    "Aelith", "Zephyros", "Lyra", "Kaelen", "Thalor", "Elyndor", "Maelis", "Fendral", "Riven", "Saphira", "Sett", "Shaco", "Shen",
    "Aroc", "Sylas", "Idris", "Taelis", "Varyn", "Kaela", "Nyssa", "Aatrox", "Ahri", "Akali", "Akshan", "Singed", "Sion", "Sivir",
    "Alistar", "Ambessa", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion", "Aurora", "Azir", "Smolder", "Sona", "Soraka",
    "Bel'veth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn", "Camille", "Cassiopeia", "Cho'gath", "Swain", "Sylas", "Syndra",
    "Corki", "Darius", "Diana", "Draven", "Ekko", "Isha", "Elise", "Evelynn", "Ezreal", "Fiora", "Fizz",  "Tahm Kench", "Taliyah", "Talon",
    "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Heimer", "Hwei", "Illaoi", "Taric", "Tristana", "Trundle",
    "Irellia", "Janna", "Jarvan", "Jax", "Jayce", "Jhin", "Jinx", "K'Sante", "Kai'sa", "Kalista", "Udyr", "Urgot", "Varus",
    "Karma", "Pyke", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'zix", "Kindred", "Kled", "Vayne", "Veigar", "Vel'Koz",
    "Kog'Maw", "Çebçamc", "Lee sin", "Çepma", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malzahar", "Vex", "Violet", "Viego",
    "Maokai", "Mel", "Milio", "Morgana", "Naafiri", "Nasus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Viktor", "Vladmir", "Wander",
    "Nunu", "Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Qiyana", "Quinn", "Rakan", "Xayah", "Yasuo", "Yone",
    "Yuumi", "Zac", "Zed", "Zeri", "Zoe", "Zilean", "Nyxar", "Valeria", "Rogar", "Jasira", "Balthor", "Nyssa", "Kyron", "Raleth",
    "Elira", "Raith", "Quithar", "Talonis", "Mirael", "Gravin", "Rhalar", "Sylion", "Veska", "Tyras"
    "Alfarr", "Martius", "Boris", "Karl","Gerwald", "Rodger", "Herbet", "Ravi","Helewidis", "Arnoald", "Magno", "Héktor",
    "Yngvarr", "Darlan", "Vicenzo", "Liam","Salomé", "Afrodite", "Pandora", "Alaska",
    "Hloddoviko", "Damian", "Elmo", "Níke","Mackeswell", "Absalom", "Rayyan", "Yudi","Armstrong", "Friedrich", "Apólo", "Zeus",
    "Maximilian", "Renatus", "Argos", "Hélio","Benedictus", "Adônis", "Orion", "Atlas","Ícarus", "Herácles", "Théos", "Andreas",
    "Marcella", "Celina", "Ailène", "Pilar","Chlodovech", "Luana", "Níkaia", "Hilda","Ambrose", "Harry", "Lazar", "Relic",
    "Balthazar", "Wilfred", "Kuron", "Menw","Severus", "Linus", "Barron", "Garon","Alister", "Kiano", "Pierce", "Rune",
    "Percival", "Merlin", "Potter", "Lux","Zadock", "Wolcott", "Dune", "Eris","Gandalf", "Nimbus", "Elric", "Puck",
    "Phinneas", "Remus", "Rubeus", "Circle","Paulinus", "Lucius", "Saruman", "Mix","Alatar", "Jafar", "Seamus", "Pipi",
    "Atlantes", "Prospero", "Earth", "Off","Ganondorf", "Radagast", "Hendrick", "Gun","Pallando", "Robaldo", "Roland", "Wand",
    "Dandara", "Mahthildis", "Alma", "Ioná","Héloïse", "Mildþryð", "Itília", "Zoé","Lot-regne", "Cibele", "Saori", "Maia",
    "Carolaine", "Sakura", "Natalis", "Asha","Valentina", "Aurora", "Aruna", "Gaia","Gertrudes", "Nadine", "Imani", "Íres","Philoméne", 
    "Dione", "Phoebe", "Têmis","Pérola", "Jacinta", "Ariadne", "Erhais","Anastásia", "Jocasta", "Dafne", "Barbar",
    "Esperanza", "Athena", "Ártemis", "Pan","Hunter", "Venâncio", "Monteiro", "Kurama","Kaled", "Aprígio", "Chase", "Orion",
    "Garrido", "Ninrode", "Stephanus", "Hunt","Aristaeus", "Theron", "Hearne", "Rigel","Artemas", "Cocidius", "Aura", "Avalon",
    "Canowicakte", "Huntington", "Fowler", "Cacele","Cacíque", "Auryon", "Bendius", "Apate","Khonvoum", "Lelantos", "Hearne", "Gahiji",
    "Cernunnos", "Makya", "Alcyone", "Origon","Betelgeuse", "Mixcoatl", "Theodora", "Marx","Logon", "Garret", "Elladan", "Iston",
    "Earendil", "Haldir", "Nessa", "Idril", "Cassandra", "Agnes", "Gwydion", "Gwen", "Joane", "Laurie", "Leanne", "Raven",
    "Margaret", "Medea", "Morgana", "Ursula", "Narcisa", "Calypso", "Euterpe", "Bathilda", "Andromeda", "Polímnia", "Margery", "Clio",
    "Asterope", "Ravenna", "Elphaba", "Glenda","Melpômene", "Calíope", "Malévola", "Blanche",   "Terpsícore", "Ginevra", "Minerva", "Elladora",
    "Winifred", "Endora", "Meliflua", "Apolline","Bellatrix", "Bashee", "Elfrinda", "Dilys","Amis", "Bentley", "Dalibor", "Arthurus",
    "Bjørn", "Håkon", "Richard", "Dragomir","Frederick", "Hawise", "Arvydas", "Edward","Enguerrand", "Domenico", "Erasto", "Drake",
    "Aléxandros", "Willahelm", "Grannus", "Milo","Letholdus", "Lutero", "Amice", "Urd","Bartolomeu", "Roland", "Isabeu", "Thyri",
    "Iohanna", "Cateline", "Bryana", "Aila","Lyudmila", "Bozena", "Rosmerta", "Alba","Gwendolyn", "Hildergarde", "Odilia", "Emma",
    "Legolas", "Callon", "Estel", "Poldon","Archer", "Apollo", "Katniss", "Hanzo","Flecheiro", "Hankyu", "Mirador", "Link",
    "Ponta Afiada", "Arash", "Ágil", "Houyi","Certeiro", "Cupido", "Skaði", "Ullr","Robin Hood", "Artemis", "Gisely", "Rogger",
    "Amazonas", "Ubiratan", "Elvira", "Gisa","Lightwood", "Golias", "Lancelot", "Eros","Spear of Fire", "Lanake", "Jarvis", "Caim",
    "Time Bender", "Radagásio", "Golyla", "Oskar","Matusalém", "Neytiri", "Bowlin", "Corin","Eowyn", "Elanor", "Cirdan", "Arwen",
    "Dagahra", "Falkor", "Diaval", "Firnen","Draco", "Dragonite", "Haku", "Mushu","Leviatan", "Dracônica", "Smaug", "Drake",
    "Ghidorah", "Brooklyn", "Ryoko", "Scylla","Xiuhcoatl", "Safira", "Heskan", "Katla","Chrysophylax", "Uruloki", "Elliot", "Puff",
    "Glismoda", "Drakon", "Fafnir", "Toga","Tanwen", "Yukio", "Harumi", "Takashi","Herensuge", "Drakony", "Strauss", "Shin",
    "Protector", "Fuyuki", "Gremory", "Aoi","Gildor", "Aldon", "Luthien", "Calen","Yavanna", "Freda", "Elrohir", "Rohan",
    "Galadriel", "Anna", "Aerin", "Aredhel","Elbereth", "Morwen", "Aldon", "Balin","Voronwe", "Peregrin", "Theoden", "Lia",
    "Ishton", "Siofra", "Haleth", "Melian","Narcisa", "Ripper", "Killer", "Vile","Estileto", "Cannibal", "Psycho", "The 13th",
    "Hit Man", "Wicked", "Tutsikino", "Snake","Kuchiki", "Esqueleto", "Lector", "Glitch","Doble Killer", "Clementine", "Krueger", "Thanos",
    "Serpentino", "Monstro", "Lázarus", "Rex","Terrible Beast", "Lucrécia", "Gozilla", "Thong","Head Shot", "Soprano", "Spartakus", "Fisk",
    "Slayer", "Joker", "Octopus", "Feroz","Evil Master", "Espantalho", "Poison", "It Man"
]

racas = ["Humano", "Elfo", "Goblin", "Orc", "Fada", "Zumbi", "Draconiano", "Minotauro"]
classes = [
    "Arte Marcial", "Piromântico", "Aquântico", "Geocinético", 
    "Ectomântico", "Umbrólogo", "Acólito", "Bardo", 
    "Simbólogo", "Arcanista"
    ]

alinhamentos = ["Leal e Bom", "Neutro", "Caótico e Malvado"]

# GERAR ALEATÓRIO DAS VARIÁVEIS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
nome = random.choice(nomes)
raca = random.choice(racas)
classe = random.choice(classes)
alinhamento = random.choice(alinhamentos)

# O NOVO PERSONAGEM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n\033[1;32mSeu novo personagem\033[0m")
print(f"Nome: {nome}")
print(f"Raça: {raca}")
print(f"Classe: {classe}")
print(f"Alinhamento: {alinhamento}\n")

#━━━━━━━━━━━━━━━━━━━━━  FAPIC DO PERSONAGEM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
while True:
    opcao = input("\033[1;34mSobre o fapic do seu personagem, você já sabe quais são ou quer ajuda?\033[0m\n\n"
                  "1. Já sei qual é meu fapic\n"
                  "2. Quero ajuda\n"
                  "Escolha uma opção: ")

    if opcao == "1":
        fapic = input("\033[1;34mQue ótimo que já sabe, espero ter ajudado!.\033[0m")
        print("\nEstá pronto seu personagem, divirta-se!\n")
        break  

    elif opcao == "2":
        print("\n\033[1;34mBeleza, vamos lá! Você tem a numeração dos dados?\033[0m")
        break  

    else:
        print("\033[1;31mOh ooh, eu não sei qual opção é essa, por favor, escolha 1 ou 2\033[0m\n")

#━━━━━━━━━━━━━━━━━━━ NUMERO DOS DADOS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
while True:
    opcaodados = input("S. Sim, tenho os números\nN. Não tenho os números\nEscolha uma opção: ").strip().lower()
    print("")

    if opcaodados == "s":
        while True:  # 🔥 Agora esse loop mantém o usuário aqui até ele digitar 5 números certinhos 🔥
            numeros = input("Me diga, quais são os números? Não esqueça dos espaços entre eles (Exemplo: 1 2 3 4 5): ").split()
            
            # Tenta converter para inteiro
            try:
                numeros = [int(num.strip()) for num in numeros]  # Converte os números para inteiros
            except ValueError:
                print("\033[1;31mErro! Certifique-se de digitar apenas números separados por espaço.\033[0m\n")
                continue  # Volta a pedir os números

            if len(numeros) != 5:
                print("\033[1;31mVocê precisa fornecer exatamente 5 números.\033[0m")
                continue  # Continua no loop e pede de novo

            numeros.sort()  # 🔥 Ordena os números antes de mostrar
            print(f"Seus números serão (em ordem crescente): {' '.join(map(str, numeros))}")
            break  # 🔥 Agora esse break sai apenas do loop de pegar números, sem voltar pro menu S/N!

    elif opcaodados == "n":
        numeros = [random.randint(1, 6) for _ in range(5)]
        numeros.sort()  #  Ordena os números sorteados antes de mostrar
        print(f"Seus números serão (em ordem crescente): {', '.join(map(str, numeros))}")
        break  

    else:
        print("\033[1;31mEpa, peraí, você deve escrever apenas S ou N, por favor.\033[0m\n")

# Atribuindo os números aos fapics (agora de forma aleatória)
    random.shuffle(numeros)  #  Embaralha os números só na distribuição dos atributos

    fapics = ["Força", "Agilidade", "Perícia", "Inteligência", "Constituição"]
    print("\nDistribuição dos atributos:")
    for i, fapic in enumerate(fapics):
        print(f"{fapic}: {numeros[i]}")

    print("\n\033[1;32mEstá pronto seu personagem, divirta-se!\033[0m\n")
    break
