#imageDLforTwitter

##Overview
画像の収集をtwitterで行います  
実行すると最新50件分のタイムラインから画像(jpg, png)を収集して保存します  
コマンドライン引数に保存するディレクトリを選んでください  


##Discription

コマンドライン引数には以下のパラメータを用意しています  
--path : 必須、C:/user/username/desktopのように指定  
--followers : オプション  
1ならばフォローしているユーザー最新200人を対象に、そのユーザーツイートから最新3200件分が範囲になる  
ただし処理に時間がかかり数日程動き続けます  
--user : オプション  
@screen_nameの@以外の部分を指定してそのユーザーを基準にする、followersと併用して用いる  

##Requirement
python3以降  
requests_oauthlib  


##Usage
最新50件からの保存  
python image_dl.py --path C:/user/username/desktop  

自分がフォローしている人最新200人からの保存  
python image_dl.py --path C:/user/username/desktop --followers 1  

あるユーザー(@example)がフォローしている人最新200人からの保存  
python image_dl.py --path C:/user/username/desktop --followers 1 --user example  
