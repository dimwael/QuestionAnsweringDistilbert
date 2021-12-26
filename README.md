# Question Answering system based on DistilBert 

This is a Python project for dealing with simple questions about general knowledge. 

## Installation for localhost

1-Clone the project

2-Install dependencies by running the following command:
```bash
pip install -r requirements.txt
```
## Installation for Public Access using Dockerfile & docker-compose

1-Clone the project

2-Build the docker image:
```bash
docker-compose build
```
3-Add a new __Inbound rule__ for the __TCP Port 5000__

4-Run the image:
```bash
docker-compose up -d
```
5-The container could use __some time__ before it becomes accessible < __50 sec__

6-You should be able to access the app on __"INSTANCE-PUBLIC-IP":5000__

## Usage

```python
python app.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
