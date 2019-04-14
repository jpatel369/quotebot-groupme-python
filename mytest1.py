import json

quotes_string = '''
{
"quotes": [
{
"id": 1,
"content": "There is no cure for birth and death save to enjoy the interval.",
"attribution": "George Santayana",
"topic_id": 1,
"created_at": "2018-01-19T02:12:02.566Z",
"updated_at": "2018-01-19T02:12:02.566Z"
},
{
"id": 2,
"content": "Without pleasure men would live like a fool and die. ",
"attribution": "Pierre de Beaumarchais",
"topic_id": 1,
"created_at": "2018-01-19T02:16:34.541Z",
"updated_at": "2018-01-19T02:16:34.541Z"
},
{
"id": 3,
"content": "All animals except man know that the principle business of life is to enjoy it.",
"attribution": "Samuel Butler",
"topic_id": 1,
"created_at": "2018-01-19T02:18:21.575Z",
"updated_at": "2018-01-19T02:18:21.575Z"
},
{
"id": 4,
"content": "Living well and beautiful and justly are all one thing. ",
"attribution": "Socrates",
"topic_id": 1,
"created_at": "2018-01-19T02:19:35.316Z",
"updated_at": "2018-01-19T02:19:35.316Z"
}
]
}
'''

data = json.loads(quotes_string)

for quote in data['quotes']:
    print (quote['content'])
