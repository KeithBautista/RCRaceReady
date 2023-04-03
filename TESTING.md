# Testing
Back to the [README](README.md)

* Continuous testing has been conducted throughout the project's development. Each view was regularly tested, and debugging occurred at any point where the outcome did not meet expectations.

## Python Validation - PEP8
* To ensure there were no syntax errors in the project, Python testing was performed using PEP8 Online. All Python files were entered into the online checker, and no errors were found in any of the custom codes.

#### RCRaceReady 
* [asgi.py](assets/readme/testing/pythonValidation/asgiRCRaceReady.png)
* [wsgi.py](assets/readme/testing/pythonValidation/wsgiRCRaceReady.png)
* [urls.py](assets/readme/testing/pythonValidation/urlsRCRaceReady.png)
* [views.py](assets/readme/testing/pythonValidation/viewsRCRaceReady.png)

#### RCRaceReady - Bag
* [contexts.py](assets/readme/testing/pythonValidation/contextsBag.png)
* [urls.py](assets/readme/testing/pythonValidation/urlsBag.png)

#### RCRaceReady - Checkout
* [admin.py](assets/readme/testing/pythonValidation/adminCheckout.png)
* [apps.py](assets/readme/testing/pythonValidation/appsCheckout.png)
* [forms.py](assets/readme/testing/pythonValidation/formsCheckout.png)
* [models.py](assets/readme/testing/pythonValidation/modelsCheckout.png)
* [signals.py](assets/readme/testing/pythonValidation/signalsCheckout.png)
* [urls.py](assets/readme/testing/pythonValidation/urlsCheckout.png)
* [views.py](assets/readme/testing/pythonValidation/urlsCheckout.png)
* [webhooks_handler.py](assets/readme/testing/pythonValidation/webhooks_handlerCheckout.png)
* [webhooks.py](assets/readme/testing/pythonValidation/webhooksCheckout.png)

#### RCRaceReady - Products
* [admin.py](assets/readme/testing/pythonValidation/adminProducts.png)
* [forms.py](assets/readme/testing/pythonValidation/formsProducts.png)
* [models.py](assets/readme/testing/pythonValidation/modelsProducts.png)
* [urls.py](assets/readme/testing/pythonValidation/urlsProducts.png)
* [views.py](assets/readme/testing/pythonValidation/urlsProducts.png)

#### RCRaceReady - Profiles
* [forms.py](assets/readme/testing/pythonValidation/formsProfile.png)
* [models.py](assets/readme/testing/pythonValidation/modelsProfile.png)
* [urls.py](assets/readme/testing/pythonValidation/urlsProfile.png)
* [views.py](assets/readme/testing/pythonValidation/urlsProfile.png)

## Performance

Below is the report generated from lighthouse via Chrome DevTools for the Desktop website. Whilst this could be better, precautions I have taken have been to convert images to WEBP to enable a fast load time. Though I don't doubt there there are further changes that need to be made to maximize this.<br>

<img src="readmeassets/lightHousePerformance.png">

## HTML Validation
![HTML Validation Result](readmeassets/extras/validation/htmlValidation.png).
* HTML was validated using W3 Validator, whilst there are no errors there are 2 warnings and 18 Info messages present.

## CSS Validation
![CSS Validation Result](readmeassets/extras/validation/cssValidation.png).

## Backend/Admin Panel
* I have repeatedly tested the Admin Panel since the start of the project's development. All the models are working without issues. I have successfully created, deleted, and updated data in all models without any errors. The models have the expected behavior for which they were built.

## Manual Testing
### Frontend
* The Signup, Login, and Logout system is working correctly and has no issues. It displays the appropriate interactive message to the users.

* The Profile Page is functioning properly. It updates the user's information and uploads/updates the user profile image. Once the update is complete, it shows the interactive message to the user.

* The user profile image in the navbar and Post Details page is working without issues and displays the user's image when it is uploaded on the Profile Page.

* All internal links are functioning correctly and direct the user to the correct page on the website.

* All external links are working correctly and direct the user to the correct social media page by opening a new browser tab.

* The comment form is without issues and submits a new comment once the form is completed by any user.

* On the Movie Page, the CRUD functionality is working without issues. Logged-in users can create a new post such as update or delete their own Movie Posts. Also, any post can be updated or deleted on this page by the Superuser.

### Backend/Admin Panel
* I have repeatedly tested the Admin Panel since the start of the project's development. All the models are working without issues. I have successfully created, deleted, and updated data in all models without any errors. The models have the expected behavior for which they were built.