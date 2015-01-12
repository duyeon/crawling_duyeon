import json
import tweepy

#tweepy를 이용한 팔로우된 트위터 유저 이름&팔로워&팔로잉 수&타임라인 크롤링 

API_KEY = 'MeZFbd05HhqXDmgSTws1TMeyR'
API_SECRET = 'FwdKMD49BNsbc4ku09GTpzpcdZxmvMHxhYFKM4ka1ouQgUOpiw'
ACCESS_KEY = '2958180889-Cw5VjkbH1o5DcFw5BA4kjW8xiiKRh1VYbEEWpLw'
ACCESS_SECRET = 'TgseUFy6xt18ai4Y0pvJls4XNGZ6teYALPLx0MFpeMbrS'

oAuth = tweepy.OAuthHandler(API_KEY, API_SECRET)
oAuth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth_handler = oAuth, api_root = '/1.1')

if __name__ == "__main__":
    userID = 2958180889
    user = api.get_user(userID)
    timeline = api.user_timeline(userID)

    f = open('../result.json','w')

    f.write("user_name:"+user.name)
    f.write('\n') 
    f.write("user_following_count:" + str(user.friends_count))
    f.write("user_followers_count:" + str(user.followers_count))
    f.write('\n\n')
    
    for id in api.friends_ids(user):
        timeline = api.user_timeline(id)
        name = api.get_user(id)
        try:
            f.write("User_name : <"+name.name+"> ")
            
            f.write("   freinds_count: ")
            count = str(name.friends_count)
            f.write(count)
            
            f.write("   followers_count:  ") 
            count_fol = str(name.followers_count)
            f.write(count_fol)
            
            f.write('\n')
        
        except UnicodeEncodeError as e:
                continue 
        for tweet in timeline:
            try:
                
                texts = tweet.text
                texts = texts.encode('utf-8')
                #texts = texts.decode('utf-8')
                #name = name.encode('utf-8')
                f.write(texts)
                f.write('\n')
              

            except UnicodeEncodeError as e:
                continue               
        f.write('\n')
    
    f.close()