# Salih Güdücü - 12A atp
todo_list = []

while True:
    print("Yapılacaklar Listesi Uygulaması")
    print("1 - Ekle")
    print("2 - Listele")
    print("3 - Sil")
    print("4 - Çıkış")

    choice = input("Bir seçenek seçin (1 - 4): ")
    print(" ")

    if choice == "1":
        task = input("Yapılacak görevi girin: ")
        todo_list.append(task)
        print("Görev eklendi!")
        print(" ")

    elif choice == "2":
        print("Yapılacaklar Listesi:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

    elif choice == "3":
        if len(todo_list) == 0:
            print("Liste boş!")
            print(" ")
        else:
            print("Yapılacaklar Listesi:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
                print(" ")
            
            task_index = int(input("Silmek istediğiniz görevin numarasını girin: ")) - 1
            print(" ")
            
            if 0 <= task_index < len(todo_list):
                removed_task = todo_list.pop(task_index)
                print(f"'{removed_task}' silindi.")
                print(" ")
            else:
                print("Geçersiz numara!")
                print(" ")

    elif choice == "4":
        print("Uygulama kapatılıyor!")
        break

    else:
        print("Geçersiz bir seçenek girdiniz!")
        print(" ")
