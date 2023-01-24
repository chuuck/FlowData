# QData

QData is an open source project which aims to easily query data by letting the user provide the instructions in natural language. For the moment the functionality of the project is limited, as it only displays the results of the data in a tabular form, however, more functionality will be added with a hope that data analysis could be done using just natural language.

## 1. Architecture :building_construction:

As Python has become the most used programming language amongst Data Scientists it was decided to write the back-end of the code in Python, therefore, allowing the majority of the practice to contribute to project if desired. Despite that it was inevatable that an additional language would be used, in this case it being JavaScript (mostly only for front-end parts). There were multiple frameworks and libraries used, so in Figure 1 you will see a rough diagram that showcases all of them. That should help you understand the overall architecture of the app and if you want to learn something new you can easily learn it without understanding other parts.


![alt text](https://github.com/chuuck/QData/blob/main/diagram.png)

**Vue.js** - JavaScript framework that helps to build user interfaces in the front-end side, its a really powerful framework to know if you ever plan to explore how to correctly build front-end of applications as it closely relates to React and Angular.js as well. One feature that is really helpful is its reactivty, meaning that whenever you change a variable in the front-end you don't need to refresh the page to see the changes in the view, they will automatically change as you update your variables.

**Bootstrap.js** - Front-End framework that helps to make the GUI a lot better, if you don't like to use the default HTML buttons and input fields then bootstrap is an option to go with in the future.

**Axios** - It enables communication between Front-End and Back-End through POST/GET requests. Really simple tool and really powerful as well.

**Flask** - Its a web framework that is also mainly used for communication between Front-End and Back-End except Flask is written in Python, a bit tricker I find to work with than Axios but it is necessary for Back-End.

**OpenAI** - Mainly using OpenAI Codex API, to translate natural language to SQL. More functionality can be added in the future using GPT-3 as well.

**Pandas** - If you don't know what Pandas library is, something has terribly gone wrong. It allows for data manipulation, but most importantly pandasql allows to query Pandas Dataframes using SQL language, there are some better alternatives that might be quicker, so feel free to explore.


## 2. Getting Started :rocket:


## 3. Contributing :pencil2:



## 4. Feedback :bulb:

If you ever have some feedback that you would like to pass on, you can either send it to me directly
