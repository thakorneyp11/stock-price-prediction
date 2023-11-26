# Stock Price Prediction
An **end-to-end Machine Learning workflow** focused on stock price forecasting. This project encompasses everything from the ML development process to the ML production lifecycle.


## 💡 Features
- Forecasting stock price using Machine Learning
- Real-time dashboard showing forecasted values
- Observability dashboard for ML models and their performance
- Open APIs for data retrieval


<!-- ## 💻 Images -->


## 🛠️ Tools
- [**BinanceAPI**](https://github.com/sammchardy/python-binance/tree/master) - for data retrieval from Binance
- [**MageAI**](https://www.mage.ai/) - for data processing pipeline
- [**DVC**](https://dvc.org/) - for data versioning control
- [**PyCaret**](https://pycaret.org/) - for Automated ML model training
- [**Weights & Biases**](https://wandb.ai/site) - for model experiment tracking
- [**Aporia's MLNotify**](https://github.com/aporia-ai/mlnotify) - for model training monitoring service ([Aporia official website](https://www.aporia.com/))
- [**Docker**](https://www.docker.com/) - for system containerization and deployment
- [**BentoML**](https://github.com/bentoml/BentoML) - for model serving ([BentoML official website](https://www.bentoml.com/))
- [**Yatai**](https://github.com/bentoml/Yatai) - for model serving at Scale on Kubernetes ([BentoML official website](https://www.bentoml.com/))
- [**Caddy**](https://caddyserver.com/) - for reverse proxy of services
- [**Grafana and Prometheus**](https://grafana.com/) - for system, model, hardware observability


## 🧩 Components
- Coming soon


## 🌐 Architecture
<details>
<summary>System Architecture (coming soon)</summary>
</details>

<details>
<summary>Functional Architecture (coming soon)</summary>
</details>


## ⚙️ Setting up
```bash
# clone this repository
git clone https://github.com/thakorneyp11/stock-price-prediction.git

# change directory to project
cd stock-price-prediction

# create virtual environment (`pip3 install virtualenv` if not installed)
virtualenv env

# activate virtual environment
source env/bin/activate

# install dependencies
pip3 install -r requirements.txt
```


<!-- ## 💾 Database -->
<!-- ## 📊 Data/Payload Schema -->


# 🚀 ML Workflow Overview
## 1. Data Collection

**Data Sources:**
- [Binance Data Dumper](https://github.com/stas-prokopiev/binance_historical_data/tree/master): included data from 2017 to Now
- [Kaggle - prasoonkottarathil/btcinusd](https://www.kaggle.com/datasets/prasoonkottarathil/btcinusd): only included data from 2017-2021
- [Binance API](https://github.com/sammchardy/python-binance/tree/master): only support few candles per request, not suitable for historical data retrieval

**Download Historical Data:**
- Download historical data from Binance Data Dumper: `python3 data_download.py`
- Raw CSV dataset: `dataset/BTCUSDT_15m_Aug2017-Oct2023.csv`

**Retrieve Real-time Data:**
- sample script can be found in `data_retrieval.py` (later will scheduled executed using MageAI)
- <u>note</u>: need to update `.env` file with Binance API key and secret

<img width="1000" alt="Raw CSV dataset" src="https://github.com/thakorneyp11/stock-price-prediction/assets/58812639/4961dd43-c409-4416-9552-773de503d6fd">

## 2. Feature Engineering
- Exploratory Data Analysis (EDA): `eda.ipynb`
- Feature Engineering: `feature_engineering.ipynb` ([reference](https://github.com/mcvoramet/altoacademy-feature-engineering))
- Processed CSV dataset: 1) `dataset/feature_extracted_data.csv` and 2) `dataset/feature_selected_data.csv`

**EDA results:**
<img width="1000" alt="EDA results" src="https://github.com/thakorneyp11/stock-price-prediction/assets/58812639/de9582af-dcc6-47ec-b7e9-5f65e55ad89f">

**Feature Engineering results:**
<img width="1000" alt="Feature Engineering results" src="https://github.com/thakorneyp11/stock-price-prediction/assets/58812639/82020337-9764-4f13-be15-cdc6826ebf5b">

## 3. Data Versioning
- Coming soon

## 4. Model Training
- Coming soon

## 5. Model Serving
- Coming soon

## 6. ML Pipeline
- Coming soon

## 7. Model Observability
- Coming soon

## 8. Model Auto-Retraining
- Coming soon
