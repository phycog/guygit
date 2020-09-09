'''
ไม่สามารถดึงข้อมูลที่เซฟลงไปได้(ข้อมูลโดนลบตอนเรียกข้อมูล)
สามารถเข้าถึงข้อมูลจาก txt โดยตรง หรือ เรียกผ่าน .py ตัวอื่นได้
'''

print("welcome to note creating program")
print()

dummy_location = "test_txt_db"

slot = str(input("insert slot to link data "))

save_as_txt = open(dummy_location+slot+".txt","w+")
read = open(dummy_location+slot+".txt","r")

database_note = []
database_note_txt = []

def choose():
    print("slot no. : ",slot)
    print()
    print("select 1-2-3 to do something.")
    print("insert 1 to create new note \ninsert 2 to show all saved note \ninsert 3 to exit")
    print()
    get = int(input("insert here : "))
    if get == 1:
        receive_note()
    if get == 2:
        show_database()
    if get == 3:
        print("Exit")

    else:
        print("ERROE!!")

def receive_note():
    print()
    print("lets make some note")
    print()
    topic = str(input("topic name  "))
    print()
    date = str(input("insert date  "))
    print()
    content = str(input("create the context  "))
    print()

    finished_note = [topic, date, content]

    database_note.append(finished_note)

    convert = str(finished_note)

    save_as_txt.write(convert)

    choose()



def show_database():
    print()
    for x in read:
        print(x)

    print()

    choose()

choose()






