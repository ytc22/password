print('最多輸入3次密碼')
while True: # 要兩個==
    password = input('請輸入密碼:')
    x = 3
    if password == 'a123456':
        print('登入成功')
        break
    elif password != 'a123456':
        x = x-1
        print('密碼錯誤!還有'+ str(x)+ '次機會')
    else:
        x = 0
        break


# ans
password = 'a123456'
i = 3 # 剩餘機會 ※詳下面+接續
while True: #while加條件
    #password = input('請輸入密碼:')
    #不能存成password,不然會覆蓋掉
    pwd = input('請輸入密碼:') #密碼縮寫pwd
    if pwd == password: 
    # 如果打 if pwd == a123456: 這樣不好
    # 因為a123456前面就已經存入password
    # 且這樣日後修改會需要改很多地方
        print('登入成功')
        break # 逃出迴圈
    else:
        i = i - 1 # ※1：這樣才會i-1再存回i
        print('密碼錯誤!還有', i,'次機會')
        # print('密碼錯誤!還有',   ,'次機會')
        #        str          ,int, str
        # int要創造變數>>此例創造i且放最上面※

        # 但寫到這邊還沒有結束，因為i無限倒數
        if i == 0:
            break