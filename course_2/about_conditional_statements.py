#Flow control - sunt folosite pentru a lua decizii.
#Practic s eevalueaza daca o conditie este indeplinita(esteadevarata).Daca este indeplinita, se executa ceva, daca nu este indeplinita,
# atunci se executa  altceva.
#De exemplu mergem la bancomat sa scoatem bani si avem urmatorul flow: (voi scrie in pseudocod sa se inteleaga)
#1.Prima data bagam cardul si ni se cere codul pin.Noi il introducem.
#Se face urmatoarea verificare:
# daca( if) pin corect:
#    executa_instructiune1: redirectioneaza catre alege suma
#    executa_instructiune2: alege suma
#    # din nou se va face o verificare daca aveti suma respectiva in cont
# daca( if) suma_disponibila_in_cont:
#    executa_intructiune3: primeste_bani
# altfel( else ):
#    executa_instructiune4: afiseaza "Sold insuficient, alege alta suma"
# ..................
# altfel( else ):
#    executa_instructiune5: afiseaza "Pinul este gresit"

#-----------------------< If > Syntaxa:

# if < expresie >:
#     < instructiune1 >
# ------------------------
# < If else > Syntaxa:
# if < expresie >:
#     < instructiune1 >
# else:
#     < instructiune2 >
#
# -------------------------
# < nested if else > Exemplu
# if < expresie >:
#     if < expresie >:
#         < instructiune1 >
#     else:
#         < instructiune2 >
# else:
#     < instructiune3 >
# --------------------------
# < if elif else > Syntaxa
# if < expresie >:
#     < instructiune1 >
# elif < expresie >:
#     < instructiune2 >
# elif < expresie >:
#     < instructiune3 >
# else:
#     < instructiune4 >