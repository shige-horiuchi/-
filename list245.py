class aaa():
    def __init__(self, name):      # 初期化メソッド定義「__init__」
        self.name = name           # 受取った引数をself.nameに保存
    def zzz(self):                 # メソッドzzz定義
        print('Hello!! ' + self.name) # selfのname「Python」を受取って処理

bbb = aaa('Python')                # aaaの引数をnameに格納
bbb.zzz()                          # メソッドzzz呼出し

print(bbb.name)