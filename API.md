**Get Accounts**
----
  Returns json data of accounts.

* **URL**

  /v1/accounts/

* **Method:**

  `GET`
  
*  **URL Params**

  None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />


**Get Payments**
----
  Returns json data of payments

* **URL**

  /v1/payments/

* **Method:**

  `GET`
  
*  **URL Params**

  None

* **Data Params**

  None


**Post Payments**
----
  POST payment to create payment objects

* **URL**

  /v1/payments/

* **Method:**

  `POST`
  
*  **URL Params**

  None

* **Data Params**

  :: amount: Float value
  :: to_account: GUID string
  :: from_account: GUID string
  :: initiated_by: GUID string

