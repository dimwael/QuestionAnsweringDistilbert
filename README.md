# Question Answering system based on DistilBert 

This is a Python project for dealing with simple questions about general knowledge. 

## Installation for localhost

1-Clone the project

2-Rename the __app.py__ to __app-backup.py__

3-Rename the __app-localhost.py__ to __app.py__

4-Install dependencies by running the following command:
```bash
pip install -r requirements.txt
```
## Installation for Public Access using Dockerfile & docker-compose

1-Clone the project

2-Build the docker image:
```bash
docker build -t  qa-distilbert:v1 .
```
3-Add a new __Inbound rule__ for the __TCP Port 5000__

4-Run the image:
```bash
docker-compose up -d
```
5-The container could use __some time__ before it becomes accessible < __50 sec__

6-You should be able to access the app on __"INSTANCE-PUBLIC-IP":5000__

PS: You can always make sure to use the __app.py designed for the public access__ by renaming 
the __(app.py to app-backup.py)__ and then renaming the __(app-public.py to app.py)__

## Usage

```python
python app.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
