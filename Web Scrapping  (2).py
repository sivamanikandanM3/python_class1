{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9d70d75a-6361-4f7b-885b-da9d1e9cd332",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'find_all'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[17], line 8\u001b[0m\n\u001b[0;32m      6\u001b[0m soup \u001b[38;5;241m=\u001b[39m BeautifulSoup(response\u001b[38;5;241m.\u001b[39mtext, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhtml.parser\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m      7\u001b[0m table_body \u001b[38;5;241m=\u001b[39m soup\u001b[38;5;241m.\u001b[39mfind(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtbody\u001b[39m\u001b[38;5;124m'\u001b[39m, class_\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mlister-list\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m----> 8\u001b[0m rows \u001b[38;5;241m=\u001b[39m table_body\u001b[38;5;241m.\u001b[39mfind_all(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtr\u001b[39m\u001b[38;5;124m'\u001b[39m)  \n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m index, row \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(rows[:\u001b[38;5;241m10\u001b[39m], start\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m):  \n\u001b[0;32m     10\u001b[0m     title_column \u001b[38;5;241m=\u001b[39m row\u001b[38;5;241m.\u001b[39mfind(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtd\u001b[39m\u001b[38;5;124m'\u001b[39m, class_\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtitleColumn\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'find_all'"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "url = \"https://www.imdb.com/chart/top/\"\n",
    "headers = { \"User-Agent\": \"Mozilla/5.0\"}\n",
    "response = requests.get(url, headers=headers)\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "table_body = soup.find('tbody', class_='lister-list')\n",
    "rows = table_body.find_all('tr')  \n",
    "for index, row in enumerate(rows[:10], start=1):  \n",
    "    title_column = row.find('td', class_='titleColumn')\n",
    "    rating_column = row.find('td', class_='ratingColumn imdbRating')\n",
    "    title = title_column.a.text.strip()\n",
    "    year = title_column.span.text.strip('()')\n",
    "    rating = rating_column.strong.text.strip()\n",
    "    print(f\"{index}. {title} ({year}) - {rating}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8b22cf8f-78ec-4bea-a462-d98afbbc5a26",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'find_all'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[17], line 8\u001b[0m\n\u001b[0;32m      6\u001b[0m soup \u001b[38;5;241m=\u001b[39m BeautifulSoup(response\u001b[38;5;241m.\u001b[39mtext, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhtml.parser\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m      7\u001b[0m table_body \u001b[38;5;241m=\u001b[39m soup\u001b[38;5;241m.\u001b[39mfind(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtbody\u001b[39m\u001b[38;5;124m'\u001b[39m, class_\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mlister-list\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m----> 8\u001b[0m rows \u001b[38;5;241m=\u001b[39m table_body\u001b[38;5;241m.\u001b[39mfind_all(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtr\u001b[39m\u001b[38;5;124m'\u001b[39m)  \n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m index, row \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(rows[:\u001b[38;5;241m10\u001b[39m], start\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m):  \n\u001b[0;32m     10\u001b[0m     title_column \u001b[38;5;241m=\u001b[39m row\u001b[38;5;241m.\u001b[39mfind(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtd\u001b[39m\u001b[38;5;124m'\u001b[39m, class_\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtitleColumn\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'find_all'"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "url = \"https://www.imdb.com/chart/top/\"\n",
    "headers = { \"User-Agent\": \"Mozilla/5.0\"}\n",
    "response = requests.get(url, headers=headers)\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "table_body = soup.find('tbody', class_='lister-list')\n",
    "rows = table_body.find_all('tr')  \n",
    "for index, row in enumerate(rows[:10], start=1):  \n",
    "    title_column = row.find('td', class_='titleColumn')\n",
    "    rating_column = row.find('td', class_='ratingColumn imdbRating')\n",
    "    title = title_column.a.text.strip()\n",
    "    year = title_column.span.text.strip('()')\n",
    "    rating = rating_column.strong.text.strip()\n",
    "    print(f\"{index}. {title} ({year}) - {rating}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7b7598c-2cf5-4836-974b-c5569f005c2b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d2c4f30-d1e8-47f7-a011-7e51714c734d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8abd7c13-bb5a-48a6-b00d-6516f3cb2706",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff72129a-4fc9-4d78-a4a5-4641874ce129",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ad845e7-5007-42db-9f8c-02fd83b60a4d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0cfb1993-e097-4773-b7bb-da8e3cf564f4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6b35c05-14bf-4e9e-84e2-25c707845329",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "057ecde8-28c0-4cb1-b120-d6557c0fccde",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa6c6dfd-d10c-493d-8098-c73fe854d5b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83e21ea4-517d-409b-ba9c-220c46adf66b",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
