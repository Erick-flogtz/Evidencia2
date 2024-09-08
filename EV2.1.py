{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.series.Series'>\n",
      "Index: 5 entries, A to E\n",
      "Series name: None\n",
      "Non-Null Count  Dtype\n",
      "--------------  -----\n",
      "5 non-null      int64\n",
      "dtypes: int64(1)\n",
      "memory usage: 80.0+ bytes\n"
     ]
    }
   ],
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
