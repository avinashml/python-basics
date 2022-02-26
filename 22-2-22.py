{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d44aa443",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "smaller\n"
     ]
    }
   ],
   "source": [
    "x=5\n",
    "if x<10:\n",
    "    print('smaller')\n",
    "    if x>20:\n",
    "        print('bigger')\n",
    "        print('finis')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ad857e13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "equals 5\n",
      "greater than 4\n",
      "greater than or equals 5\n",
      "less than 6\n",
      "less than or equals 5\n",
      "not equals 6\n"
     ]
    }
   ],
   "source": [
    "x=5\n",
    "if x==5:\n",
    "    print('equals 5')\n",
    "    if x>4:\n",
    "        print('greater than 4')\n",
    "        if x>=5:\n",
    "            print('greater than or equals 5')\n",
    "            if x<6:\n",
    "                print('less than 6')\n",
    "                if x<=5:\n",
    "                    print('less than or equals 5')\n",
    "                    if x!=6:\n",
    "                        print('not equals 6')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "34420822",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "before 5\n",
      "is 5\n",
      "is still 5\n",
      "third 5\n",
      "afterwards 5\n",
      "before 6\n"
     ]
    }
   ],
   "source": [
    "x=5\n",
    "print('before 5')\n",
    "if x==5:\n",
    "    print('is 5')\n",
    "    print('is still 5')\n",
    "    print('third 5')\n",
    "    print('afterwards 5')\n",
    "    print('before 6')\n",
    "    if x==6:\n",
    "        print('is 6')\n",
    "        print('is still 6')\n",
    "        print('third 6')\n",
    "        print('afterwards 6')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e887ac74",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "de25cd6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "v\n"
     ]
    }
   ],
   "source": [
    "r=3\n",
    "v=4/3*3.14*r**3\n",
    "print('v')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d5aeb27b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "v\n"
     ]
    }
   ],
   "source": [
    "r=5\n",
    "v=(4/3)*3.14*r**3\n",
    "print('v')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e20b85bf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "raw",
   "id": "22acd1f8",
   "metadata": {},
   "source": [
    "r==5\n",
    "v==(4/3)*3.14*r**3\n",
    "print('v')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9a2adaf1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "volume of the sphere904.3199999999999\n"
     ]
    }
   ],
   "source": [
    "radius=6\n",
    "pie=3.14\n",
    "volume=(4.0/3.0)*pie*(radius*radius*radius)\n",
    "print(\"volume of the sphere\"+str(volume))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "76560d37",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/1056520946.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/1056520946.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    min=60seconds\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "min=60seconds\n",
    "required time=42 min 42 seconds\n",
    "print(\"time taken\"+42*60+42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "16b64cfe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bigger than 2\n",
      "still bigger\n",
      "done with 2\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "bigger than 2\n",
      "dont with i 3\n",
      "all done\n",
      "4\n",
      "bigger than 2\n",
      "dont with i 4\n",
      "all done\n"
     ]
    }
   ],
   "source": [
    "x=5\n",
    "if x>2:\n",
    "    print('bigger than 2')\n",
    "    print('still bigger')\n",
    "    print('done with 2')\n",
    "    for i in range (5):\n",
    "        print(i)\n",
    "        if i>2:\n",
    "            print('bigger than 2')\n",
    "            print('dont with i',i)\n",
    "            print('all done')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a7ea314f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "more than 1\n",
      "less than 100\n",
      "all done\n"
     ]
    }
   ],
   "source": [
    "x=42\n",
    "if x>1:\n",
    "    print('more than 1')\n",
    "    if x<100:\n",
    "        print('less than 100')\n",
    "        print('all done')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a4d48851",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/122639318.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/122639318.py\"\u001b[1;36m, line \u001b[1;32m4\u001b[0m\n\u001b[1;33m    else:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "x=4\n",
    "if x>2:\n",
    "    print('bigger')\n",
    "    else:\n",
    "        print('smaller')\n",
    "        print('all done')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1537199b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bigger\n",
      "all done\n"
     ]
    }
   ],
   "source": [
    "x=4\n",
    "if x>2:\n",
    "    print('bigger')\n",
    "else:\n",
    "    print('smaller')\n",
    "print('all done')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "95ea1562",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "large\n",
      "all done\n"
     ]
    }
   ],
   "source": [
    "x=12\n",
    "if x<3:\n",
    "    print('small')\n",
    "elif x<8:\n",
    "    print('medium')\n",
    "else:\n",
    "    print('large')\n",
    "print('all done')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a2b9a2c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "medium\n"
     ]
    }
   ],
   "source": [
    "x=5\n",
    "if x<2:\n",
    "    print('small')\n",
    "elif x<10:\n",
    "    print('medium')\n",
    "elif x<20:\n",
    "    print('large')\n",
    "elif x<40:\n",
    "    print('huge')\n",
    "else:\n",
    "    print('ginomrous')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "cdaf70bd",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/2609334791.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/2609334791.py\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    istr=int'astr'\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "astr='hello bob'\n",
    "istr=int'astr'\n",
    "print('first',istr)\n",
    "astr='123'\n",
    "istr=int(astr)\n",
    "print('second',istr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "e686e47d",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/2609334791.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/2609334791.py\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    istr=int'astr'\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "astr='hello bob'\n",
    "istr=int'astr'\n",
    "print('first',istr)\n",
    "astr='123'\n",
    "istr=int(astr)\n",
    "print('second',istr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8abfad64",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'hello bob'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/3861015516.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mastr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'hello bob'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mistr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mastr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'first'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mistr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mastr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'123'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mistr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mastr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: 'hello bob'"
     ]
    }
   ],
   "source": [
    "astr='hello bob'\n",
    "istr=int(astr)\n",
    "print('first',istr)\n",
    "astr='123'\n",
    "istr=int(astr)\n",
    "print('second',istr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e5779d23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "first -1\n",
      "second 123\n"
     ]
    }
   ],
   "source": [
    "astr='hello ashu'\n",
    "try:\n",
    "    istr=int(astr)\n",
    "except:\n",
    "    istr=-1\n",
    "print('first',istr)\n",
    "astr='123'\n",
    "try:\n",
    "    istr=int(astr)\n",
    "except:\n",
    "    istr=-1\n",
    "print('second',astr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "440f28b7",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/2988521166.py, line 7)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/2988521166.py\"\u001b[1;36m, line \u001b[1;32m7\u001b[0m\n\u001b[1;33m    print(nice work)\u001b[0m\n\u001b[1;37m               ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "rawstr=input('enter a number:')\n",
    "try:\n",
    "    ival=int(rawstr)\n",
    "except:\n",
    "    ival=-1\n",
    "if ival>0:\n",
    "    print(nice work)\n",
    "else:\n",
    "    print('not a number')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b61427ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number:5\n",
      "nice work\n"
     ]
    }
   ],
   "source": [
    "rawstr=input('enter a number:')\n",
    "try:\n",
    "    ival=int(rawstr)\n",
    "except:\n",
    "    ival=-1\n",
    "if ival>0:\n",
    "    print('nice work')\n",
    "else:\n",
    "    print('not a number')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "0cb1c49d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number:seventy two\n",
      "not a number\n"
     ]
    }
   ],
   "source": [
    "rawstr=input('enter a number:')\n",
    "try:\n",
    "    ival=int(rawstr)\n",
    "except:\n",
    "    ival=-1\n",
    "if ival>0:\n",
    "    print('nice work')\n",
    "else:\n",
    "    print('not a number')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "8199e2f0",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '3.999999999'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/427775229.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'3.999999999'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: '3.999999999'"
     ]
    }
   ],
   "source": [
    "int('3.999999999')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ce5ffdca",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '3.99999'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/3072032848.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'3.99999'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'int'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: '3.99999'"
     ]
    }
   ],
   "source": [
    "int('3.99999')\n",
    "print('int')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3f2f53b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "2c912b74",
   "metadata": {},
   "source": [
    "degrees=45\n",
    "radians=degrees/180*math.pi\n",
    "math.sin(radians)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "bde63ddb",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/514648213.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/514648213.py\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    module 'math'(built-in)\u001b[0m\n\u001b[1;37m           ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "math\n",
    "module 'math'(built-in)\n",
    "degrees=45\n",
    "radians= degrees/180*math.pi\n",
    "math.sin(radians)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "3fe9e330",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/3441242032.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/3441242032.py\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    module 'math'(built-in)\u001b[0m\n\u001b[1;37m           ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "math\n",
    "module 'math'(built-in)\n",
    "ratio=signal_power/noise_power\n",
    "decibels=10*math.log10(ratio)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ef75c136",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7071067811865476"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "degrees=45\n",
    "radians=degrees/180*math.pi\n",
    "math.sin(radians)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "1cfe6491",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'signal_power' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/305933792.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mmath\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mratio\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msignal_power\u001b[0m\u001b[1;33m/\u001b[0m\u001b[0mnoise_power\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mdecibels\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlog10\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mratio\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'signal_power' is not defined"
     ]
    }
   ],
   "source": [
    "import math\n",
    "ratio=signal_power/noise_power\n",
    "decibels=10*math.log10(ratio)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "1e33d698",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7071067811865476"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "math.sqrt(2)/2.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a115f742",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "hours=5\n",
    "minutes=hours*60"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "06849914",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "minutes\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "hours=5\n",
    "minutes=hours*60\n",
    "print('minutes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3876455b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "minute\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "hour=5\n",
    "minute=hour*60\n",
    "print('minute')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "969a49c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "minute\n"
     ]
    }
   ],
   "source": [
    "hour=5\n",
    "minute=hour*60\n",
    "print('minute')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "afbff156",
   "metadata": {},
   "outputs": [],
   "source": [
    "def thing():\n",
    "    print('hello')\n",
    "    print('fun')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "4c502ac3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "big\n"
     ]
    }
   ],
   "source": [
    "big=max('hello')\n",
    "print('big')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "e00bf173",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tiny\n"
     ]
    }
   ],
   "source": [
    "tiny=min('hi')\n",
    "print('tiny')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "6150dd32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "big\n"
     ]
    }
   ],
   "source": [
    "big = max('hello world')\n",
    "print('big')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "5459e563",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "w\n"
     ]
    }
   ],
   "source": [
    "big=max('hello world')\n",
    "print(big)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "9e48f9ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_lyrics():\n",
    "    print(\"i'm a lumberjack, and i am okay\")\n",
    "    print(\"i sleep all night and i work all day\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "23606044",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i'm a lumberjack, and i am okay\n",
      "i sleep all night and i work all day\n",
      "i'm a lumberjack, and i am okay\n",
      "i sleep all night and i work all day\n"
     ]
    }
   ],
   "source": [
    "def print_lyrics():\n",
    "    print(\"i'm a lumberjack, and i am okay\")\n",
    "    print(\"i sleep all night and i work all day\")\n",
    "    \n",
    "def repeat_lyrics():\n",
    "    print_lyrics()\n",
    "    print_lyrics()\n",
    "    \n",
    "repeat_lyrics()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "9dc4bd23",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'print_twice' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/1250536017.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint_twice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'spam'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'print_twice' is not defined"
     ]
    }
   ],
   "source": [
    "print_twice('spam')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "a4e0fa2c",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/1100986972.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/1100986972.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    def print_twice('spam')\u001b[0m\n\u001b[1;37m                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def print_twice('spam')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "6da84830",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/431579205.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/431579205.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    def print_twice('spam'):\u001b[0m\n\u001b[1;37m                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def print_twice('spam'):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "965b5d9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_twice(bruce):\n",
    "    print(bruce)\n",
    "    print(bruce)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "35f471f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.141592653589793\n"
     ]
    }
   ],
   "source": [
    "print(math.pi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "169edb7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "52\n"
     ]
    }
   ],
   "source": [
    "print(52)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "0fe8a7b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "spamspamspamspam\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'pprint' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/2738110664.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint_twice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'spam'\u001b[0m\u001b[1;33m*\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/3586273171.py\u001b[0m in \u001b[0;36mprint_twice\u001b[1;34m(bruce)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mprint_twice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mpprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'pprint' is not defined"
     ]
    }
   ],
   "source": [
    ">>> print_twice('spam'*4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "ff255bad",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'bruce' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/787651624.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint_twice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'bruce' is not defined"
     ]
    }
   ],
   "source": [
    ">>> print_twice(bruce)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "9d1640a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.141592653589793\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'pprint' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/846879191.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint_twice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpi\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/3586273171.py\u001b[0m in \u001b[0;36mprint_twice\u001b[1;34m(bruce)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mprint_twice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mpprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'pprint' is not defined"
     ]
    }
   ],
   "source": [
    ">>> print_twice(math.pi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "807e2a17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eric, the half a bee\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'pprint' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/1209120960.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mmicheal\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'eric, the half a bee'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mprint_twice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmicheal\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/3586273171.py\u001b[0m in \u001b[0;36mprint_twice\u001b[1;34m(bruce)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mprint_twice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mpprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbruce\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'pprint' is not defined"
     ]
    }
   ],
   "source": [
    ">>> micheal='eric, the half a bee'\n",
    ">>> print_twice(micheal)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "2e67c77e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cat_twice(part1, part2):\n",
    "    cat=part1+part2\n",
    "    print_twice(cat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "be22f28d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cat_twice(part1, part2):\n",
    "    cat=part1+part2\n",
    "    print_twice(cat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "bd8e4f3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bing tiddletiddle bang\n",
      "bing tiddletiddle bang\n"
     ]
    }
   ],
   "source": [
    ">>> line1 = 'bing tiddle'\n",
    ">>> line2 = 'tiddle bang'\n",
    ">>> cat_twice(line1, line2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "4880f72d",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'cat' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_10880/3983562679.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcat\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'cat' is not defined"
     ]
    }
   ],
   "source": [
    ">>> print(cat)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "db50f046",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/3310202492.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/3310202492.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    print float(99)/100\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "print float(99)/100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "593d1918",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/2133463520.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/2133463520.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    print float(99) / 100\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "print float(99) / 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "04c0d4e3",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/2260909532.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/2260909532.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    print float(99) /100\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "print float(99) /100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "ae483ad4",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/1562098191.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/1562098191.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    print float(99)/100\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    ">>> print float(99)/100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "56cdace3",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_10880/3887045229.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\ASUS\\AppData\\Local\\Temp/ipykernel_10880/3887045229.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    print float(99) /100\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    ">>> print float(99) /100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d1ea94f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
