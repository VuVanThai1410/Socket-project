def LogIn(conn, addr):

    while True:
        try:
            print("TAO CHAY QUA SERVER ROI")
            fileAccountRead = open('ListAccount.txt', 'r')
            msgCheck = conn.recv(1024).decode("utf8")
            if msgCheck == "break":
                return
            print("LAYTK VOI MK")
            usernameRecv = conn.recv(1024).decode("utf8")
            passwordRecv = conn.recv(1024).decode("utf8")
            
            print("LAY XONG ROI")
            print(usernameRecv)
            print(passwordRecv)
            success = False
            while fileAccountRead.tell() != os.fstat(fileAccountRead.fileno()).st_size:
                lineAccount = fileAccountRead.readline()
                if lineAccount == usernameRecv + " " + passwordRecv + "\n":
                    conn.sendall(bytes("Login successfully", "utf8"))
                    success = True
                    fileAccountRead.close()
                    break
            if success == False:
                conn.sendall(bytes("Account doesn't exist", "utf8"))
            else:
                break
        except socket.error:
            return


def dang_ky(conn, addr):
    file_registry = open('DS_ng_dung.txt', 'a')
    try:
        while True:
            file_read = open('DS_ng_dung.txt', 'r')
            msg_check = conn.recv(1024).decode("utf8")
            if msg_check == "break":
                return
            username_recv = conn.recv(1024).decode("utf8")
            password_recv = conn.recv(1024).decode("utf8")
            pass_again_recv = conn.recv(1024).decode("utf8")
            check_exist = username_recv
            success = True
            while file_read.tell() != os.fstat(file_read.fileno()).st_size:
                line = file_read.readline()
                line_split = line.split(" ")

                if line_split[0] == check_exist or pass_again_recv != password_recv:
                    conn.sendall(bytes("Ten dang nhap ton tai", "utf8"))
                    success = False
                    break
            if success == True:
                file_registry.writelines(username_recv + " " + password_recv + "\n")
                conn.sendall(bytes("Dang ky thanh cong", "utf8"))
                break
        file_read.close()
        file_registry.close()
    except socket.error:
        return


# Ki???m tra v?? ghi t??i kho???n m???i v??o danh s??ch ng?????i d??ng.
    fileAccountWrite = open('ListAccount.txt', 'a')
    try:
        while True:
            print("TAO CHAY QUA SERVER ROI")
            fileAccountRead = open('ListAccount.txt', 'r')
            msgCheck = conn.recv(1024).decode("utf8")
            if msgCheck == "break":
                return
            print("LAYTK VOI MK")
            usernameRecv = conn.recv(1024).decode("utf8")
            passwordRecv = conn.recv(1024).decode("utf8")
            passwordRepRecv = conn.recv(1024).decode("utf8")
            #checkExist = usernameRecv
            success = True
            while fileAccountRead.tell() != os.fstat(fileAccountRead.fileno()).st_size:
                line = fileAccountRead.readline()
                #Chuy???n 1 d??ng th??nh 1 list g???m 2 ph???n t??? t??n t??i kho???n v?? m???t kh???u.
                lineAccount = line.split(" ")

                if lineAccount[0] == usernameRecv:  #M???I THAY BI???N checkEXist B???NG BI???N usernameRecv
                    conn.sendall(bytes("Username available", "utf8"))
                    success = False
                    break
                if passwordRepRecv != passwordRecv:
                    conn.sendall(bytes("Passwords aren't the same", "utf8"))
                    success = False
                    break
            if success == True:
                fileAccountWrite.writelines(usernameRecv + " " + passwordRecv + "\n")
                conn.sendall(bytes("Account created successfully", "utf8"))
                break
        fileAccountRead.close()
        fileAccountWrite.close()
    except socket.error:
        return
