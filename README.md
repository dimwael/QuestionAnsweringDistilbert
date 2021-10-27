# Question Answering system based on DistilBert 

This is a Python project for dealing with simple questions about general knowledge. 

## Installation for localhost

1-Clone the project

2-Rename the app.py to app-backup.py

3-Rename the app-localhost.py to app.py

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
3-Add a new Inbound rule for the TCP Port 5000

4-Run the image:
```bash
docker-compose up -d
```
5-The container could use some time before it becomes accessible < 50 sec

6-You should be able to access the app on "INSTANCE-PUBLIC-IP":5000 

PS: You can always make sure to use the app.py designed for the public access by renaming 
the (app.py to app-backup.py) and then renaming the (app-public.py to app.py)

## Usage

```python
python app.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
