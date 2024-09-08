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
      "Cell \u001b[1;32mIn[1], line 6\u001b[0m\n\u001b[0;32m      1\u001b[0m diccionario_litas \u001b[38;5;241m=\u001b[39m {\n\u001b[0;32m      2\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNombre\u001b[39m\u001b[38;5;124m\"\u001b[39m:[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCiro\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mErick\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAlissa\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMiguel\u001b[39m\u001b[38;5;124m\"\u001b[39m,],\n\u001b[0;32m      3\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEdad\u001b[39m\u001b[38;5;124m\"\u001b[39m : [\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m19\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m22\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m30\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m25\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[0;32m      4\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mArea\u001b[39m\u001b[38;5;124m\"\u001b[39m :[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGerencia\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMaquila\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mObrero\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLimpieza\u001b[39m\u001b[38;5;124m\"\u001b[39m,]\n\u001b[0;32m      5\u001b[0m }\n\u001b[1;32m----> 6\u001b[0m df \u001b[38;5;241m=\u001b[39m\u001b[43mpd\u001b[49m\u001b[38;5;241m.\u001b[39mSeries(diccionario_litas)\n\u001b[0;32m      7\u001b[0m df\n",
      "\u001b[1;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "diccionario_litas = {\n",
    "    \"Nombre\":[\"Ciro\",\"Erick\",\"Alissa\",\"Miguel\",],\n",
    "    \"Edad\" : [\"19\",\"22\",\"30\",\"25\"],\n",
    "    \"Area\" :[\"Gerencia\",\"Maquila\",\"Obrero\",\"Limpieza\",]\n",
    "}\n",
    "df =pd.Series(diccionario_litas)\n",
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
