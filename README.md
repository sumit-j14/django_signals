# django_signals
this is a demo about integrating django signals to django projects  
# a very practical use case  
lets say we have to perform a task upon creation of a database entry so we may create respective view BUT  
BUT.. what if we added something from admin panel, normal view functionality wont work in that case.  
django signals prove apt in this case!  
# what are django signals ?  
A signal is an object corresponding to particular event.  
# Two parts of signals  
# 1: sender/event  
is something which triggers signals  
# 2: receiver  
are the handler functions which have to execute as a consequence  
# Two methods of using django signals  
one is using signal.connect()function  
second is using @ receiver decorator  
# more details  
https://seddonym.me/2018/05/04/django-signals/  
# outputs using method 1   
![Screenshot from 2022-07-12 00-07-20](https://user-images.githubusercontent.com/72104547/178337670-15743015-837c-46c3-9809-3e531af194bd.png)  
# output using method 2  
![Screenshot from 2022-07-12 00-15-26](https://user-images.githubusercontent.com/72104547/178338803-6e96c2b3-a971-465e-9e5f-b9cbd88087d6.png)
