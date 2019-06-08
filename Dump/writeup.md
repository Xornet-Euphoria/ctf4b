# Dump

## 手順
対称にfileコマンドを実行すると以下のような出力が得られる。
```
fc23f13bcf6562e540ed81d1f47710af_dump: pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 262144)
```
結果からこのファイルがpcapファイルであることがわかるのでWiresharkに読み込ませる。  
この内HTTPプロトコルによる通信に注目すると  
`Request URI: /webshell.php?cmd=ls%20%2Dl%20%2Fhome%2Fctf4b%2Fflag`
ということからcmdパラメータに指定したコマンドを実行しそれを表示させているのだと考えられる。  
pcapを読むと2つのコマンドをサーバーに対して送っており、もう1つは  
`Request URI: /webshell.php?cmd=hexdump%20%2De%20%2716%2F1%20%22%2502%2E3o%20%22%20%22%5Cn%22%27%20%2Fhome%2Fctf4b%2Fflag`  
であった。これをURLエンコードをデコードして読みやすい形にすると
`hexdump -e '16/1 "%02.3o " "¥n" ' /home/ctf4b/flag`  
よってflagファイルを8進数でhexdumpしたものがレスポンスとして返ってくるはずである。  
pcapからこのレスポンスを読みバイナリを復元する(使用コードは添付)。  
このファイルをfileコマンドにかけるとgzip形式でありそこからファイルを抽出するとflagの書かれた画像が出てくる。

## Flag
ctf4b{hexdump_is_very_useful}
