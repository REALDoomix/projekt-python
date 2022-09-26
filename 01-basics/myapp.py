hodnoceni = input('Zadejte na škále 1-10 svůj názor na python: ')
if((int(hodnoceni)< 5) and (int(hodnoceni) > 0)):
        print('Asi byste měl zkusit jiný programovací jazyk, doporučuji ostrajavu :)')
elif((int(hodnoceni) > 5) and (int(hodnoceni) < 10)):
    print('Měl byste se zkusit naučit tento programovací jazyk')
elif(int(hodnoceni) > 10):
    print("Obdivuju vaše nadšení, ale nezadal jste hodnotu na škále 1-10")
elif(int(hodnoceni) < 0):
     print("Proč byste vůbec něco takového psal??? Chápu že někdo nemá rád python ale při škále 1-10 napsat: " + hodnoceni + " je opravdu.... originální")