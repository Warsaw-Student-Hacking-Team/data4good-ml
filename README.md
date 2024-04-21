# ecommute berlin - ML & backend app

This is the repository for the ML & backend app of the ecommute berlin project for the data4good hackathon 2024.

Technologies used:
* pytorch
* numpy & pandas
* fastapi
* onnx runtime


Checkout our frontend repo at: https://github.com/Warsaw-Student-Hacking-Team/data4good-frontend

We also share the api at

* https://ecommute.micorix.dev/api/predict_pm10/day?l_spared=<n>
  * where `<n>` is number of trips not taken
  * output: difference between predicted pm10 level and level of pm10 due to the number of trips not taken at given day.

* https://ecommute.micorix.dev/api/predict_pm10/day?l_spared=<n>&hour=<h>
  * where `<n>` is number of trips not taken. `<h>` is hour - int from range [0, 23]
  * output: difference between predicted pm10 level and level of pm10 due to the number of trips not taken at given hour.
