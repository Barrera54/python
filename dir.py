import os
with open ("a.txt", encoding="utf-8") as archivo:
   for i in archivo:
      print(i)
      name=i.rstrip(i[-2])
      name2=name[:-1]
      os.mkdir(name2)
      os.chdir(name2)
      os.mkdir('1.Evidencias_de_aprendizaje')
      os.mkdir('2.Sanciones_e_indiciplina')
      os.mkdir('3.Plan_concertado')
      os.mkdir('4.Material_de_estudio')
      os.mkdir('5.Plan_de_mejoramiento')
      os.chdir("c:\\users\\302\\yo")