def create_disk2():
    print("Fehlende Datei disk2 erstellen wird vorbereitet …")

    disk0_byte_array = []
    disk1_byte_array = []
    disk2_byte_array = []
    disk3_byte_array = []

    with open("disk0", "rb") as d0, open("disk1", "rb") as d1, open("disk3", "rb") as d3:
        disk0_byte_array = bytearray(d0.read())
        print("Datei disk0 eingelesen")
        disk1_byte_array = bytearray(d1.read())
        print("Datei disk1 eingelesen")
        disk3_byte_array = bytearray(d3.read())
        print("Datei disk3 eingelesen")

    print("disk2 berechnen …")
    for i in range(0, len(disk0_byte_array)):
        bit_array = []
        for j in range(7, -1, -1):
            bit_array.append(
                get_bit(disk0_byte_array[i], j) ^ get_bit(disk1_byte_array[i], j) ^ get_bit(disk3_byte_array[i], j))
        bit_array_string = ""
        for digit in bit_array:
            bit_array_string += str(digit)
        disk2_byte_array.append(int(bit_array_string, 2))
    print("Datei disk2 wurde erstellt")

    with open("disk2", "wb") as d2:
        d2.write(bytearray(disk2_byte_array))


def check_parity():
    print("disk2 auf Parität prüfen wird vorbereitet …")
    with open("disk0", "rb") as d0, open("disk1", "rb") as d1, open("disk2", "rb") as d2, open("disk3", "rb") as d3:
        disk0_byte_array = bytearray(d0.read())
        print("Datei disk0 eingelesen")
        disk1_byte_array = bytearray(d1.read())
        print("Datei disk1 eingelesen")
        disk2_byte_array = bytearray(d2.read())
        print("Datei disk2 eingelesen")
        disk3_byte_array = bytearray(d3.read())
        print("Datei disk3 eingelesen")

    print("Parität wird überprüft …")
    for i in range(0, len(disk0_byte_array)):
        for j in range(7, -1, -1):
            if get_bit(disk0_byte_array[i], j) ^ get_bit(disk1_byte_array[i], j) ^ get_bit(disk2_byte_array[i], j)\
                    != get_bit(disk3_byte_array[i], j):
                print("Fehler in Byte " + str(i) + ", Bit " + str(j))
    print("Parität geprüft; System ist in konsistentem Zustand")


def tomb_RAID():
    print("Tomb raiden und die Datei zusammenbasteln …")
    with open("disk0", "rb") as d0, open("disk1", "rb") as d1, open("disk2", "rb") as d2:
        disk0_byte_array = bytearray(d0.read())
        print("Datei disk0 eingelesen")
        disk1_byte_array = bytearray(d1.read())
        print("Datei disk1 eingelesen")
        disk2_byte_array = bytearray(d2.read())
        print("Datei disk2 eingelesen")

    tombRaid_array = []

    print("Datei tombRAID.jpg wird generiert und gespeichert …")
    for i in range(0, len(disk0_byte_array) // 4096):
        disk0Part = disk0_byte_array[i * 4096:i * 4096 + 4096]
        disk1Part = disk1_byte_array[i * 4096:i * 4096 + 4096]
        disk2Part = disk2_byte_array[i * 4096:i * 4096 + 4096]
        tombRaid_array.extend(disk0Part)
        tombRaid_array.extend(disk1Part)
        tombRaid_array.extend(disk2Part)

    with open("tombRAID.jpg", "wb") as tr:
        tr.write(bytearray(tombRaid_array))

    print("Abgeschlossen!")


def get_bit(byte, position):
    return (byte >> position) & 1


create_disk2()
check_parity()
tomb_RAID()
