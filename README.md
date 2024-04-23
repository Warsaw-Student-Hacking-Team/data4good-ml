# ecommute berlin - ML & backend app

This is the repository for the ML & backend app of the ecommute berlin project for the data4good hackathon 2024.

Technologies used:
* pytorch
* numpy & pandas
* fastapi
* onnx runtime
* ![435447512_753852496891601_3116057107313378568_n](https://github.com/Warsaw-Student-Hacking-Team/data4good-ml/assets/116288437/a011e35a-b1ad-497c-95d4-0416e848e757)



Checkout our frontend repo at: https://github.com/Warsaw-Student-Hacking-Team/data4good-frontend

We also share the api at

* https://ecommute.micorix.dev/api/predict_pm10/day?l_spared=<n>
  * where `<n>` is number of trips not taken
  * output: difference between predicted pm10 level and level of pm10 due to the number of trips not taken at given day.

* https://ecommute.micorix.dev/api/predict_pm10/day?l_spared=<n>&hour=<h>
  * where `<n>` is number of trips not taken. `<h>` is hour - int from range [0, 23]
  * output: difference between predicted pm10 level and level of pm10 due to the number of trips not taken at given hour.
