
#randomly balance the data

a = np.argmax(y_train, axis = 1)
ind1 = np.where(a == 1)
ind0 = np.where(a == 0)


x1 = X_train[ind1,:,:,:]
y1 = y_train[ind1,:]

X_train = X_train[ind0,:,:,:]
y_train = y_train[ind0,:]

print(X_train.shape, y_train.shape, x1.shape, y1.shape)

ind =np.arange(y_train.shape[0])
print(ind)
np.random.seed(101)
np.random.shuffle(ind)
print(ind)

ind0 = ind[:int(1.2*y1.shape[0])]
print(ind0)

aa = X_train[ind[:int(1.2*y1.shape[0])],:,:,:]
bb = y_train[ind[:int(1.2*y1.shape[0])],:]

print(aa.shape, bb.shape)

aa = np.append(aa,x1, axis = 0)
bb = np.append(bb,y1, axis = 0)

print(aa.shape, bb.shape)

ind =np.arange(bb.shape[0])

y_class1 = np.append(y_class1,y_temp)

np.random.seed(101)
np.random.shuffle(ind)

aa = aa[ind]

bb = bb[ind]
