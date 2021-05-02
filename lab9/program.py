#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mojeklasy

def testy():
    pass

print("Zadanie 4.1")
pkt1 = mojeklasy.Punkt2D(2,3)
pkt1.drukuj()
pkt1.zeruj()
pkt1.drukuj()
print()

print("Zadanie 4.2")
pkt2 = mojeklasy.Punkt3D(2,3,4)
pkt2.drukuj()
pkt2.zeruj()
pkt2.drukuj()
print()

print("Zadanie 4.3")
dluOdc = mojeklasy.Odcinek(2,3,3,5)
dluOdc.drukuj()
print()

if __name__ == "__main__":
    testy()


# In[ ]:




