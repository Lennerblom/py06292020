import requests
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    city = 'Seattle'
    ENV_key = 'add .env stuff'

    r = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=imperial&appid={ENV_key}')
    weather_data = r.json()
    labels = ['M', 'T', 'W', 'TH', 'F', 'S','SN']
    temperature = []
    for i in range(7):
        temperature.append(weather_data['list'][i]['main']['temp'])
    width = 0.35
    fig, ax = plt.subplots()
    ax.bar(labels, temperature, width, label='farenheit')
    ax.set_ylabel('temperature')
    ax.set_title('Seven Day Temperatures')
    ax.legend()

    plt.savefig("mygraph.png")


if __name__ == "__main__":
    main()
