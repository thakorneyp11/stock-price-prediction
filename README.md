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


<!-- ## ⚙️ Setting up -->
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

**Retrieve Real-time Data:**
- sample script can be found in `data_retrieval.py` (later will scheduled executed using MageAI)

## 2. Feature Engineering
- Coming soon

## 3. Model Training
- Coming soon

## 4. Model Serving
- Coming soon

## 5. Model Observability
- Coming soon

## 6. Model Auto-Retraining
- Coming soon
