{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Zadanie 1:\n",
      "x = 2 y = 3\n",
      "Zeruje argumenty\n",
      "x = 0 y = 0\n",
      "\n",
      "Zadanie 2:\n",
      "x = 2 y = 3 z = 4\n",
      "Zeruje argumenty\n",
      "x = 0 y = 0 z = 0\n",
      "\n",
      "Zadanie 3:\n",
      "Wynik:  2.6457513110645907\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"\n",
    "Created on Wed Apr 28 09:42:52 2021\n",
    "\n",
    "@author: Janowicz\n",
    "\"\"\"\n",
    "import math\n",
    "\n",
    "class Punkt2D():\n",
    "    def __init__(self,x,y):\n",
    "        self.x=x\n",
    "        self.y=y\n",
    "        \n",
    "    def drukuj(self):\n",
    "        print(\"x =\", self.x, \"y =\", self.y)\n",
    "        \n",
    "    def zeruj(self):\n",
    "        print(\"Zeruje argumenty\")\n",
    "        self.x = 0\n",
    "        self.y = 0\n",
    "        \n",
    "class Punkt3D(Punkt2D):\n",
    "    def __init__(self,x,y,z):\n",
    "        Punkt2D.__init__(self,x,y)\n",
    "        self.z=z\n",
    "        \n",
    "    def drukuj(self):\n",
    "        print(\"x =\", self.x,\"y =\", self.y,\"z =\", self.z)\n",
    "        \n",
    "    def zeruj(self):\n",
    "        print(\"Zeruje argumenty\")\n",
    "        self.x=0\n",
    "        self.y=0\n",
    "        self.z=0\n",
    "        \n",
    "class Odcinek(Punkt2D):\n",
    "    def __init__(self,a,b,c,d):\n",
    "        self.A=Punkt2D(a,b)\n",
    "        self.B=Punkt2D(c,d)\n",
    "        self.odl=math.sqrt((self.B.x-self.A.x)^2+(self.B.y-self.A.y)^2)\n",
    "    def drukuj(self):\n",
    "        print(\"Wynik: \",self.odl)\n",
    "\n",
    "def testy():\n",
    "    pass\n",
    "\n",
    "#Zadanie 1\n",
    "print(\"Zadanie 1:\")\n",
    "pkt1 = Punkt2D(2,3)\n",
    "pkt1.drukuj()\n",
    "pkt1.zeruj()\n",
    "pkt1.drukuj()\n",
    "print()\n",
    "\n",
    "\n",
    "#Zadanie 2\n",
    "print(\"Zadanie 2:\")\n",
    "pkt2 = Punkt3D(2,3,4)\n",
    "pkt2.drukuj()\n",
    "pkt2.zeruj()\n",
    "pkt2.drukuj()\n",
    "print()\n",
    "\n",
    "#Zadanie 3\n",
    "print(\"Zadanie 3:\")\n",
    "dluOdc = Odcinek(2,3,3,5)\n",
    "dluOdc.drukuj()\n",
    "print()\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    testy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
