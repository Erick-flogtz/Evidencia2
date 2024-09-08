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
     "evalue": "name 'np' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m nuevos_indices \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPepsi\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mManzanita\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSprite\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNaranjada\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPepsi Light\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[1;32m----> 2\u001b[0m arreglo_numpy \u001b[38;5;241m=\u001b[39m \u001b[43mnp\u001b[49m\u001b[38;5;241m.\u001b[39marray  ([\u001b[38;5;241m10\u001b[39m,\u001b[38;5;241m20\u001b[39m,\u001b[38;5;241m30\u001b[39m,\u001b[38;5;241m40\u001b[39m,\u001b[38;5;241m50\u001b[39m])\n\u001b[0;32m      3\u001b[0m edades_diccionario\u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mSeries(arreglo_numpy,index\u001b[38;5;241m=\u001b[39mnuevos_indices)\n\u001b[0;32m      4\u001b[0m edades_diccionario\n",
      "\u001b[1;31mNameError\u001b[0m: name 'np' is not defined"
     ]
    }
   ],
   "source": [
    "nuevos_indices = [\"Pepsi\",\"Manzanita\",\"Sprite\",\"Naranjada\",\"Pepsi Light\"]\n",
    "arreglo_numpy = np.array  ([10,20,30,40,50])\n",
    "edades_diccionario= pd.Series(arreglo_numpy,index=nuevos_indices)\n",
    "edades_diccionario"
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
