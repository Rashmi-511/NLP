{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "61fa3bb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "de161610",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('tripadvisor_hotel_reviews.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4caf0518",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Review</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>nice hotel expensive parking got good deal sta...</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ok nothing special charge diamond member hilto...</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>nice rooms not 4* experience hotel monaco seat...</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>unique, great stay, wonderful time hotel monac...</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>great stay great stay, went seahawk game aweso...</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Review  Rating\n",
       "0  nice hotel expensive parking got good deal sta...       4\n",
       "1  ok nothing special charge diamond member hilto...       2\n",
       "2  nice rooms not 4* experience hotel monaco seat...       3\n",
       "3  unique, great stay, wonderful time hotel monac...       5\n",
       "4  great stay great stay, went seahawk game aweso...       5"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ecb66b56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>20491.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.952223</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.233030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>5.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Rating\n",
       "count  20491.000000\n",
       "mean       3.952223\n",
       "std        1.233030\n",
       "min        1.000000\n",
       "25%        3.000000\n",
       "50%        4.000000\n",
       "75%        5.000000\n",
       "max        5.000000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f351e418",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20491 entries, 0 to 20490\n",
      "Data columns (total 2 columns):\n",
      " #   Column  Non-Null Count  Dtype \n",
      "---  ------  --------------  ----- \n",
      " 0   Review  20491 non-null  object\n",
      " 1   Rating  20491 non-null  int64 \n",
      "dtypes: int64(1), object(1)\n",
      "memory usage: 320.3+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "08c30bfc",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['length']=df['Review'].apply(len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c5d30972",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Review</th>\n",
       "      <th>Rating</th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>nice hotel expensive parking got good deal sta...</td>\n",
       "      <td>4</td>\n",
       "      <td>593</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ok nothing special charge diamond member hilto...</td>\n",
       "      <td>2</td>\n",
       "      <td>1689</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>nice rooms not 4* experience hotel monaco seat...</td>\n",
       "      <td>3</td>\n",
       "      <td>1427</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>unique, great stay, wonderful time hotel monac...</td>\n",
       "      <td>5</td>\n",
       "      <td>600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>great stay great stay, went seahawk game aweso...</td>\n",
       "      <td>5</td>\n",
       "      <td>1281</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Review  Rating  length\n",
       "0  nice hotel expensive parking got good deal sta...       4     593\n",
       "1  ok nothing special charge diamond member hilto...       2    1689\n",
       "2  nice rooms not 4* experience hotel monaco seat...       3    1427\n",
       "3  unique, great stay, wonderful time hotel monac...       5     600\n",
       "4  great stay great stay, went seahawk game aweso...       5    1281"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d78b5b9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x2bff9a2ebb0>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABdEAAAEiCAYAAAAWHJuuAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA28ElEQVR4nO3de5BV5Zkv4F/LpQXEVjDQEEGJIhrBBDUiJBNwVMSREI81YoIHNRriFcXoKI4ZLzkR1MRLIhPvhcYbOpWYyYkZBCbKjAFEUSbeQmJEvIEYg40esUFY5w/LHVvcSgPdm7afp2pV0Wt9e633W0X9Ct799VpVRVEUAQAAAAAA1rNVpQsAAAAAAIAtlSY6AAAAAACUoYkOAAAAAABlaKIDAAAAAEAZmugAAAAAAFCGJjoAAAAAAJShiQ4AAAAAAGVoogMAAAAAQBma6AAAAAAAUIYmOi3e888/n6qqqixcuLDSpQCtjPwBKkkGAZUkg4BKkkE0N010msVxxx2XqqqqVFVVpW3btundu3dOPvnkrFixotHnOfzwwxvs69WrV5YuXZr+/ftvxoqbxiWXXJIhQ4akY8eO2W677SpdDrQK8ue9f2CecMIJ6dOnTzp06JBddtklF154YVavXl3p0uBTTwa9Z9SoUendu3e23nrr9OjRI2PHjs0rr7xS6bLgU08GNVRfX58vfvGLGm/QTGTQe3beeefSfXh/mzhxYqXLopE00Wk2I0aMyNKlS/P888/npptuyv/9v/83p5xyyiaft02bNqmtrU3btm03Q5VNa/Xq1TnyyCNz8sknV7oUaFVae/784Q9/yLp163L99dfnqaeeylVXXZXrrrsu//zP/1zp0qBVaO0ZlCQHHHBA7rnnnixatCg///nP8+c//zn/+I//WOmyoFWQQX9zzjnnpGfPnpUuA1oVGfSe73//+1m6dGlp+973vlfpkmgkTXSaTXV1dWpra7Pjjjtm+PDhOeqoozJjxozS8bVr1zZYKdmvX7/8+Mc/Lh2/6KKLcuutt+bf//3fS9/cPfjgg+v9Cs+DDz6Yqqqq/Od//mf23XffdOzYMUOGDMmiRYsa1PODH/wg3bp1S+fOnfPtb387EydOzBe/+MUmvQcXX3xxzjzzzAwYMKBJrwM01NrzZ8SIEZk6dWqGDx+ez33ucxk1alTOPvvs/OIXv2iyawJ/09ozKEnOPPPM7L///tlpp50yZMiQTJw4MfPmzcuaNWua9LqADHrff/zHf2TGjBn50Y9+1OTXAv5GBr2nc+fOqa2tLW3bbLNNk1+TzUsTnYp47rnnMn369LRr1660b926ddlxxx1zzz335Omnn84FF1yQf/7nf84999yTJDn77LMzevTo0reYS5cuzZAhQ8pe4/zzz88VV1yRRx99NG3bts3xxx9fOnbHHXfkkksuyWWXXZYFCxakd+/eufbaaz+x7m222eZjt0MPPXQT7grQHOTPe+rq6tKlS5dGfQbYdDIo+etf/5o77rgjQ4YMaXAfgKbXWjPo1Vdfzbhx43LbbbelY8eOn3g9oGm01gxKkssuuyxdu3bNF7/4xVxyySUerdkCtYzfeeBT4de//nW22WabrF27Nu+8806S5Morrywdb9euXS6++OLSz3369MmcOXNyzz33ZPTo0dlmm23SoUOH1NfXp7a29hOvd8kll2To0KFJkokTJ+awww7LO++8k6233jrXXHNNTjjhhHzrW99KklxwwQWZMWNG3nrrrY895yc9N69Dhw6fWBfQ/ORPQ3/+859zzTXX5IorrtjgzwAbTwa959xzz82UKVPy9ttvZ//998+vf/3rT/wMsOlaewYVRZHjjjsuJ510Uvbdd988//zznzgHYPNp7RmUJGeccUb23nvvbL/99pk/f37OO++8LF68ODfddNMnzocthyY6zeaAAw7Itddem7fffjs33XRT/vjHP2b8+PENxlx33XW56aabsmTJkqxatSqrV6/e6F+r2WuvvUp/7tGjR5Jk+fLl6d27dxYtWrTeM7j222+//Pa3v/3Yc+66664bVQtQWfLnb1555ZWMGDEiRx55ZL797W9vlnMCH08Gveef/umfcsIJJ2TJkiW5+OKLc8wxx+TXv/51qqqqNvncQHmtPYOuueaarFy5Muedd95GnwPYeK09g5L3Hmv3wfq23377/OM//mNpdTotg8e50Gw6deqUXXfdNXvttVd+8pOfpL6+vsG3jffcc0/OPPPMHH/88ZkxY0YWLlyYb33rWxv9Ky4f/PWg9/9ztm7duvX2va8oik88p8e5QMskf97zyiuv5IADDsjgwYNzww03bOh0gE0kg96zww47ZLfddsvBBx+cadOm5Te/+U3mzZu3odMCNlJrz6Df/va3mTdvXqqrq9O2bdtSM2zffffNscce26i5AY3X2jPoo+y///5JkmeffbZRn6OyrESnYi688MIceuihOfnkk9OzZ8/893//d4YMGdLgW8E///nPDT7Tvn37rF27dpOv3a9fv8yfPz9jx44t7Xv00Uc/8XMe5wKfDq0xf15++eUccMAB2WeffTJ16tRstZXv0aFSWmMGfdj7/2Gtr69v1OeATdfaMugnP/lJfvCDH5R+fuWVV3LIIYfk7rvvzqBBgz65aGCzam0Z9FEef/zxJH9bKU/LoIlOxQwbNix77rlnJk2alClTpmTXXXfNz372s9x///3p06dPbrvttjzyyCPp06dP6TM777xz7r///ixatChdu3ZNTU3NRl17/PjxGTduXPbdd98MGTIkd999d37/+9/nc5/73Md+blN/heeFF17IX//617zwwgtZu3ZtKYh33XVXb2aGZtTa8ueVV17JsGHD0rt37/zoRz/Ka6+9Vjq2Ic8VBDav1pZB8+fPz/z58/OVr3wl22+/fZ577rlccMEF2WWXXTJ48OCNPi+wcVpbBvXu3bvBz+//v2uXXXbJjjvuuNHnBTZOa8uguXPnZt68eTnggANSU1OTRx55JGeeeWZGjRq1Xj6xZbMMjYr67ne/mxtvvDEvvvhiTjrppBxxxBE56qijMmjQoLz++uvrPatq3Lhx6devX/bdd9985jOfye9+97uNuu7RRx+d8847L2effXb23nvvLF68OMcdd1y23nrrzTGtsi644IIMHDgwF154Yd56660MHDgwAwcO3KBvPoHNqzXlz4wZM/Lss8/mt7/9bXbcccf06NGjtAGV0ZoyqEOHDvnFL36RAw88MP369cvxxx+f/v37Z/bs2amurm6y6wLltaYMArY8rSmDqqurc/fdd2fYsGH5/Oc/nwsuuCDjxo3LXXfd1WTXpGlUFRvy8B9oBQ4++ODU1tbmtttuq3QpQCsjf4BKkkFAJckgoJJkEBvK41xold5+++1cd911OeSQQ9KmTZvcddddmTVrVmbOnFnp0oBPOfkDVJIMAipJBgGVJIPYFFai0yqtWrUqX/va1/LYY4+lvr4+/fr1y/e+970cccQRlS4N+JSTP0AlySCgkmQQUEkyiE2hiQ4AAAAAAGV4sSgAAAAAAJShiQ4AAAAAAGVoogMAAAAAQBmf2iZ6URRZuXJlPPIdqAQZBFSSDAIqSQYBlSSDgKbwqW2iv/nmm6mpqcmbb75Z6VKAVkgGAZUkg4BKkkFAJckgoCl8apvoAAAAAACwqTTRAQAAAACgDE10AAAAAAAoQxMdAAAAAADK0EQHAAAAAIAyNNEBAAAAAKAMTXQAAAAAAChDEx0AAAAAAMrQRAcAAAAAgDLaVroAAAAAAKiUnSfe12Tnfv7Sw5rs3EDzsRIdAAAAAADKaFQT/d133833vve99OnTJx06dMjnPve5fP/738+6detKY4qiyEUXXZSePXumQ4cOGTZsWJ566qkG56mvr8/48eOzww47pFOnThk1alReeumlBmNWrFiRsWPHpqamJjU1NRk7dmzeeOONjZ8pAAAAAAA0UqOa6Jdddlmuu+66TJkyJc8880wuv/zy/PCHP8w111xTGnP55ZfnyiuvzJQpU/LII4+ktrY2Bx98cN58883SmAkTJuTee+/NtGnT8tBDD+Wtt97KyJEjs3bt2tKYMWPGZOHChZk+fXqmT5+ehQsXZuzYsZthygAAAAAAsGEa9Uz0uXPn5utf/3oOO+y95zntvPPOueuuu/Loo48meW8V+tVXX53zzz8/RxxxRJLk1ltvTffu3XPnnXfmxBNPTF1dXW6++ebcdtttOeigg5Ikt99+e3r16pVZs2blkEMOyTPPPJPp06dn3rx5GTRoUJLkxhtvzODBg7No0aL069dvs90AAAAAAAAop1Er0b/yla/kP//zP/PHP/4xSfI///M/eeihh/IP//APSZLFixdn2bJlGT58eOkz1dXVGTp0aObMmZMkWbBgQdasWdNgTM+ePdO/f//SmLlz56ampqbUQE+S/fffPzU1NaUxH1ZfX5+VK1c22ACaiwwCKkkGAZUkg4BKkkFAc2hUE/3cc8/NN7/5zey+++5p165dBg4cmAkTJuSb3/xmkmTZsmVJku7duzf4XPfu3UvHli1blvbt22f77bf/2DHdunVb7/rdunUrjfmwyZMnl56fXlNTk169ejVmagCbRAYBlSSDgEqSQUAlySCgOTSqiX733Xfn9ttvz5133pnHHnsst956a370ox/l1ltvbTCuqqqqwc9FUay378M+POajxn/cec4777zU1dWVthdffHFDpwWwyWQQUEkyCKgkGQRUkgwCmkOjnon+T//0T5k4cWK+8Y1vJEkGDBiQJUuWZPLkyTn22GNTW1ub5L2V5D169Ch9bvny5aXV6bW1tVm9enVWrFjRYDX68uXLM2TIkNKYV199db3rv/baa+utcn9fdXV1qqurGzMdgM1GBgGVJIOASpJBQCXJIKA5NGol+ttvv52ttmr4kTZt2mTdunVJkj59+qS2tjYzZ84sHV+9enVmz55dapDvs88+adeuXYMxS5cuzZNPPlkaM3jw4NTV1WX+/PmlMQ8//HDq6upKYwAAAAAAoKk1aiX61772tVxyySXp3bt39txzzzz++OO58sorc/zxxyd57xEsEyZMyKRJk9K3b9/07ds3kyZNSseOHTNmzJgkSU1NTU444YScddZZ6dq1a7p06ZKzzz47AwYMyEEHHZQk2WOPPTJixIiMGzcu119/fZLkO9/5TkaOHJl+/fptzvkDAAAAAEBZjWqiX3PNNfmXf/mXnHLKKVm+fHl69uyZE088MRdccEFpzDnnnJNVq1bllFNOyYoVKzJo0KDMmDEjnTt3Lo256qqr0rZt24wePTqrVq3KgQcemFtuuSVt2rQpjbnjjjty+umnZ/jw4UmSUaNGZcqUKZs6XwAAAAAA2GBVRVEUlS6iKaxcuTI1NTWpq6vLtttuW+lygFZGBgGVJIOASpJBQCVtTAbtPPG+Jqvn+UsPa7JzA82nUc9EBwAAAACA1kQTHQAAAAAAytBEBwAAAACAMjTRAQAAAACgDE10AAAAAAAoQxMdAAAAAADK0EQHAAAAAIAyNNEBAAAAAKAMTXQAAAAAAChDEx0AAAAAAMrQRAcAAAAAgDI00QEAAAAAoAxNdAAAAAAAKEMTHQAAAAAAytBEBwAAAACAMjTRAQAAAACgDE10AAAAAAAoQxMdAAAAAADK0EQHAAAAAIAyNNEBAAAAAKAMTXQAAAAAAChDEx0AAAAAAMrQRAcAAAAAgDI00QEAAAAAoAxNdAAAAAAAKEMTHQAAAAAAytBEBwAAAACAMjTRAQAAAACgDE10AAAAAAAoQxMdAAAAAADK0EQHAAAAAIAyNNEBAAAAAKAMTXQAAAAAAChDEx0AAAAAAMrQRAcAAAAAgDI00QEAAAAAoAxNdAAAAAAAKKPRTfSXX345//t//+907do1HTt2zBe/+MUsWLCgdLwoilx00UXp2bNnOnTokGHDhuWpp55qcI76+vqMHz8+O+ywQzp16pRRo0blpZdeajBmxYoVGTt2bGpqalJTU5OxY8fmjTfe2LhZAgAAAADARmhUE33FihX58pe/nHbt2uU//uM/8vTTT+eKK67IdtttVxpz+eWX58orr8yUKVPyyCOPpLa2NgcffHDefPPN0pgJEybk3nvvzbRp0/LQQw/lrbfeysiRI7N27drSmDFjxmThwoWZPn16pk+fnoULF2bs2LGbPmMAAAAAANhAbRsz+LLLLkuvXr0yderU0r6dd9659OeiKHL11Vfn/PPPzxFHHJEkufXWW9O9e/fceeedOfHEE1NXV5ebb745t912Ww466KAkye23355evXpl1qxZOeSQQ/LMM89k+vTpmTdvXgYNGpQkufHGGzN48OAsWrQo/fr129R5AwAAAADAJ2rUSvRf/epX2XfffXPkkUemW7duGThwYG688cbS8cWLF2fZsmUZPnx4aV91dXWGDh2aOXPmJEkWLFiQNWvWNBjTs2fP9O/fvzRm7ty5qampKTXQk2T//fdPTU1NacyH1dfXZ+XKlQ02gOYig4BKkkFAJckgoJJkENAcGtVEf+6553Lttdemb9++uf/++3PSSSfl9NNPz89+9rMkybJly5Ik3bt3b/C57t27l44tW7Ys7du3z/bbb/+xY7p167be9bt161Ya82GTJ08uPT+9pqYmvXr1aszUADaJDAIqSQYBlSSDgEqSQUBzaFQTfd26ddl7770zadKkDBw4MCeeeGLGjRuXa6+9tsG4qqqqBj8XRbHevg/78JiPGv9x5znvvPNSV1dX2l588cUNnRbAJpNBQCXJIKCSZBBQSTIIaA6NeiZ6jx498vnPf77Bvj322CM///nPkyS1tbVJ3ltJ3qNHj9KY5cuXl1an19bWZvXq1VmxYkWD1ejLly/PkCFDSmNeffXV9a7/2muvrbfK/X3V1dWprq5uzHQANhsZBFSSDAIqSQYBlSSDgObQqJXoX/7yl7No0aIG+/74xz9mp512SpL06dMntbW1mTlzZun46tWrM3v27FKDfJ999km7du0ajFm6dGmefPLJ0pjBgwenrq4u8+fPL415+OGHU1dXVxoDAAAAAABNrVEr0c8888wMGTIkkyZNyujRozN//vzccMMNueGGG5K89wiWCRMmZNKkSenbt2/69u2bSZMmpWPHjhkzZkySpKamJieccELOOuusdO3aNV26dMnZZ5+dAQMG5KCDDkry3ur2ESNG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AAAAQBma6AAAAAAAUIYmOgAAAAAAlKGJDgAAAAAAZWiiAwAAAABAGZroAAAAAABQhiY6AAAAAACUoYkOAAAAAABlaKIDAAAAAEAZmugAAAAAAFCGJjoAAAAAAJShiQ4AAAAAAGVoogMAAAAAQBma6AAAAAAAUIYmOgAAAAAAlKGJDgAAAAAAZWiiAwAAAABAGZroAAAAAABQhiY6AAAAAACUoYkOAAAAAABlaKIDAAAAAEAZmugAAAAAAFCGJjoAAAAAAJTRqCb65MmT86UvfSmdO3dOt27dcvjhh2fRokUNxhRFkYsuuig9e/ZMhw4dMmzYsDz11FMNxtTX12f8+PHZYYcd0qlTp4waNSovvfRSgzErVqzI2LFjU1NTk5qamowdOzZvvPHGxs0SAAAAAAA2QqOa6LNnz86pp56aefPmZebMmXn33XczfPjw/L//9/9KYy6//PJceeWVmTJlSh555JHU1tbm4IMPzptvvlkaM2HChNx7772ZNm1aHnroobz11lsZOXJk1q5dWxozZsyYLFy4MNOnT8/06dOzcOHCjB07djNMGQAAAAAANkzbxgyePn16g5+nTp2abt26ZcGCBfnqV7+aoihy9dVX5/zzz88RRxyRJLn11lvTvXv33HnnnTnxxBNTV1eXm2++ObfddlsOOuigJMntt9+eXr16ZdasWTnkkEPyzDPPZPr06Zk3b14GDRqUJLnxxhszePDgLFq0KP369dsccwcAAAAAgI+1Sc9Er6urS5J06dIlSbJ48eIsW7Ysw4cPL42prq7O0KFDM2fOnCTJggULsmbNmgZjevbsmf79+5fGzJ07NzU1NaUGepLsv//+qampKY0BAAAAAICm1qiV6B9UFEW++93v5itf+Ur69++fJFm2bFmSpHv37g3Gdu/ePUuWLCmNad++fbbffvv1xrz/+WXLlqVbt27rXbNbt26lMR9WX1+f+vr60s8rV67cyJkBNJ4MAipJBgGVJIOASpJBQHPY6JXop512Wn7/+9/nrrvuWu9YVVVVg5+Lolhv34d9eMxHjf+480yePLn0EtKampr06tVrQ6YBsFnIIKCSZBBQSTIIqCQZBDSHjWqijx8/Pr/61a/ywAMPZMcddyztr62tTZL1VosvX768tDq9trY2q1evzooVKz52zKuvvrredV977bX1Vrm/77zzzktdXV1pe/HF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NxhNafz48fnVr36VBx54IDvuuOPHju3Ro0d22mmn/OlPf0qS1NbWZvXq1VmxYkWDcR+cQ21tbV599dX1zvXaa69tlnl26tQpAwYMyJ/+9KfSW5k/7p5WsuYlS5Zk1qxZ+fa3v/2x47bE+9yc97a2tna966xYsSJr1qzZqLmsWbMmo0ePzuLFizNz5swG3zp+lL333jvt2rVrcP+bu+bmIINkUDlb4n2WQTKoqcig5qtZBsmgLYkMkkHlbIn3WQbJoKYig5qvZhkkgzbZRj5L/VNjv/32K04++eQG+/bYY49meZHEunXrilNPPbXo2bNn8cc//nGDPvOXv/ylqK6uLm699daiKP724oC77767NOaVV175yBcHPPzww6Ux8+bN22wvZXjnnXeKz372s8XFF19cetnBZZddVjpeX1//kS87qETNF154YVFbW1usWbPmY8dtCfc5ZV4k0Rz39v2XMrzyyiulMdOmTduoF0msXr26OPzww4s999yzwVu7P84TTzzR4KUqTVlzpckgGfRRtoT7LINkUFOTQTLo48ggGdTUZJAM+jgySAY1NRkkgz6ODNoyM6jVN9GnTZtWtGvXrrj55puLp59+upgwYULRqVOn4vnnn2/ya5988slFTU1N8eCDDxZLly4tbW+//XZRFEXx5ptvFmeddVYxZ86cYvHixcUDDzxQDB48uPjsZz9brFy5snSek046qdhxxx2LWbNmFY899ljx93//98UXvvCF4t133y2NGTFiRLHXXnsVc+fOLebOnVsMGDCgGDly5EbVfdZZZxUPPvhg8dxzzxXz5s0rRo4cWXTu3Ll0zy699NKipqam+MUvflE88cQTxTe/+c2iR48eFa25KIpi7dq1Re/evYtzzz23wf4t6T6/+eabxeOPP148/vjjRZLiyiuvLB5//PHSm4ub696+++67Rf/+/YsDDzyweOyxx4pZs2YVO+64Y3Haaac1quY1a9YUo0aNKnbcccdi4cKFDf6e19fXF0VRFM8++2xx8cUXF4888kixePHi4r777it23333YuDAgU1W85ZEBjWeDJJBG1qzDPpkMqjxZJAM2tCaZdAnk0GNJ4Nk0IbWLIM+mQxqPBkkgza05k9jBrX6JnpRFMW//uu/FjvttFPRvn37Yu+99y5929HUknzkNnXq1KIoiuLtt98uhg8fXnzmM58p2rVrV/Tu3bs49thjixdeeKHBeVatWlWcdtppRZcuXYoOHToUI0eOXG/M66+/Xhx99NFF586di86dOxdHH310sWLFio2q+6ijjip69OhRtGvXrujZs2dxxBFHFE899VTp+Lp160rf8FVXVxdf/epXiyeeeKKiNRdFUdx///1FkmLRokUN9m9J9/mBBx74yL8Txx57bFEUzXtvlyxZUhx22GFFhw4dii5duhSnnXZa8c477zSq5sWLF5f9e/7AAw8URVEUL7zwQvHVr3616NKlS9G+fftil112KU4//fTi9ddfb7KatzQyqHFkkAza0Jpl0IaRQY0jg2TQhtYsgzaMDGocGSSDNrRmGbRhZFDjyCAZtKE1fxozqKooiiIAAAAAAMB6WvWLRQEAAAAA4ONoogMAAAAAQBma6AAAAAAAUIYmOgAAAAAAlKGJDgAAAAAAZWiiAwAAAABAGZroAAAAAABQhiY6AAAAAACUoYnOFm/YsGGZMGFCpcvIgw8+mKqqqrzxxhuVLgVoRjIIqCQZBFSSDAIqSQaxJdFEh4+wpQQ10DrJIKCSZBBQSTIIqCQZRDma6AAAAAAAUIYmOi3K6tWrc8455+Szn/1sOnXqlEGDBuXBBx8sHb/llluy3Xbb5f77788ee+yRbbbZJiNGjMjSpUtLY959992cfvrp2W677dK1a9ece+65OfbYY3P44YcnSY477rjMnj07P/7xj1NVVZWqqqo8//zzpc8vWLAg++67bzp27JghQ4Zk0aJFzTR7oNJkEFBJMgioJBkEVJIMotI00WlRvvWtb+V3v/tdpk2blt///vc58sgjM2LEiPzpT38qjXn77bfzox/9KLfddlv+67/+Ky+88ELOPvvs0vHLLrssd9xxR6ZOnZrf/e53WblyZX75y1+Wjv/4xz/O4MGDM27cuCxdujRLly5Nr169SsfPP//8XHHFFXn00UfTtm3bHH/88c0yd6DyZBBQSTIIqCQZBFSSDKLiCtjCDR06tDjjjDOKZ599tqiqqipefvnlBscPPPDA4rzzziuKoiimTp1aJCmeffbZ0vF//dd/Lbp37176uXv37sUPf/jD0s/vvvtu0bt37+LrX//6etf8oAceeKBIUsyaNau077777iuSFKtWrdocUwW2QDIIqCQZBFSSDAIqSQaxJWlbgb49bJTHHnssRVFkt912a7C/vr4+Xbt2Lf3csWPH7LLLLqWfe/TokeXLlydJ6urq8uqrr2a//fYrHW/Tpk322WefrFu3boPq2GuvvRqcO0mWL1+e3r17N35SQIshg4BKkkFAJckgoJJkEFsCTXRajHXr1qVNmzZZsGBB2rRp0+DYNttsU/pzu3btGhyrqqpKURTr7fugDx//OB88//vn2dDABVouGQRUkgwCKkkGAZUkg9gSeCY6LcbAgQOzdu3aLF++PLvuumuDrba2doPOUVNTk+7du2f+/PmlfWvXrs3jjz/eYFz79u2zdu3azVo/0LLJIKCSZBBQSTIIqCQZxJbASnRajN122y1HH310jjnmmFxxxRUZOHBg/vKXv+S3v/1tBgwYkH/4h3/YoPOMHz8+kydPzq677prdd98911xzTVasWNHg28idd945Dz/8cJ5//vlss8026dKlS1NNC2ghZBBQSTIIqCQZBFSSDGJLYCU6LcrUqVNzzDHH5Kyzzkq/fv0yatSoPPzwww3elvxJzj333Hzzm9/MMccck8GDB2ebbbbJIYcckq233ro05uyzz06bNm3y+c9/Pp/5zGfywgsvNMV0gBZGBgGVJIOASpJBQCXJICqtqmjMw3/gU2jdunXZY489Mnr06Pyf//N/Kl0O0MrIIKCSZBBQSTIIqCQZRGN4nAutzpIlSzJjxowMHTo09fX1mTJlShYvXpwxY8ZUujSgFZBBQCXJIKCSZBBQSTKITeFxLrQ6W221VW655ZZ86Utfype//OU88cQTmTVrVvbYY49Klwa0AjIIqCQZBFSSDAIqSQaxKTzOBQAAAAAAyrASHQAAAAAAytBEBwAAAACAMjTRAQAAAACgDE10AAAAAAAoQxMdAAAAAADK0EQHAAAAAIAyNNEBAAAAAKAMTXQAAAAAAChDEx0AAAAAAMr4/xwxJWGebi6XAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1500x300 with 5 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "g=sns.FacetGrid(df,col='Rating')\n",
    "g.map(plt.hist,'length')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4a4498ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Rating', ylabel='length'>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk0AAAGyCAYAAAD51vAJAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABUSElEQVR4nO3dfVhUZf4/8PcMDwMiTILAMIDlppGEEmEYuru13xTtK7oE/LQo0tZF3QqX1HzYNtf6lm5WaumuonWVmYUuCD1skbabtuYDimKZZlmWgIOQ4PCQDgjn94dfzpeRAUbmMOfMnPfruua65Nw3M59xmDmfuc99f26NIAgCiIiIiKhbWrkDICIiInIFTJqIiIiI7MCkiYiIiMgOTJqIiIiI7MCkiYiIiMgOTJqIiIiI7MCkiYiIiMgOTJqIiIiI7MCkiYiIiMgOnnIH4E7a2tpw9uxZ+Pv7Q6PRyB0OERER2UEQBDQ0NMBoNEKr7WY8SZDR7t27heTkZCEsLEwAIBQWFnbZd+bMmQIAYdWqVVbHL126JDz22GNCUFCQ0K9fP2HSpElCeXm5VZ/a2lrhwQcfFAICAoSAgADhwQcfFOrq6qz6/Pjjj0JycrLQr18/ISgoSMjOzhYsFss1PZ/y8nIBAG+88cYbb7zx5oK3q/OHq8k60tTU1ITY2Fg8/PDDSEtL67JfUVERDhw4AKPR2KktJycH77//PvLy8hAUFIR58+YhOTkZpaWl8PDwAABkZGSgoqICxcXFAICZM2ciMzMT77//PgCgtbUVEydORHBwMPbs2YPz589j2rRpEAQBa9assfv5+Pv7AwDKy8sREBBg9+8RERGRfOrr6xEZGSmex7t0TUMpfQiwPdJUUVEhhIeHC8eOHROuv/56q5GmCxcuCF5eXkJeXp54rLKyUtBqtUJxcbEgCIJw/PhxAYCwf/9+sc++ffsEAMLXX38tCIIgfPjhh4JWqxUqKyvFPu+8846g0+kEs9ls93Mwm80CgGv6HSIiIpKXvedvRU8Eb2trQ2ZmJp544gnccsstndpLS0vR0tKCpKQk8ZjRaERMTAz27t0LANi3bx/0ej1GjRol9rnjjjug1+ut+sTExFiNZI0fPx4WiwWlpaVdxmexWFBfX291IyIiIvek6KTp+eefh6enJ+bMmWOzvaqqCt7e3hgwYIDV8dDQUFRVVYl9QkJCOv1uSEiIVZ/Q0FCr9gEDBsDb21vsY8vy5cuh1+vFW2Rk5DU9PyIiInIdik2aSktL8fLLL+ONN9645pVogiBY/Y6t3+9Nn6stXrwYZrNZvJWXl19TnEREROQ6FJs0/ec//0F1dTUGDRoET09PeHp64scff8S8efNwww03AAAMBgOam5tRV1dn9bvV1dXiyJHBYMC5c+c63X9NTY1Vn6tHlOrq6tDS0tJpBKojnU6HgIAAqxsRERG5J8UmTZmZmfjiiy9QVlYm3oxGI5544gl8/PHHAID4+Hh4eXlh586d4u+ZTCYcO3YMo0ePBgAkJibCbDajpKRE7HPgwAGYzWarPseOHYPJZBL77NixAzqdDvHx8c54ukRERKRwspYcaGxsxKlTp8SfT58+jbKyMgQGBmLQoEEICgqy6u/l5QWDwYCoqCgAgF6vx4wZMzBv3jwEBQUhMDAQ8+fPx/DhwzF27FgAwLBhwzBhwgRkZWUhNzcXwJWSA8nJyeL9JCUlITo6GpmZmXjhhRdQW1uL+fPnIysri6NHREREBEDmkaZDhw4hLi4OcXFxAIC5c+ciLi4OS5Yssfs+Vq1ahZSUFEyZMgVjxoxBv3798P7774s1mgBgy5YtGD58OJKSkpCUlIQRI0Zg8+bNYruHhwf++c9/wsfHB2PGjMGUKVOQkpKCF198UbonS0RERC5NIwiCIHcQ7qK+vh56vR5ms5kjVERERC7C3vO3Yuc0ERERESkJkyYiIjuUlJQgKyvLalEJEakLkyYioh5YLBasX78eNTU1yM3NhcVikTskIpIBkyYioh7k5+eL9eBqa2tRUFAgc0REJAcmTURE3TCZTNi+fTva18wIgoCCggKrum5EpA5MmoiIuiAIAjZs2ICrFxl3dZyI3BuTJiKiLlRUVODIkSNoa2uzOt7W1oYjR46goqJCpsiISA5MmoiIuhAREYG4uDhotdYflVqtFnFxcYiIiJApMiKSA5MmIqIuaDQazJw5ExqNxq7jROTemDQREXUjLCwMqampYoKk0WiQlpaGsLAwmSMjImdj0kRE1IP09HQMGDAAABAYGIi0tDSZIyIiOTBpIiLqgU6nw+zZsxEcHIxZs2ZBp9PJHRIRycBT7gCIiFxBQkICEhIS5A6DiGTEkSYiIiIiOzBpIiIiIrIDkyYiIiIiOzBpIiIiIrIDkyYiIiIiOzBpIiIiIrIDkyYiIiIiOzBpIiIiol4pKSlBVlYWSkpK5A7FKZg0ERER0TWzWCxYv349ampqkJubC4vFIndIfY5JExEREV2z/Px81NXVAQBqa2tRUFAgc0R9j0kTERERXROTyYTt27dDEAQAgCAIKCgogMlkkjmyvsWkiYiIiOwmCAI2bNggJkw9HXcnTJqIiIjIbhUVFThy5Aja2tqsjre1teHIkSOoqKiQKbK+x6SJiIiI7BYREYG4uDhotdYphFarRVxcHCIiImSKrO8xaSIiIiK7aTQazJw5ExqNxq7j7oRJExEREV2TsLAwpKamigmSRqNBWloawsLCZI6sbzFpIiIiomuWnp6OAQMGAAACAwORlpYmc0R9j0kTERERXTOdTofZs2cjODgYs2bNgk6nkzukPucpdwBERETkmhISEpCQkCB3GE7DkSYiIiIiOzBpIiIiIrIDkyYiIiIiOzBpIiIiIrIDkyYiIiIiOzBpIiIiIrIDkyYiIiIiO8iaNH322WeYNGkSjEYjNBoNioqKxLaWlhYsXLgQw4cPh5+fH4xGIx566CGcPXvW6j4sFguys7MxcOBA+Pn5YfLkyZ12WK6rq0NmZib0ej30ej0yMzNx4cIFqz5nzpzBpEmT4Ofnh4EDB2LOnDlobm7uq6dORERELkbWpKmpqQmxsbFYu3Ztp7aff/4Zhw8fxlNPPYXDhw9j+/bt+OabbzB58mSrfjk5OSgsLEReXh727NmDxsZGJCcno7W1VeyTkZGBsrIyFBcXo7i4GGVlZcjMzBTbW1tbMXHiRDQ1NWHPnj3Iy8tDQUEB5s2b13dPnoiIiFyLoBAAhMLCwm77lJSUCACEH3/8URAEQbhw4YLg5eUl5OXliX0qKysFrVYrFBcXC4IgCMePHxcACPv37xf77Nu3TwAgfP3114IgCMKHH34oaLVaobKyUuzzzjvvCDqdTjCbzXY/B7PZLAC4pt8hIiIiedl7/napOU1msxkajQbXXXcdAKC0tBQtLS1ISkoS+xiNRsTExGDv3r0AgH379kGv12PUqFFinzvuuAN6vd6qT0xMDIxGo9hn/PjxsFgsKC0t7TIei8WC+vp6qxsRERG5J5dJmi5duoRFixYhIyMDAQEBAICqqip4e3uLuyy3Cw0NRVVVldgnJCSk0/2FhIRY9QkNDbVqHzBgALy9vcU+tixfvlycJ6XX6xEZGenQcyQiIiLlcomkqaWlBffddx/a2trw97//vcf+giBAo9GIP3f8tyN9rrZ48WKYzWbxVl5e3mNsRERE5JoUnzS1tLRgypQpOH36NHbu3CmOMgGAwWBAc3Mz6urqrH6nurpaHDkyGAw4d+5cp/utqamx6nP1iFJdXR1aWlo6jUB1pNPpEBAQYHUjIiIi96TopKk9Yfr222/xySefICgoyKo9Pj4eXl5e2Llzp3jMZDLh2LFjGD16NAAgMTERZrMZJSUlYp8DBw7AbDZb9Tl27BhMJpPYZ8eOHdDpdIiPj+/Lp0hEREQuwlPOB29sbMSpU6fEn0+fPo2ysjIEBgbCaDQiPT0dhw8fxgcffIDW1lZxNCgwMBDe3t7Q6/WYMWMG5s2bh6CgIAQGBmL+/PkYPnw4xo4dCwAYNmwYJkyYgKysLOTm5gIAZs6cieTkZERFRQEAkpKSEB0djczMTLzwwguora3F/PnzkZWVxdEjIiIiusIZS/m68umnnwoAOt2mTZsmnD592mYbAOHTTz8V7+PixYvCY489JgQGBgq+vr5CcnKycObMGavHOX/+vPDAAw8I/v7+gr+/v/DAAw8IdXV1Vn1+/PFHYeLEiYKvr68QGBgoPPbYY8KlS5eu6fmw5AAREZHrsff8rREEQZAlW3ND9fX10Ov1MJvNHKEiIiJyEfaevxU9p4mIiIhIKZg0EREREdmBSRMRERGRHZg0EREREdmBSRMRERGRHZg0EREREdmBSRMRERGRHZg0EREREdmBSRMRERGRHZg0EREREdmBSRMRERGRHZg0EREREdmBSRMRERGRHZg0ERERUa+UlJQgKysLJSUlcofiFEyaiIiI6JpZLBasX78eNTU1yM3NhcVikTukPsekiYiIiK5Zfn4+6urqAAC1tbUoKCiQOaK+x6SJiIiIronJZML27dshCAIAQBAEFBQUwGQyyRxZ32LSRERERHYTBAEbNmwQE6aejrsTJk1ERERkt4qKChw5cgRtbW1Wx9va2nDkyBFUVFTIFFnfY9JEREREdouIiEBcXBy0WusUQqvVIi4uDhERETJF1veYNBEREZHdNBoNZs6cCY1GY9dxd8KkiYiIiK5JWFgYUlNTxQRJo9EgLS0NYWFhMkfWt5g0ERER0TVLT0/HgAEDAACBgYFIS0uTOaK+x6SJiIiIrplOp8Ps2bMRHByMWbNmQafTyR1Sn/OUOwAiIiJyTQkJCUhISJA7DKfhSBMRERGRHZg0EREREdmBSRMRERGRHZg0ERERUa+UlJQgKysLJSUlcofiFEyaiIiI6JpZLBasX78eNTU1yM3NhcVikTukPsekiYiIiK5Zfn4+6urqAAC1tbUoKCiQOaK+x6SJiIiIronJZML27dshCAIAQBAEFBQUwGQyyRxZ32LSRERERHYTBAEbNmwQE6aejrsTJk1ERERkt4qKChw5cgRtbW1Wx9va2nDkyBFUVFTIFFnfY9JEREREdouIiEBcXBy0WusUQqvVIi4uDhERETJF1veYNBEREZHdNBoNZs6cCY1GY9dxd8KkiYiIiK5JWFgYUlNTxQRJo9EgLS0NYWFhMkfWt5g0ERGRS1FbQUWlSk9Px4ABAwAAgYGBSEtLkzmivsekiYiIXIYaCyoqlU6nw+zZsxEcHIxZs2ZBp9PJHVKfkzVp+uyzzzBp0iQYjUZoNBoUFRVZtQuCgKVLl8JoNMLX1xd33XUXvvrqK6s+FosF2dnZGDhwIPz8/DB58uROM/fr6uqQmZkJvV4PvV6PzMxMXLhwwarPmTNnMGnSJPj5+WHgwIGYM2cOmpub++JpExFRL6mxoKKSJSQkYOPGjUhISJA7FKeQNWlqampCbGws1q5da7N9xYoVWLlyJdauXYuDBw/CYDBg3LhxaGhoEPvk5OSgsLAQeXl52LNnDxobG5GcnIzW1laxT0ZGBsrKylBcXIzi4mKUlZUhMzNTbG9tbcXEiRPR1NSEPXv2IC8vDwUFBZg3b17fPXkiIromai2oSMqhERRShUqj0aCwsBApKSkArrwZjEYjcnJysHDhQgBXRpVCQ0Px/PPPY9asWTCbzQgODsbmzZsxdepUAMDZs2cRGRmJDz/8EOPHj8eJEycQHR2N/fv3Y9SoUQCA/fv3IzExEV9//TWioqLw0UcfITk5GeXl5TAajQCAvLw8TJ8+HdXV1QgICLDrOdTX10Ov18NsNtv9O0RE1DNBEPDMM8/g6NGjVvWBtFotYmNjsWTJErdetUV9y97zt2LnNJ0+fRpVVVVISkoSj+l0Otx5553Yu3cvAKC0tBQtLS1WfYxGI2JiYsQ++/btg16vFxMmALjjjjug1+ut+sTExIgJEwCMHz8eFosFpaWlXcZosVhQX19vdSMiIumpuaAiKYdik6aqqioAQGhoqNXx0NBQsa2qqgre3t7i7P2u+oSEhHS6/5CQEKs+Vz/OgAED4O3tLfaxZfny5eI8Kb1ej8jIyGt8lkREZA81F1Qk5VBs0tTu6uFWQRB6HIK9uo+t/r3pc7XFixfDbDaLt/Ly8m7jIiKi3lFzQUVSDsUmTQaDAQA6jfRUV1eLo0IGgwHNzc3iSoqu+pw7d67T/dfU1Fj1ufpx6urq0NLS0mkEqiOdToeAgACrGxER9Q21FlRUMrXVzFJs0jR48GAYDAbs3LlTPNbc3Izdu3dj9OjRAID4+Hh4eXlZ9TGZTDh27JjYJzExEWaz2eoFPXDgAMxms1WfY8eOWa3A2LFjB3Q6HeLj4/v0eRIRkf3S09Ph5+cHAOjfv78qCioqlRprZnnK+eCNjY04deqU+PPp06dRVlaGwMBADBo0CDk5OVi2bBmGDh2KoUOHYtmyZejXrx8yMjIAAHq9HjNmzMC8efMQFBSEwMBAzJ8/H8OHD8fYsWMBAMOGDcOECROQlZWF3NxcAMDMmTORnJyMqKgoAEBSUhKio6ORmZmJF154AbW1tZg/fz6ysrI4ekREpDC8FKcMtmpmtZ+f3ZWsI02HDh1CXFwc4uLiAABz585FXFwclixZAgBYsGABcnJy8Mgjj2DkyJGorKzEjh074O/vL97HqlWrkJKSgilTpmDMmDHo168f3n//fXh4eIh9tmzZguHDhyMpKQlJSUkYMWIENm/eLLZ7eHjgn//8J3x8fDBmzBhMmTIFKSkpePHFF530P0FERPbIz89HY2MjgCtfvFncUh5qrZmlmDpN7oB1moiI+o7JZMJjjz1mVbzYw8MDa9eu5bwmJ3LHmlkuX6eJiIionSAI2LBhA67+nt/Vceo7aq6ZxaSJiIgUT80naqVRc80sJk1ERKR4aj5RK42aa2YxaSIiIsVT84laidRaM4tJExERuQS1nqiVKj09XdzGLDAwUBU1s5g0ERHZQW2Vj5UqPT0d/fv3B8DilnLT6XSYPXs2goODMWvWLOh0OrlD6nOyFrckInIF7ZWPa2trkZubi9jYWFWcIJSKK+WUIyEhAQkJCXKH4TQcaSIi6oGtysckj/z8fDQ1NQFgcUtyPiZNRETdUGvlYyXia0FyY9JERNQFFlRUDr4WpARMmoiIusCCisrB14KUgEkTEVEXWFBROfhakBIwaSIi6gILKioHXwtSAiZNRETdYEFF5eBrQXJj0kRE1AM1Vj5WKha3JDkxaSIi6oEaKx8rGVfKkVxYEZyIyA5qq3ysVLaKW2ZkZMgcFakFR5qIiMglsLglyY1JExERKR6LW5ISMGkiIiLFY3FLUgImTUREpHgsbklKwKSJiIgUj8UtSQmYNBERkUsICwvD5MmTrY799re/ZXFLchomTURE5DJsjTQROQuTJiIicgkmkwnvvvuu1bGioiKWHCCnYdJERESKx5IDpARMmoiISPFYcoCUgEkTEREpXkREBKKjo222RUdHs+QAOQWTJiIiIiI7MGkiIiLFq6iowPHjx222HT9+nJfnyCmYNBERkeK1VwS3VXKAFcHJWZg0ERGR4rEiOCkBkyYiInIJYWFhiIqKsjp28803syI4OQ2TJiIicgkmkwnffPON1bGTJ0+yuCU5DZMmIiJSPBa3JCVg0kRERIrH4pakBEyaiIhI8dpXz2m11qctrVbL1XPkNEyaiIhI8bh6jpSASRMREbmEsLAwpKamigmSRqNBWloaV8/JqKSkBFlZWSgpKZE7FKdQdNJ0+fJl/PnPf8bgwYPh6+uLX/ziF3jmmWesrmkLgoClS5fCaDTC19cXd911F7766iur+7FYLMjOzsbAgQPh5+eHyZMnd7r+XVdXh8zMTOj1euj1emRmZuLChQvOeJpERGSn9PR0DBgwAAAQGBiItLQ0mSNSL4vFgvXr16Ompga5ubmwWCxyh9TnFJ00Pf/881i/fj3Wrl2LEydOYMWKFXjhhRewZs0asc+KFSuwcuVKrF27FgcPHoTBYMC4cePQ0NAg9snJyUFhYSHy8vKwZ88eNDY2Ijk5Ga2trWKfjIwMlJWVobi4GMXFxSgrK0NmZqZTny8REXVPp9Nh9uzZCA4OxqxZs6DT6eQOSbXy8/NRW1sLADh//jwKCgpkjqjvaQQFr9NMTk5GaGgoXnvtNfFYWloa+vXrh82bN0MQBBiNRuTk5GDhwoUArmS+oaGheP755zFr1iyYzWYEBwdj8+bNmDp1KgDg7NmziIyMxIcffojx48fjxIkTiI6Oxv79+zFq1CgAwP79+5GYmIivv/66UzG1rtTX10Ov18NsNiMgIEDi/w0iIiJlMJlMePTRR62u/Gi1Wvztb39zycul9p6/FT3S9Mtf/hL/+te/xGJmR48exZ49e/Df//3fAIDTp0+jqqoKSUlJ4u/odDrceeed2Lt3LwCgtLQULS0tVn2MRiNiYmLEPvv27YNerxcTJgC44447oNfrxT62WCwW1NfXW92IiIjcWXttLFvlH9y9Zpaik6aFCxfi/vvvx8033wwvLy/ExcUhJycH999/PwCgqqoKABAaGmr1e6GhoWJbVVUVvL29xWvgXfUJCQnp9PghISFiH1uWL18uzoHS6/WIjIzs/ZMluoraJlgSkWtor5lli7vXzFJ00rR161a89dZbePvtt3H48GFs2rQJL774IjZt2mTV7+qlpoIg9Lj89Oo+tvr3dD+LFy+G2WwWb+Xl5fY8LaIeqXGCJRG5hvDwcPj7+9ts8/f3R3h4uJMjch5FJ01PPPEEFi1ahPvuuw/Dhw9HZmYmHn/8cSxfvhwAYDAYAKDTaFB1dbU4+mQwGNDc3Iy6urpu+5w7d67T49fU1HQaxepIp9MhICDA6kYkhfz8fPFvtra2VhUTLInINVRWVlottuqooaEBlZWVTo7IeRSdNP3888+dqr96eHiI11EHDx4Mg8GAnTt3iu3Nzc3YvXs3Ro8eDQCIj4+Hl5eXVR+TyYRjx46JfRITE2E2m60ugxw4cABms1nsQ+QsJpMJ27dvF+cFCIKAgoICbkpKRIrQXp3dVqFRd6/OruikadKkSXjuuefwz3/+Ez/88AMKCwuxcuVK3HvvvQCuvEA5OTlYtmwZCgsLcezYMUyfPh39+vVDRkYGAECv12PGjBmYN28e/vWvf+HIkSN48MEHMXz4cIwdOxYAMGzYMEyYMAFZWVnYv38/9u/fj6ysLCQnJ9u9co5ICtyUlIiUrr0Ku60tbdy9Orun3AF0Z82aNXjqqafwyCOPoLq6GkajEbNmzcKSJUvEPgsWLMDFixfxyCOPoK6uDqNGjcKOHTusrreuWrUKnp6emDJlCi5evIi7774bb7zxBjw8PMQ+W7ZswZw5c8RVdpMnT8batWud92SJ0PUEy46bknLBARHJrb06+z/+8Q/xmBqqsyu6TpOrYZ0mcpQgCHjmmWdQVlZmNaqk0Whw6623YsmSJW79LY6IXIfFYsGMGTPQ2NgIf39/vPrqqy5bbNQt6jQRqY1Go0FKSorNy3P33nsvEyYiUhS1fSYxaSJSEEEQUFRUZLOtsLCQc5qISDHy8/PR2NgIAGhsbFTFKl8mTUQKouaicUTkOtS6ypdJE5GCtC/ltbUqxd2X8hKRa1DzKl8mTUQK0r6U11b9E3dfyktkL24xJK/2EXFbe8+5+4i4Q0lTc3MzKioqcObMGasbEfVe+1Le9gRJo9GoYikvkT24xZD81Dwi3quk6dtvv8WvfvUr+Pr64vrrr8fgwYMxePBg3HDDDRg8eLDUMRKpTnp6urjJdGBgINLS0mSOiEgZuMWQ/NQ8It6rpGn69OnQarX44IMPUFpaisOHD+Pw4cM4cuQIDh8+LHWMRKqj0+kwe/ZsBAcHY9asWS5b+4RISmqdfKxE7SPiHalhRLxXxS39/PxQWlqKm2++uS9iclksbklE1DdY+FV56uvrMW3aNAiCAK1WizfeeMNlz319WtwyOjoaP/30U6+DIyIiuhbtk49trdhy98nHSvX++++Lr0dbWxs++OADmSPqe3YnTfX19eLt+eefx4IFC7Br1y6cP3/eqq2+vr4v4yUiIhWKiIhAdHS0zbbo6Gi3nnysRO2XSjtSw6VSuzfsve6666yGPgVBwN13323VRxAEaDQatLa2ShchERERKUZ7PSZbJQc2bNjg1pdK7U6aPv30076Mg4iIqEsVFRU4fvy4zbbjx4+joqICkZGRTo5KnbrauaDjpVJ3fS3sTpruvPNO8d9nzpxBZGRkp0xSEASUl5dLFx0RERH+rzbQ0aNHrUY4tFotYmNjeXnOicLDw+Hv74+GhoZObf7+/ggPD5chKufo1UTwwYMHo6amptPx2tpa1mkiIiLJqbk2kNJUVlbaTJgAoKGhAZWVlU6OyHl6lTS1z126WmNjI3x8fBwOioiI6Gqslq8M7aN+trh7RXC7L88BwNy5cwFc+UN96qmn0K9fP7GttbUVBw4cwK233ippgERERO3S09Pxr3/9C7W1tayWLxONRoOUlBSb85pSUlLcetTvmpKm9v8gQRDw5ZdfwtvbW2zz9vZGbGws5s+fL22ERERE/6u9Wv7GjRuRlZXFavkyEAQBRUVF0Gg0nQqNFhUVYcSIEW6bOF1T0tS+gu7hhx/Gyy+/7LKVP4mIiKh31Lx6rldzml5//XUmTERE5HQWiwWvvPIKampqsGbNGlgsFrlDUp32OU1arXUKodVqOafJlqs36Wun0Wjg4+ODIUOGICMjA1FRUQ4FR0RE1FFeXh4aGxsBXFmptXXrVjz00EMyR6Uu7SsWH3vsMZvH3fXSHNDLkaaAgAD8+9//xuHDh8X/nCNHjuDf//43Ll++jK1btyI2Nhaff/65pMESEZF6mUwmFBUVWR0rLCx0+607lEitKxl7lTQZDAZkZGTg+++/R0FBAbZv347vvvsODz74IG688UacOHEC06ZNw8KFC6WOl4iIVEgQBKxZs8bmhr22jlPfS09Px4ABAwBANSsZe5U0vfbaa8jJybG6nqnVapGdnY0NGzZAo9Hgsccew7FjxyQLlIiI1Ku8vLzbbVS4G4Xzta9kDA4OxqxZs1SxkrFXc5ouX76Mr7/+GjfddJPV8a+//lrcrNfHx8etr2sSERGpXUJCAhISEuQOw2l6NdKUmZmJGTNmYNWqVdizZw8+//xzrFq1CjNmzBAn5O3evRu33HKLpMFS3yspKUFWVhZKSkrkDoWISBQZGYkhQ4bYbBsyZIjbLnFXOrWdM3o10rRq1SqEhoZixYoVOHfuHAAgNDQUjz/+uDiPKSkpCRMmTJAuUupzFosF69evR21tLXJzcxEbG6uK4VYicg0dCyrbc5z6lhrPGb0aafLw8MCTTz4Jk8mECxcu4MKFCzCZTPjTn/4EDw8PAMCgQYPculaDO8rPz0ddXR2AK5svFxQUyBwREdEVFRUV3c5pqqiocHJEpMZzRq+Spo4CAgJY6NINmEwmbN++XVyBIggCCgoKuJSXiBRBzQUVlUit54xeJU3nzp1DZmYmjEYjPD094eHhYXUj1yIIAjZs2GBzKa+t40REztZeONHW55S7F1RUGjWfM3o1p2n69Ok4c+YMnnrqKYSFhfGP1cV1tY9QW1ub2+8jRESuxdaJmpxLzeeMXiVNe/bswX/+8x/ceuutEodDcmgf9j569Cja2trE41qtFrGxsRz2JsKVVUIbN25EVlaWqpZYK0V7EUtb1qxZg+eee45f4J2k/ZxhK3Fy90ulvbo8FxkZyezejXS1X5Aa9hEiskf7KqGamhrk5uZyk1gZsLilcmg0GqSkpNhsS0lJcetzRq+SptWrV2PRokX44YcfJA6H5KLWfYSI7KHGVUJEXREEAUVFRTa/aBcVFbn1oEqvkqapU6di165duPHGG+Hv74/AwECrG7kmNe4jRNQTta4SUpqIiAj4+fnZbPPz83PrS0JK0z6nydb8svY5Te6qV3OaVq9eLXEYpATt+wi1z9tw9yJlRD3paZXQkiVL3PpShJJUVlaiqanJZltTUxMqKyvddvKx0rTPaSorK7N6b2g0Gtx6661uncD2KmmaNm2a1HGQQqhtHyGi7qh5lZDSqHnysdK0z2m6+rUQBAH33nuvW3+R6HVxy++++w5//vOfcf/996O6uhoAUFxcjK+++kqy4IiI5MSCisrRvjDF1mvBBSvOJQgCtm7darMtLy+Pc5qutnv3bgwfPhwHDhzA9u3b0djYCAD44osv8Je//EXSAImI5MKVpcoSFhbWaa5leno6F6w4mZpXMvYqaVq0aBGeffZZ7Ny502qjxN/85jfYt2+fZMEBV65jP/jggwgKCkK/fv1w6623orS0VGwXBAFLly6F0WiEr68v7rrrrk6jXRaLBdnZ2Rg4cCD8/PwwefLkThPV6urqkJmZCb1eD71ej8zMTFy4cEHS50JEricsLAw33XST1bGoqCieqGWSnp6O/v37AwD8/f25YIWcqldJ05dffol777230/Hg4GCcP3/e4aDa1dXVYcyYMfDy8sJHH32E48eP46WXXsJ1110n9lmxYgVWrlyJtWvX4uDBgzAYDBg3bhwaGhrEPjk5OSgsLEReXh727NmDxsZGJCcno7W1VeyTkZGBsrIyFBcXo7i4GGVlZcjMzJTsuRCRazKZTPj666+tjp04cYKr52TU/tl9+fJlmSNRJzWvZOxV0nTdddfZ/MA4cuQIwsPDHQ6q3fPPP4/IyEi8/vrrSEhIwA033IC7774bN954I4Aro0yrV6/Gk08+idTUVMTExGDTpk34+eef8fbbbwMAzGYzXnvtNbz00ksYO3Ys4uLi8NZbb+HLL7/EJ598AuDKB2BxcTFeffVVJCYmIjExERs3bsQHH3yAkydPSvZ8iMi1qHmPLaXaunUrLl68CAC4ePEitm3bJnNE6mPPSkZ31aukKSMjAwsXLkRVVRU0Gg3a2trw+eefY/78+XjooYckC+69997DyJEj8f/+3/9DSEgI4uLisHHjRrH99OnTqKqqQlJSknhMp9PhzjvvxN69ewEApaWlaGlpsepjNBoRExMj9tm3bx/0ej1GjRol9rnjjjug1+vFPrZYLBbU19db3YjIfXS1eg6A29ejUSKTyYTCwkKrY9u3b+eon5O1L5Cwxd0XSPQqaXruuecwaNAghIeHo7GxEdHR0fjVr36F0aNH489//rNkwX3//fdYt24dhg4dio8//hizZ8/GnDlz8OabbwIAqqqqAAChoaFWvxcaGiq2VVVVwdvbWyza2FWfkJCQTo8fEhIi9rFl+fLl4hwovV7PpcckqS1btiA1NRVbtmyROxTVCg8Ph7+/v802f39/SUfWqXvte8/ZGvWzdZz6jppXMvYqafLy8sKWLVvw7bffYtu2bXjrrbdw8uRJbN68GR4eHpIF19bWhttuuw3Lli1DXFwcZs2ahaysLKxbt86q39UvkCAIPb5oV/ex1b+n+1m8eDHMZrN4c+cVA+Rc9fX1yM/PR1tbG/Lz8zmKKZPKykqr+ZEdNTQ0uPVlCKVR84otJQoLC0NUVJTVsZtvvtntF0jYXdxy7ty53bbv379f/PfKlSt7H1EHYWFhiI6Otjo2bNgwcd8ng8EA4MpIUccXqrq6Whx9MhgMaG5uRl1dndVoU3V1NUaPHi32OXfuXKfHr6mp6TSK1ZFOp2PVbOoTy5cvt9q2469//SuWLVsmc1Tqo+bKx0TdMZlMneb8fv311zCZTG6dONk90nTkyBG7bmVlZZIFN2bMmE4vyjfffIPrr78eADB48GAYDAbs3LlTbG9ubsbu3bvFhCg+Ph5eXl5WfUwmE44dOyb2SUxMhNlsRklJidjnwIEDMJvNYh8iZzl69ChOnDhhdez48eM4evSoTBGpl5ovQyhNZGQkhgwZYrNtyJAhnB7hRO0LIWxx9wUSdo80ffrpp30Zh02PP/44Ro8ejWXLlmHKlCkoKSnBhg0bxBdLo9EgJycHy5Ytw9ChQzF06FAsW7YM/fr1Q0ZGBgBAr9djxowZmDdvHoKCghAYGIj58+dj+PDhGDt2LIAro1cTJkxAVlYWcnNzAQAzZ85EcnJyp+FHor7U1taGF1980Wbbiy++iE2bNnU6gVPfCgsLQ2pqKv7xj3+Ix9LS0tz627RSdawLaM9x6htq3l5I0Z++t99+OwoLC/HOO+8gJiYG//M//4PVq1fjgQceEPssWLAAOTk5eOSRRzBy5EhUVlZix44dVpM3V61ahZSUFEyZMgVjxoxBv3798P7771vNv9qyZQuGDx+OpKQkJCUlYcSIEdi8ebNTny9RaWlpt3NoOhZ2JedJT09HYGAgACAoKIgFFWVQUVHR7ZwmrmR0HjWvntMI7jyO5mT19fXQ6/Uwm80ICAiQO5xeKSkpwcaNG5GVlcWNe2XQ1taGadOm2Uyc/P39OdIkI7435MX3hrIcPXrU5rZpTz/9NGJjY2WIyDH2nr/5F0Yii8WC9evXo6amBrm5ubBYLHKHpDparRbz58+32fbEE0/wpCCjhIQEbNy4kQmTTLiSUTkEQUBRUZHNtqKiIree08RPYBLl5+ejrq4OAFBbWyuuUiTnio2NxbBhw6yORUdHY8SIETJFRCQ/o9HYZUkbDw8PGI1GJ0ekXmou+sqkiQBcWVG4fft2q2XuBQUFrLQrk8WLF4srs7RaLRYtWiRzRFRSUoKsrCyrVbbkPIcPH7baL7Sj1tZWHD582MkRqZeai74yaSLur6VAAQEBSE9Ph1arRVpamsvOkXMXFosFr7zyCmpqarBmzRpeupZBfHx8tyfq+Ph4J0ekXmq+VMqkicSh1ra2NqvjHZePkvM98MAD2L59u9VqUZJHXl4eGhsbAVw5KWzdulXmiNRHq9Xi4Ycfttn2u9/9jvP9nEjNq+f4V0biG8BWAT93fwMoGS8HKQM3iVUGQRDwn//8x2bbZ599xhFxJ2ov+mqLuxd9ZdJE4hvg6j/0ro5T3+NKRmVo3wzWFm4S61xqnnxMysGkiQBcqXp80003WR2Liopi1WOZcCWjMnCTWOWIiIjotBdpu+joaI6IO5EgCHjppZdstr300ktu/WWCSRMB6H7zRXIurmQksq2rEVeOxDrXmTNncOrUKZttp06dwpkzZ5wckfMwaSJVb76oNFzJSGRbeXk5vvvuO5tt3333HUf9nOjcuXMOtbsyJk3E1XMKwtdCWSIjI7u9JOSum5Iq0dXviWttJ+mMHDkSfn5+Ntv8/PwwcuRIJ0fkPEyaiKvnFISvhbJoNBpkZ2fbXCRh6zj1nerqaofaSTparRYLFiyw2bZw4UK3Lv/gvs+M7Kbm5aNKw5WMyhMWFoaUlBSrY/feey8XSTiZmkc3lCg2NhZRUVFWx26++Wa33+6JSRMBuHJisPUG4InB+cLCwpCamiomSBqNBmlpaXwtZHTfffehf//+AK5Un546darMEamPmkc3lOrJJ5+0+pz605/+JHNEfY9/ZQTgyoqtb775xurYyZMnuWJLJunp6RgwYAAAIDAwEGlpaTJHpG46nQ5z5sxBcHAwsrOzodPp5A5JldQ6uqFUHbd7Sk9PV8V2TxqBy3EkU19fD71eD7PZ7FJ/PIIg4JlnnsHRo0etJlNqtVrExsZiyZIlvCwkg5KSEmzcuBFZWVlISEiQOxwiRaivr8e0adMgCAI0Gg02bdrkUp+3pEz2nr89nRgTKVRXlXY7rtjiKiHnS0hIYLJEdJWAgACEh4ejoqIC4eHhTJjIqXh5jrhiS6G49xxRZzU1NWLpjYqKCtTU1Mgckbqp7XOKSRNxxZYCce85ItsWLVpk9fPixYtlioQsFgteeeUV1NTUYM2aNar4nGLSRAC4Yktp8vPzUVtbCwA4f/48954jAvDvf/8b58+ftzr2008/4d///rdMEalbXl4eGhsbAQANDQ3YunWrzBH1PSZNJOKKLWUwmUydkqT8/HyuZCRVa21txd/+9jebbX/729/Q2trq5IjUzWQyoaioyOpYYWGh239OMWkikU6nw+zZsxEcHIxZs2ZxWbUM2veYs7WNCveeIzXbsWNHl4lRa2srduzY4eSI1EsQBKxZs8bmHpm2jrsTJk1kJSEhARs3buSqLZl0tZIRAPeeI1UbN26cQ+0knfLychw/ftxm2/Hjx91682QmTUQKEh4eDl9fX5ttvr6+CA8Pd3JE1G7Lli1ITU3Fli1b5A5Flc6ePetQO5EUmDQRKUhFRQUuXrxos+3ixYscaZJJfX098vPz0dbWhvz8fNTX18sdkur0dMnHnS8JKU1kZCSio6NttkVHR7t1XT8mTUQK0tMkSnefZKlUy5cvF0/KgiDgr3/9q8wRqU9PpU9YGsV5NBoNsrOzbbZlZ2e79WvBpIlIQXoq8cASEM539OhRnDhxwurY8ePHcfToUZkiUic1j26QcjBpIitqq+6qNJGRkbjxxhtttg0ZMoQnBidra2vDiy++aLPtxRdf7LTKkfqORqPB1KlTbbbdd999bj26oTTtq+Rs4eo5Ug2LxYI1a9aoqrqr0mg0GkycONFm28SJE3licLLS0lI0NDTYbGtoaEBpaamTI1IvQRCwefNmm21vvvmmW5+olYar54gAbN26VTxBNDQ0YNu2bTJHpD5tbW147bXXbLa9+uqrHNlwsttuuw0eHh422zw8PHDbbbc5OSL1OnPmDE6dOmWz7dSpUzhz5oyTIyI1YtJEAK5MMC4sLLQ6tn37dk48drJDhw6hqanJZltTUxMOHTrk5IjU7ezZs90WVOQyd+c5d+6cQ+0knZ6+vLnzlzsmTaTq6q5KExoa6lA7SSs8PBz+/v422/z9/Vk3y4lCQkIcaifpVFdXO9Tuypg0kaqvTysNl1UrS2VlZbdzmiorK50ckXpptd2frnpqJ+n0dFnanS9b86+MWDROQbisWlkiIiIQFxdnsy0uLg4RERFOjki9+DmlHD0tgHDnBRJMmghVVVUOtZN01Fw0Tok0Gg1mzpxps23mzJl8PZyIo7CkBEyaiPNoFCYsLAyTJ0+2Ovbb3/6WhS1l0tX8DHeet6FEkZGRGDJkiM021jBzrttvvx3e3t4227y9vXH77bc7OSLnYdJEqp7Up1RXL3Pvatk79S0Wt1SWri7B8dKc83X1t+/u7wkmTYSRI0fCz8/PZpufnx9Gjhzp5IjUzWQy4b333rM69u6777L8gwxY3FI5ysvL8d1339ls++6777hgxYkOHDiAy5cv22y7fPkyDhw44OSInIdJE0Gr1WLBggU22xYuXMhVKU4kCAI2bNhgs/yDrePUt+Lj47stORAfH+/kiNSLE8GVo6vk1d52V+ZSZ8Ply5dDo9EgJydHPCYIApYuXQqj0QhfX1/cdddd+Oqrr6x+z2KxIDs7GwMHDoSfnx8mT56MiooKqz51dXXIzMyEXq+HXq9HZmYmLly44IRnpQyxsbEIDAy0OhYYGIgRI0bIFJE6VVRU4MiRI52GuNva2nDkyJFOf7fUt7RaLebPn2+z7YknnuAXClKl++67z6F2V+Yy7/iDBw9iw4YNnU7iK1aswMqVK7F27VocPHgQBoMB48aNsxpSz8nJQWFhIfLy8rBnzx40NjYiOTnZqtJvRkYGysrKUFxcjOLiYpSVlSEzM9Npz09uJpMJtbW1Vsdqa2t5ScjJuMRdeboqmhgcHOzkSNSNq+eUQ82vhUskTY2NjXjggQewceNGDBgwQDwuCAJWr16NJ598EqmpqYiJicGmTZvw888/4+233wYAmM1mvPbaa3jppZcwduxYxMXF4a233sKXX36JTz75BABw4sQJFBcX49VXX0ViYiISExOxceNGfPDBBzh58qQsz9mZ1LxjtdJoNBqkpKTYbEtJSXHrDyMl4ntDOcLDw7sc2dNqtazO7kQff/yxQ+2uzCWSpkcffRQTJ07E2LFjrY6fPn0aVVVVSEpKEo/pdDrceeed2Lt3L4ArEzlbWlqs+hiNRsTExIh99u3bB71ej1GjRol97rjjDuj1erGPLRaLBfX19VY3V8SK4MohCAKKioo6JUcajQZFRUU8STsZ3xvKcfjw4W5XbB0+fNjJEalXVwV47W13ZYpPmvLy8lBaWorly5d3amsvunh1HaHQ0FCxraqqCt7e3lYjVLb62BqCDwkJ6baw4/Lly8U5UHq9nnVCyGHtc5psTQTnnCbnU/PGpEpz2223dTvS5M5bdyiNmre0UfQzKy8vxx//+Eds2bIFPj4+Xfa7+lu5IAg9Xsa4uo+t/j3dz+LFi2E2m8Ubv3WSo9rnNF39oaPVajmnSQbnzp1zqJ2kU1FR0e1IE79QOI/RaHSo3ZUpOmkqLS1FdXU14uPj4enpCU9PT+zevRuvvPIKPD09xRGmq0eDqqurxTaDwYDm5mbU1dV128fWh19NTU231bB1Oh0CAgKsbq6IlXaVo33bDlur57htB6kZt3tSjp07dzrU7soUnTTdfffd+PLLL1FWVibeRo4ciQceeABlZWX4xS9+AYPBYPUCNTc3Y/fu3Rg9ejSAK3VWvLy8rPqYTCYcO3ZM7JOYmAiz2YySkhKxz4EDB2A2m8U+7q67kvjkXNy2QzlGjhzZ7SUhFn51HoPB4FA7SWfcuHEOtbsyT7kD6I6/vz9iYmKsjvn5+SEoKEg8npOTg2XLlmHo0KEYOnQoli1bhn79+iEjIwMAoNfrMWPGDMybNw9BQUEIDAzE/PnzMXz4cHFi+bBhwzBhwgRkZWUhNzcXwJXNOJOTkxEVFeXEZyyPioqKbie7VlRUcLTJSXratmPTpk1uPV9Aac6ePdvtJaGzZ8/yveEkgwYNQlhYmM0yKEajEYMGDZIhKnU6e/Zsj+3u+nooOmmyx4IFC3Dx4kU88sgjqKurw6hRo7Bjxw6rKr6rVq2Cp6cnpkyZgosXL+Luu+/GG2+8YbWf15YtWzBnzhxxld3kyZOxdu1apz8fORiNRmi1WpsnB61W69bXp5XGnm073HkzTKUJDw+Hn58fmpqaOrX5+flxmbsTCYLQZcHhuro6u+aykjTUXJ3d5ZKmXbt2Wf2s0WiwdOlSLF26tMvf8fHxwZo1a7qstwJcqX791ltvSRSlayktLe3223RpaSkSEhKcHJU6ta8Q6iqB5Qoh56qoqLCZMAFAU1MTKioq3PYbtdIcOnQIFy9etNl28eJFHDp0iJ9TTsLilqRqXFatHJWVld0msJWVlU6OiEgZuqrMbm87SaelpcWhdlfGpIlUvXxUabhCSFkiIyO7LNQXHR3N+UxOxPIPyrFjxw6H2l0ZkyZCZGQkbrzxRpttLDngXCNHjoSvr6/NNl9fX67WcjKNRoOpU6fabJs6dapbX4ZQGo40KcfDDz/sULsrY9JE0Gg0eOihh2y2PfTQQzwxOJFGo+lyI9jg4GC+Fk7Wvq2NLdzWxrlOnDjhUDtJ59NPP3Wo3ZUxaaJuTwyFhYU8MThReXk5zpw5Y7PtzJkzrDrvZO3b2tjCbW2c6+abb3aonaSj5jpNTJqIJwYFaW1tdaidpBUREdHtnCZua+M8P/30k0PtJJ2eFqS484IVJk3E/c4U5KuvvnKonchddXXZ2t52ko6aP6eYNJG439nV82W6Ok59Z+DAgQ61k7TsqZZPzqHmE7XS3H333Q61uzImTQQACAsLw29/+1urYykpKQgLC5MpInXqaXUcV885Fy/PKUdQUJBD7SSdvLw8h9pdGZMmEl094ZsTwJ2vtLTUoXYid3X+/HmH2kk6jY2NDrW7MiZNBAAwmUx49913rY4VFRXZ3ByT+k5NTY1D7SQtXp5TDq6eU4577rnHoXZXxqSJIAgCNmzY0Gn7jra2NmzYsIEjTk40fPhwh9pJWuHh4d0WG+WGvc5TXFzsUDtJx9Oz+21re2p3ZUyaiCUHFGTQoEFdVjYODQ3l5rBOVl5e3u0msayb5Tw97UzAnQucp6cv0u78RZtJEyE8PBz+/v422/z9/flt2okEQUBTU5PNtsbGRrf+MFKini5P8/K189TW1jrUTtJh0kSqVllZiYaGBpttDQ0Nbl2oTGlKS0u7TJqampo4EZxU6+o6ctfaTtL58ssvHWp3ZfwrI440KUh8fDx8fHxstvn4+CA+Pt7JEalbTzXKWMOM1IgjTaRqHGlSDkEQcOnSJZttly5dcusPIyW67bbbHGon6Vy+fNmhdpKOmr9MMGkiREREdDnBeNCgQSzg50QffPCBQ+0krY8++sihdpJOVxtZ29tO0rnuuuscandlTJoIbW1tXa4CKi8v71SKgPrOiRMnHGonaf3www8OtZN07r//fofaSToff/yxQ+2ujEkTobi4uMvLPoIgsP6JEw0bNsyhdpJWV5Py7W0n6VxdfPda20k6XdUus7fdlTFpoh5HkjjS5DwjRoxwqJ2kNXfuXIfaSTpDhw51qJ2ko+YivEyaCDExMQ61k3Sqq6sdaidpVVVVOdRO0ulqsYq97SSd4OBgh9pdGZMm4n5nCqLmpbxKdO7cOYfaSTr19fUOtZN01Py+YNJEiI+P77IwnFarZW0gJzIYDA61k7T43lCO2NhYh9pJOj1tH+TO2wsxaSKcPXu2y3lLbW1tOHv2rJMjUi9u26EslZWV3b43WMPMefbu3etQO0mnp4LH7lwQmUkTwWg0dvtt2mg0Ojki9frpp58caidpMYlVjptuusmhdpJOT18W3PnLBJMmQmlpabffprnfmfOoudKuErW2tjrUTtLZs2ePQ+0kHTUvkGDSRAgJCXGonaQzbtw4h9pJWhcuXHConaTT084E3LnAeQYPHuxQuytj0kSq/tagNO+8845D7SStpKQkh9pJOqdOnXKonaTz3XffOdTuypg0ES8JKQgTWGXpaREEF0k4j5eXl0PtJJ26ujqH2l0ZkybCyJEju50IPnLkSCdHpF4+Pj4OtZO01DzhVWk4v0w51LxghUkTseSAgqh593AlUvNlCKW54YYbHGon6bAiOKlaeHh4lyMYPj4+bl1zQ2mioqIcaidppaenO9RO0lHz6IbSXLp0yaF2V8akiVBeXt7lH/mlS5fcurqr0nAbFWX5xz/+4VA7SYfz/ZRDzSPiTJoIX331lUPtJB01T7BUon79+jnUTtLR6/UOtZN0PD09HWp3ZUyaCOPHj3eonaQzduxYh9pJWmVlZQ61k3S8vb0daifpXL582aF2V8akiUhB8vLyHGonacXFxTnUTtL5/vvvHWon6ai5FAeTJsJHH33kUDtJR80fRkp05MgRh9pJOkOGDHGonaQzaNAgh9pdGZMm6rLcgL3tJB2dTudQO0mLl0uVo76+3qF2ks6ZM2ccandlik6ali9fjttvvx3+/v4ICQlBSkoKTp48adVHEAQsXboURqMRvr6+uOuuuzpNXLZYLMjOzsbAgQPh5+eHyZMno6KiwqpPXV0dMjMzodfrodfrkZmZqZp9pX788UeH2kk6zc3NDrWTtPbv3+9QO0mntrbWoXaSjpp3kVB00rR79248+uij2L9/P3bu3InLly8jKSkJTU1NYp8VK1Zg5cqVWLt2LQ4ePAiDwYBx48ahoaFB7JOTk4PCwkLk5eVhz549aGxsRHJyslUF2YyMDJSVlaG4uBjFxcUoKytDZmamU5+vXG677TaH2kk6vAShLImJiQ61k3S62rXA3naSjpongit6XWBxcbHVz6+//jpCQkJQWlqKX//61xAEAatXr8aTTz6J1NRUAMCmTZsQGhqKt99+G7NmzYLZbMZrr72GzZs3i0Ppb731FiIjI/HJJ59g/PjxOHHiBIqLi7F//36MGjUKALBx40YkJibi5MmTbl9QUM3fGpTm6NGjPbazoKLzsKCicqj5RK00Pj4+aGxs7LbdXblUam42mwEAgYGBAIDTp0+jqqrKaqdxnU6HO++8E3v37gUAlJaWoqWlxaqP0WhETEyM2Gffvn3Q6/ViwgQAd9xxB/R6vdjHFovFgvr6equbKzp//rxD7SSdAQMGONRO0iosLHSonaTDwq/KoeYv2ooeaepIEATMnTsXv/zlLxETEwPg/yrAhoaGWvUNDQ0V5+FUVVXB29u708kmNDRU/P2qqiqEhIR0esyQkJBuq8wuX74cTz/9dO+flELww0gagiDAYrE4dB/2XIJwdIsCnU7n1h9qUrrzzjvxwQcfdNtOzsGRJuXoOP2lN+2uzGWSpsceewxffPEF9uzZ06nt6hOAIAg9nhSu7mOrf0/3s3jxYsydO1f8ub6+HpGRkd0+rhKpuSS+lCwWC+67774+fYxdu3Zh165dDt1HXl6eWw+fS0nNlY+JqDOXeMdnZ2fjvffew2effYaIiAjxuMFgAHBlpCgsLEw8Xl1dLY4+GQwGNDc3o66uzmq0qbq6GqNHjxb7nDt3rtPj1tTUdBrF6kin08m6BFyKkQ0AeO+993psT0hIcOgxOLpBrogrS5VDr9eLUzS6aifqa4pOmgRBQHZ2NgoLC7Fr1y4MHjzYqn3w4MEwGAzYuXOnWJm3ubkZu3fvxvPPPw8AiI+Ph5eXF3bu3IkpU6YAAEwmE44dO4YVK1YAuLICxmw2o6SkREwODhw4ALPZLCZWSuSMkQ0AOHXqlMOPo4bRDZ1O53DF7suXL+PBBx/ssv2tt95yeHSDtZ7sV11d7VA7SYc1zEgJFJ00Pfroo3j77bfx7rvvwt/fX5xfpNfr4evrC41Gg5ycHCxbtgxDhw7F0KFDsWzZMvTr1w8ZGRli3xkzZmDevHkICgpCYGAg5s+fj+HDh4ur6YYNG4YJEyYgKysLubm5AICZM2ciOTnZ7VfOkXQ0Go0kieFDDz2EN998s9Px6dOno3///g7fvxpINQprzzwaR+aYcQTWfkxgSQkUnTStW7cOAHDXXXdZHX/99dcxffp0AMCCBQtw8eJFPPLII6irq8OoUaOwY8cO+Pv7i/1XrVoFT09PTJkyBRcvXsTdd9+NN954Ax4eHmKfLVu2YM6cOeIqu8mTJ2Pt2rV9+wQdJMXIBsDRDaVJTU3Ftm3brE7Gvr6+SElJkS8oF+OsUdhz58459DhqGIElcieKTprsWbWl0WiwdOlSLF26tMs+Pj4+WLNmDdasWdNln8DAQLz11lu9CVM2Uo1sABzdUJrnnnsO8+bNE39+4YUXZIyGqPekGvWzB1eWUl9TdNJEzpOamop33nkHLS0t4jFvb2+ObsgkPDxc/HdUVJTVAgjqmVSjsC0tLd3uDLB582Z4eXn1+v7VMALrrFE/AJx7SX2OSROJ/vrXv1qNbqxcuVLGaKidO9QCczapRmF9fHyQkpKCoqKiTm2pqalW0wCIyP0xaSIRRzeIOps+fTreffddq+kCGo0GDz30kIxRuQ6pRv0EQcD999/fZfs777zj8KU1NYz8kWOYNJFNHN0g+j/Lli3D4sWLxZ9feuklGaNxLVLOvVy3bh3+8Ic/2Dzu6+sryWMQdYdJExFRDzrWiAsPD8cvfvELGaNRr7CwMISGhloVIzYYDFbFjalrnJTvOCZNRETXgKNM8lqxYgWmTZsm/vzyyy/LGI1r4aR8x3W/OygREZGCdJx39MQTT3AeEjkVR5qIiMglxcfHyx2CS5FqUv758+fx6KOPdtn+t7/9DUFBQQ49hlKTYSZNREREKiDVpPzw8HB4e3ujubm5U5u3t7fVSmx3w8tzREREdE22bdt2TcfdBZMmIiIiumbjx4+3+nnixIkyReI8TJqIiIjomj388MNWP2dlZckUifMwaSIiIiKHSDHB3BUwaSIiIiKyA5MmIiIiIjuw5ACpljO3FLhWHbcgcHQ7gr6m1O0OiIikxqSJVMuZWwo4Yvr06XKH0C2lbndARCQ1Jk1OxtENaXB0g4iInI1Jk5NxdEMaUo9uNGRnQ/Dykuz+HCYIwOXLV/7t6QkoLEHUtLTAf80aye5PyV8mANf5QsEvE0R9i0kTEXAlYfL2ljsMawrdewkABInvz1W+TADK/kIhxZcJJrDSYRLrfpg0yejn2KcBrYJO1IIAtLVc+bfWS3GjG2hrRr+jf5E7CiK3xgRWOpzv536YNMlJ6w14KG00gW9wkteYV6bBQ6esjyZBENDWfOVyqdbbU1GjB62Wy/h8zia5w6A+wFE/6Ug16qesTyYiUj0PnSc8dAqaX9bOR0Gjwk7y+IIEeHl7yB2GFUEQ0NLSBgDw8tIqKoEFgJbmVqxaUSLJfXHUTzpSjfoxaSIiIpu8vD3grbCkCVD0dD9yc0yaiIiIFG5FvC90CtvDQxAENF8Z9IO3Foob9bO0AQtKL0p6n0yaSLUEocMasJYW+QJxRR3+v6z+H4moT+i0gM5DWUkJoFH4LFjpP5uYNJFqdZxgGSBhzSG1sVgs8PX1deg+OiZerRYmsNei4/8XE1iivsWkycmsPtRam+ULxBV1+P/iycG9dExgP5/zpoyRuDYpElgi6hqTJifreHLo9wVrDvWWFCcHXYfZpPXZ2YCSKoIrXUuLODqn46xct9LxC0lzc6uMkbimjv9n/HLnfpg0kWpZTVpUYkVwFyHF5M+OideYVx5SZskBhWq1tIijc1IksB2/2K2WaOm8Wjn65a5j0mVpZQJ2rTr+n0mVwDJpcrKOH2o/j3ga8OCJ2m6tzeLonNSjG5qWlj6YMugAF9h7TtL76/D8PHReTJp6SWmrl8gxHRPYBYeVXTxS6aS6dM2kycmsPtQ8lFgR3DVIfXKQcvNZIlfW8QtJzoIERdZpUrLm5lZxhI6Xrt0PkyY5tSlsIrgL7D1H7q/VclnuEDpR+jYqUur43LwVWtzSVTj6d9Ix6Vpxm48CSw4om6VVEEfopEpgmTTJiJvPykun0yEvL0/uMGy6dOmSuC3BG2+8oehNP6X+Ns191JSjRYETwV1hGxWpWD03hT1PQPnFLTv+n0kVG5MmUi2NRqPoZKSdj4+PS8RJ7keqPdTIcVJXtqbeYdLkZBzdkAbnCrgXJb8vANd5b/B9QdS3mDQ5GUc3iDpzlfcF4P7vDSaw0nE0ieVrIR3OaSIiIskxgVUOvhbKo7A9k4mIiIiUiSNNV/n73/+OF154ASaTCbfccgtWr16NX/3qV3KHZZMgCFbFzxx16dIlm/+Wgk6nU97KColJ+XrwtSB3wc8pcidMmjrYunUrcnJy8Pe//x1jxoxBbm4u7rnnHhw/fhyDBg2SO7xOLBYL7rvvvj657/br1FLJy8tz+6Hbvno9+FpcO1c5UavhJM3PKeVwlfcFoNz3BpOmDlauXIkZM2bg97//PQBg9erV+Pjjj7Fu3TosX75c5uiIyF6ucqJ295M0KYurvC8A5b43mDT9r+bmZpSWlmLRokVWx5OSkrB3716bv2OxWKyy9vr6+j6N8WpSr6zo+C1E6ixfDUuhpXw9+FqQu+DnFLkTJk3/66effkJraytCQ0OtjoeGhqKqqsrm7yxfvhxPP/20M8KzqS9WVkixoaFaSf168LXoPVc5UavhJM3PKeVwlfdF+/0pEZOmq1z9oguC0OUfwuLFizF37lzx5/r6ekRGRvZpfETUM56oiTrj+8JxTJr+18CBA+Hh4dFpVKm6urrT6FM7nU6n2GyYiIiIpMU6Tf/L29sb8fHx2Llzp9XxnTt3YvTo0TJFRURERErBkaYO5s6di8zMTIwcORKJiYnYsGEDzpw5g9mzZ8sdGhEREcmMSVMHU6dOxfnz5/HMM8/AZDIhJiYGH374Ia6//nq5QyMiIiKZaQRBEOQOwl3U19dDr9fDbDYjICBA7nCIiIjIDvaevzmniYiIiMgOTJqIiIiI7MCkiYiIiMgOTJqIiIiI7MCkiYiIiMgOTJqIiIiI7MCkiYiIiMgOTJqIiIiI7MCK4BJqrxNaX18vcyRERERkr/bzdk/1vpk0SaihoQEAEBkZKXMkREREdK0aGhqg1+u7bOc2KhJqa2vD2bNn4e/vD41GI3c4vVJfX4/IyEiUl5dzKxiZ8bVQFr4eysHXQjnc5bUQBAENDQ0wGo3QarueucSRJglptVpERETIHYYkAgICXPoN4E74WigLXw/l4GuhHO7wWnQ3wtSOE8GJiIiI7MCkiYiIiMgOTJrIik6nw1/+8hfodDq5Q1E9vhbKwtdDOfhaKIfaXgtOBCciIiKyA0eaiIiIiOzApImIiIjIDkyaiIiIiOzApIkAAJ999hkmTZoEo9EIjUaDoqIiuUNSreXLl+P222+Hv78/QkJCkJKSgpMnT8odliqtW7cOI0aMEGvQJCYm4qOPPpI7LMKV94lGo0FOTo7coajS0qVLodForG4Gg0HusPockyYCADQ1NSE2NhZr166VOxTV2717Nx599FHs378fO3fuxOXLl5GUlISmpia5Q1OdiIgI/PWvf8WhQ4dw6NAh/Nd//Rd++9vf4quvvpI7NFU7ePAgNmzYgBEjRsgdiqrdcsstMJlM4u3LL7+UO6Q+x4rgBAC45557cM8998gdBgEoLi62+vn1119HSEgISktL8etf/1qmqNRp0qRJVj8/99xzWLduHfbv349bbrlFpqjUrbGxEQ888AA2btyIZ599Vu5wVM3T01MVo0sdcaSJSOHMZjMAIDAwUOZI1K21tRV5eXloampCYmKi3OGo1qOPPoqJEydi7Nixcoeiet9++y2MRiMGDx6M++67D99//73cIfU5jjQRKZggCJg7dy5++ctfIiYmRu5wVOnLL79EYmIiLl26hP79+6OwsBDR0dFyh6VKeXl5KC0txaFDh+QORfVGjRqFN998EzfddBPOnTuHZ599FqNHj8ZXX32FoKAgucPrM0yaiBTssccewxdffIE9e/bIHYpqRUVFoaysDBcuXEBBQQGmTZuG3bt3M3FysvLycvzxj3/Ejh074OPjI3c4qtdxOsfw4cORmJiIG2+8EZs2bcLcuXNljKxvMWkiUqjs7Gy89957+OyzzxARESF3OKrl7e2NIUOGAABGjhyJgwcP4uWXX0Zubq7MkalLaWkpqqurER8fLx5rbW3FZ599hrVr18JiscDDw0PGCNXNz88Pw4cPx7fffit3KH2KSRORwgiCgOzsbBQWFmLXrl0YPHiw3CFRB4IgwGKxyB2G6tx9992dVmc9/PDDuPnmm7Fw4UImTDKzWCw4ceIEfvWrX8kdSp9i0kQArqxIOXXqlPjz6dOnUVZWhsDAQAwaNEjGyNTn0Ucfxdtvv413330X/v7+qKqqAgDo9Xr4+vrKHJ26/OlPf8I999yDyMhINDQ0IC8vD7t27eq0wpH6nr+/f6d5fX5+fggKCuJ8PxnMnz8fkyZNwqBBg1BdXY1nn30W9fX1mDZtmtyh9SkmTQQAOHToEH7zm9+IP7dfk542bRreeOMNmaJSp3Xr1gEA7rrrLqvjr7/+OqZPn+78gFTs3LlzyMzMhMlkgl6vx4gRI1BcXIxx48bJHRqRrCoqKnD//ffjp59+QnBwMO644w7s378f119/vdyh9SmNIAiC3EEQERERKR3rNBERERHZgUkTERERkR2YNBERERHZgUkTERERkR2YNBERERHZgUkTERERkR2YNBERERHZgUkTERERkR2YNBER2emHH36ARqNBWVmZ3KEQkQyYNBGR25k+fTo0Gg00Gg08PT0xaNAg/OEPf0BdXd013UdKSorVscjISJhMJu51RqRSTJqIyC1NmDABJpMJP/zwA1599VW8//77eOSRRxy6Tw8PDxgMBnh6cttOIjVi0kREbkmn08FgMCAiIgJJSUmYOnUqduzYAQBobW3FjBkzMHjwYPj6+iIqKgovv/yy+LtLly7Fpk2b8O6774ojVrt27ep0eW7Xrl3QaDT417/+hZEjR6Jfv34YPXo0Tp48aRXLs88+i5CQEPj7++P3v/89Fi1ahFtvvdVZ/xVEJBEmTUTk9r7//nsUFxfDy8sLANDW1oaIiAhs27YNx48fx5IlS/CnP/0J27ZtAwDMnz8fU6ZMEUerTCYTRo8e3eX9P/nkk3jppZdw6NAheHp64ne/+53YtmXLFjz33HN4/vnnUVpaikGDBmHdunV9+4SJqE9wjJmI3NIHH3yA/v37o7W1FZcuXQIArFy5EgDg5eWFp59+Wuw7ePBg7N27F9u2bcOUKVPQv39/+Pr6wmKxwGAw9PhYzz33HO68804AwKJFizBx4kRcunQJPj4+WLNmDWbMmIGHH34YALBkyRLs2LEDjY2NUj9lIupjHGkiIrf0m9/8BmVlZThw4ACys7Mxfvx4ZGdni+3r16/HyJEjERwcjP79+2Pjxo04c+ZMrx5rxIgR4r/DwsIAANXV1QCAkydPIiEhwar/1T8TkWtg0kREbsnPzw9DhgzBiBEj8Morr8BisYijS9u2bcPjjz+O3/3ud9ixYwfKysrw8MMPo7m5uVeP1X7ZDwA0Gg2AK5cArz7WThCEXj0OEcmLSRMRqcJf/vIXvPjiizh79iz+85//YPTo0XjkkUcQFxeHIUOG4LvvvrPq7+3tjdbWVocfNyoqCiUlJVbHDh065PD9EpHzMWkiIlW46667cMstt2DZsmUYMmQIDh06hI8//hjffPMNnnrqKRw8eNCq/w033IAvvvgCJ0+exE8//YSWlpZePW52djZee+01bNq0Cd9++y2effZZfPHFF51Gn4hI+Zg0EZFqzJ07Fxs3bkRKSgpSU1MxdepUjBo1CufPn+9UwykrKwtRUVHivKfPP/+8V4/5wAMPYPHixZg/fz5uu+02nD59GtOnT4ePj48UT4mInEgj8OI6EZFTjRs3DgaDAZs3b5Y7FCK6Biw5QETUh37++WesX78e48ePh4eHB9555x188skn2Llzp9yhEdE14kgTEVEfunjxIiZNmoTDhw/DYrEgKioKf/7zn5Gamip3aER0jZg0EREREdmBE8GJiIiI7MCkiYiIiMgOTJqIiIiI7MCkiYiIiMgOTJqIiIiI7MCkiYiIiMgOTJqIiIiI7MCkiYiIiMgOTJqIiIiI7PD/ARqcAioMhNYgAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x='Rating',y='length',data=df,palette='rainbow')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "98c1150d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Rating', ylabel='count'>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='Rating',data=df,palette='rainbow')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "42a55d7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "reviews=df.groupby('Rating').mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "50906b4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rating</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>769.534835</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>867.002789</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>784.664835</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>745.339957</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>661.696488</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            length\n",
       "Rating            \n",
       "1       769.534835\n",
       "2       867.002789\n",
       "3       784.664835\n",
       "4       745.339957\n",
       "5       661.696488"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reviews"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "f1a6eab7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>length</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        length\n",
       "length     1.0"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reviews.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c167b7f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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au3atf4xn3zySd1yyy2aO3eu7rrrLr399tvavn27f3dISz63xQwAANBuLFmyxBgwYIARERFhjBw50ti5c6f/vdzcXOPWW2/1v/7zn/9s3HTTTUZ0dLTRvXt346677jI+/fTToDH/4z/+wxg8eLARHh5uXH/99camTZtC+tyWajfnVAAAgI6NNRUAAMAWBBUAAMAWBBUAAMAWBBWATW677Tbl5+e39TS0Y8cOORwOnT59uq2nAuAKQ1ABdGDtJZABAImgAgAA2ISgAmgF9fX1+vWvf62rr75aXbp0UUpKinbs2OF/f82aNbrqqqu0detWJSYmqmvXrho3bpw8Ho+/z7lz5/TEE0/oqquuUu/evfX0008rNzdXEydOlCRNnTpVO3fu1CuvvCKHwyGHw6ETJ07476+oqFBycrI6d+6s9PR0ffbZZz/STw/gSkVQAbSCBx98UB999JE2bNigP/3pT7rvvvs0btw4VVdX+/ucPXtW8+fP129/+1vt2rVLbrdbhYWF/vfnzp2r3//+93r99df10Ucfqa6uTps3b/a//8orrygtLU2PPPKIPB6PPB6PrrnmGv/706dP18svv6zy8nJ16tRJv/jFL36Unx3AlYtjugGbHT16VOvXr9eXX36p2NhYSVJhYaHef/99vf7663rxxRclSQ0NDVq+fLkGDRokSXrsscc0Z84c/zivvvqqioqK9NOf/lSStHjxYm3ZssX/fo8ePRQREaHOnTsrJiYmaB4vvPCCbr31VknStGnTdOedd+q7775TVFRU6/zgAK54BBWAzT7++GMZhqHrrrsuoN3n86l3797+1507d/YHFJLUr18/1dTUSJL+9re/6auvvtLNN9/sf9/pdCopKUlNTU0tmseNN94YMLZ0/qmDcXFxof9QANACBBWAzZqamuR0OlVRUSGn0xnwXteuXf3/Dg8PD3jP4XDIfGq+w+EIeB3KqfrfH//COC0NSADACtZUADYbMWKEGhsbVVNTo5/85CcBV3Nliub06NFDLpdLZWVl/rbGxkZVVlYG9IuIiFBjY6Ot8wcAq8hUADa77rrr9LOf/UxTpkzRyy+/rBEjRqi2tlYffPCBhg0bpjvuuKNF4zz++OMqLi7WT37yE11//fV69dVX9c033wRkLwYOHKj9+/frxIkT6tq1q3r16tVaPxYAXBaZCqAVvP7665oyZYr+5V/+RYMHD9Y//dM/af/+/QG7My7n6aef1uTJkzVlyhSlpaWpa9euGjt2bMBCy8LCQjmdTg0ZMkR9+/aV2+1ujR8HAFqER58DHURTU5MSExN1//3367nnnmvr6QBAEMofQDv1xRdfaNu2bbr11lvl8/m0ePFiHT9+XA888EBbTw0AmkX5A2inwsLCtGbNGo0aNUqjR4/WgQMHtH37diUmJrb11ACgWZQ/AACALchUAAAAWxBUAAAAWxBUAAAAWxBUAAAAWxBUAAAAWxBUAAAAWxBUAAAAWxBUAAAAW/w/EblUYU90rn8AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(reviews.corr(),cmap='coolwarm',annot=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "20cafc27",
   "metadata": {},
   "outputs": [],
   "source": [
    "review_class=df[(df.Rating==1) | (df.Rating==5)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "ec07b328",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = review_class['Review']\n",
    "y = review_class['Rating']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "cd76f837",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "cv=CountVectorizer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "39a57ba0",
   "metadata": {},
   "outputs": [],
   "source": [
    "X=cv.fit_transform(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8588488e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "796eb1e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "dcbbc54a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.naive_bayes import MultinomialNB\n",
    "nb=MultinomialNB()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "10988913",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MultinomialNB()"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nb.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "4bc1296b",
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions=nb.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "c609eb42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 370   48]\n",
      " [   9 2716]]\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           1       0.98      0.89      0.93       418\n",
      "           5       0.98      1.00      0.99      2725\n",
      "\n",
      "    accuracy                           0.98      3143\n",
      "   macro avg       0.98      0.94      0.96      3143\n",
      "weighted avg       0.98      0.98      0.98      3143\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import classification_report,confusion_matrix\n",
    "print(confusion_matrix(y_test,predictions))\n",
    "print(classification_report(y_test,predictions))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "992837c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import TfidfTransformer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "47578276",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.pipeline import Pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "6ac57efb",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipeline = Pipeline([\n",
    "    ('bow', CountVectorizer()),  # strings to token integer counts\n",
    "    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores\n",
    "    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier\n",
    "])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "c29b9dff",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = review_class['Review']\n",
    "y = review_class['Rating']\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=101)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "de6b6412",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pipeline(steps=[('bow', CountVectorizer()), ('tfidf', TfidfTransformer()),\n",
       "                ('classifier', MultinomialNB())])"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipeline.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "4b00d5af",
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions = pipeline.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "d3c5e756",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[   3  415]\n",
      " [   0 2725]]\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           1       1.00      0.01      0.01       418\n",
      "           5       0.87      1.00      0.93      2725\n",
      "\n",
      "    accuracy                           0.87      3143\n",
      "   macro avg       0.93      0.50      0.47      3143\n",
      "weighted avg       0.89      0.87      0.81      3143\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(confusion_matrix(y_test,predictions))\n",
    "print(classification_report(y_test,predictions))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1c0b60e",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
