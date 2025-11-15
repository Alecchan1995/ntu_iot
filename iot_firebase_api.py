from firebase import firebase
url = 'https://ntuiot-f7743-default-rtdb.firebaseio.com'
fdb = firebase.FirebaseApplication(url, None)
#fdb.post('/product',{'id':0, 'name':"noodle","table_id":1,"number":10})
fdb.post('/product',{'id':1, 'name':"water","table_id":2,"number":10})