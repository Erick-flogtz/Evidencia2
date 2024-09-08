{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np\n",
    "\n",
    "diccionario_python = {\n",
    "    \"A\":10,\n",
    "    \"B \":20,\n",
    "    \"C\":30,\n",
    "    \"D\":40,\n",
    "    \"E\":50\n",
    "}\n",
    "\n",
    "edades_diccionario=pd.Series(diccionario_python)\n",
    "diccionario_python\n",
    "\n",
    "edades_diccionario.values\n",
    "edades_diccionario.index\n",
    "edades_diccionario.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 8\u001b[0m\n\u001b[0;32m      1\u001b[0m lista_python \u001b[38;5;241m=\u001b[39m [\n\u001b[0;32m      2\u001b[0m     [\u001b[38;5;241m10\u001b[39m,\u001b[38;5;241m20\u001b[39m,\u001b[38;5;241m30\u001b[39m,\u001b[38;5;241m40\u001b[39m],\n\u001b[0;32m      3\u001b[0m     [\u001b[38;5;241m50\u001b[39m,\u001b[38;5;241m60\u001b[39m,\u001b[38;5;241m70\u001b[39m,\u001b[38;5;241m80\u001b[39m],\n\u001b[0;32m      4\u001b[0m     [\u001b[38;5;241m90\u001b[39m,\u001b[38;5;241m100\u001b[39m,\u001b[38;5;241m110\u001b[39m,\u001b[38;5;241m120\u001b[39m],\n\u001b[0;32m      5\u001b[0m     [\u001b[38;5;241m130\u001b[39m,\u001b[38;5;241m140\u001b[39m,\u001b[38;5;241m150\u001b[39m,\u001b[38;5;241m160\u001b[39m]\n\u001b[0;32m      6\u001b[0m ]\n\u001b[1;32m----> 8\u001b[0m df \u001b[38;5;241m=\u001b[39m \u001b[43mpd\u001b[49m\u001b[38;5;241m.\u001b[39mDataFrame(lista_python)\n\u001b[0;32m      9\u001b[0m df\n",
      "\u001b[1;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "lista_python = [\n",
    "    [10,20,30,40],\n",
    "    [50,60,70,80],\n",
    "    [90,100,110,120],\n",
    "    [130,140,150,160]\n",
    "]\n",
    "\n",
    "df = pd.DataFrame(lista_python)\n",
    "df"
   ]
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
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
