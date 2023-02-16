
<p align="center">
  <img src="https://github.com/chuuck/QData/blob/main/img/logo.png" />
</p>

#    

QData is an open source project which aims to easily query data by letting the user provide instructions in natural language. For the moment the functionality of the project is limited, as it only displays the results of the data in a tabular form, however, more functionality will be added with a hope that data analysis could be done using just natural language

## 1. Demos :video_camera:

Here are two demos that showcase the functionality of the web app.


<details>
  <summary>Demo using single file CSV file</summary>
https://user-images.githubusercontent.com/59098387/214292487-cb7fa63b-28e8-4f86-92a8-6683d3c55ca6.mov
</details>

<details>
  <summary>Demo using multiple file CSV file</summary>
https://user-images.githubusercontent.com/59098387/214292584-ce338da2-cfc6-488b-9559-7e43e3af71ff.mov
</details>

## 2. Architecture :building_construction:

As Python has become the most used programming language amongst Data Scientists it was decided to write the back-end of the code in Python, therefore, allowing the majority of the practice to contribute to project if desired. Despite that it was inevatable that an additional language would be used, in this case it being JavaScript (mostly only for front-end parts). There were multiple frameworks and libraries used, so in Figure 1 you will see a rough diagram that showcases all of them. That should help you understand the overall architecture of the app and if you want to learn something new you can easily learn it without understanding other parts.


![alt text](https://github.com/chuuck/QData/blob/main/diagram.png)

**Vue.js** - JavaScript framework that helps to build user interfaces in the front-end side, its a really powerful framework to know if you ever plan to explore how to correctly build front-end of applications as it closely relates to React and Angular.js as well. One feature that is really helpful is its reactivty, meaning that whenever you change a variable in the front-end you don't need to refresh the page to see the changes in the view, they will automatically change as you update your variables.

**Bootstrap.js** - Front-End framework that helps to make the GUI a lot better, if you don't like to use the default HTML buttons and input fields then bootstrap is an option to go with in the future.

**Axios** - It enables communication between Front-End and Back-End through POST/GET requests. Really simple tool and really powerful as well.

**Flask** - Its a web framework that is also mainly used for communication between Front-End and Back-End except Flask is written in Python, a bit tricker I find to work with than Axios but it is necessary for Back-End.

**OpenAI** - Mainly using OpenAI Codex API, to translate natural language to SQL. More functionality can be added in the future using GPT-3 as well.

**Pandas** - If you don't know what Pandas library is, something has terribly gone wrong. It allows for data manipulation, but most importantly pandasql allows to query Pandas Dataframes using SQL language, there are some better alternatives that might be quicker, so feel free to explore.


## 3. Getting Started :rocket:

To get started you will need two terminal windows one for Front-End and one for Back-End.

### 3.1. Front-End

To add packages and started the Front-End side you will need ```yarn``` and ```node```. To install it you can use [HomeBrew](https://docs.brew.sh/Installation):

```
brew install yarn
brew install node
```

Then to set up the project you will have to change directory to the location where you have saved the front-end code and run command:

```
yarn install
```

Once that is done, you are ready to launch front-end side: 

```
yarn serve
```

### 3.2. Back-End

First you will need an API key from OpenAI which you can get [here](https://beta.openai.com/account/api-keys), and then add it in the back-end/.env file in quotes.

Then you will need to install all the requirements, in the main directory a ```requirements.txt``` has been prepared, so just use command:

```
pip3 install -r requirements.txt
```

Then you should be ready to lunch in back-end folder:

```
python app.py
```

You shuold be good to go at this point, so take a look at the code try to understand it and if you want to contribute go ahead and write some code.

## 4. Contributing :pencil2:

If you would you would like to contribute to the project you are more than welcome to do so here are a few guidlines:

- Bug fixes are the best and always welcome!
- If you don't understand the code you are changing, don't change it!
- New features are welcome, however, please include some tests.

If you would like to add additional features here are some ideas:

- Adding a graph section where a graph could be displayed answering the questions in the prompt.
- Adding a text section where a natural language could be used to answer the prompt using data.
- Visual improvements to the Front-End side of the app.
- Alter table once it has been created using prompts

<p align="center">
  <img width="200" src="https://github.com/chuuck/QData/blob/main/img/most_important_photo.jpeg" />
</p>

