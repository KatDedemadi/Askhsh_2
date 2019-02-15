#ΆΣΚΗΣΗ 2
#ΓΙΝΟΜΕΝΟ ΠΡΩΤΩΝ ΠΑΡΑΓΟΝΤΩΝ
while True:
        ar=int(input("Dwste enan arithmo poy na anhkei sto diastima [2,1000000]: "))
        while ar<2 or ar>1000000:  #Έλεγχος εγκυρότητας τιμής που δόθηκε.
                print("O arithos poy dwsate den anhkei sto [2,1000000]. Dokimaste ksana!")
                ar=int(input("Dwste enan arithmo poy na anhkei sto diastima [2,1000000]: "))
        arithmos=ar
#Δημιουργούμε μια λίστα που περιέχει ολους τους πρώτους αριθμούς μεχρι το 2000
#Aρχικοποιουμε την παραπάνω λιστα με το 2 καθώς ειναι ο πρώτος πρώτος αριθμός
        prwtoi_ar=[2]
        pr=[0]
        i=3
        while i<2000:
                n=0 
                for j in range(1,i+1):
                        if i%j==0:
                                n+=1

                if n==2: #Αν ο n ειναι ίσος με 2 τότε ο αριθμος διαιρείται με τον εαυτό του και την μονάδα άρα ειναι πρώτος
                        prwtoi_ar.append(i)
                        
                i+=1
                  
        pr=[0]*(len(prwtoi_ar)+1)       
        while ar!=1:
                i=0
                while ar!=1:
                        if ar%prwtoi_ar[i]==0:
                                ar=ar//prwtoi_ar[i]
                                pr[i]+=1
                                i=0
                        else:
                                i+=1

        othoni=" "  #Αρχικοποιούμε το string othoni με το κενο καθώς στην συνέχεια θα παρει το μνμ με τις τιμές που θα εμφανίσει.
        for i in range(len(prwtoi_ar)):
                if pr[i]!=0:
                        prwtos_arithmos=str(prwtoi_ar[i])
                        dinami=str(pr[i])
                
                        othoni+="("+(prwtos_arithmos + "**" + dinami)+")" 

        print("O arithmos" ,arithmos, "mporei na graftei ws ginomeno prvtvn arithmwn:" ,othoni)
        answer=str(input("An thelete na dwsete enan kainoyrio arithmo parakalw pieste 'ENTER'."))
        if answer!="":
                break
