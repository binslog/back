## 20221021 07_pjt

---

## 1. 파이썬을 세팅한다.

```python
# 기본적인 세팅먼저.
` python -m venv venv
` source venv/Scripts/activate
` pip install -r requirements.txt
` django-admin startproject mypjt . # . 띄어주고,
` python manage.py startapp movies

` python manage.py loaddata movies.json
` python manage.py makemigrations
` python manage.py migrate
```

## 2. 기본적인 장고 세팅
- models.py => urls.py => views.py
- 이제 template는 만들어주지 않기로 한다.

### 1. mypjt
```python
#1. mypjt => settings.py
INSTALLED_APPS = [
    'movies',
    'rest_framework',
    ...
    ] 

#2. mypjt => urls.py
path('api/v1/',include('movies.urls')),

# 해당 movies로 가기위한 왜냐하면, articles app_name
# 해주는 거랑 똑같이 생각한다.
```

<이 작업을 기점으로 더이상 my_pjt는 건들지 않는다.>

---

### 2. movies app으로 온다
* <models.py => urls.py => views.py & serializers.py>

---
## 1) Models.py
<해당되는 클래스에 선언하자>
### 1. TEXT
* 텍스트의 크기가 있으면,
name = models.CharField(max_length=200)
* 크기가 없으면
overview = models.Textfield
  
### 2. DateTimeField
- 날짜를 나타낼 때 설정
- auto_now_add와 auto_now 구분
- add가 있으면 created, 없으면 updated

### 3. 외래키 설정
- movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

### 4. 다대다 관계 설정
- actors = models.ManyToManyField(Actor,related_name='movies')

---
## 2) urls.py
```python
path('actors/,views.actor_list),
     
path('actors/<int:actor_pk>/,views.actor_detail),

path('movies/<int:movie_pk>/reviews/',)


1. pk값 없을떄
2. pk값에 해당되는 detail
3. movie의 pk에 해당하는 리뷰!
```
---
## 3) views.py

### (1)
1. 처음에 from --- import-- 할때 만든 serializer는 항상 import하자.
2. 만든 모델도 항상 .models 뒤에 import 해야한다.

### (2)

#### '@' api_view(['GET']), 데코레이터를 통해 명령어를 먼저 지정해주자.

```python
if request.method == 'GET':
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

1. 먼저 actors를 통해 Actor 모델을 모두 가져오자.  
2. 그리고 Serializer = ActorSerializer(actor)를 통해
해당되는 값들을 serailizer 해주고,
3. 마지막으로 Response는 (serializer.data)로 !!
4. many=True 는 여러가지 참조하고 싶을 때 쓴다. 혼자 있으면 안써도 상관x

---

# 만약에 디테일 같이 특정 pk 값을 받아오고 싶다면??
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
처럼 사용하면 된다..!!

``` 

---
### (3) GET, DELETE, PUT

```python
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

1. API 지정해주고,
2. 전체가 아니기 때문에 해당되는 PK가 필요하다.  

- 'GET'은 Serializer = ReviewSerializer(review)
=> serializer 안에서, GET을 저절로 한다. 

- 'DELETE'는 review.delete()... 
=> status 를 반환하는 것을 유의!!

- 'PUT'은 Serializer 한다음에...   
=> vaild하면 save, 그렇지 않으면 에러 메시지 출력!!
=> .is_valid 뒤에 (raise_exception=True) 암기...!!


- 'CREATE'는....
`serializer = ReviewSerializer(data=request.data)
- serializer 해주고... put과 동일하게 하면 된다.
- 주의할 점은  serializer.save(movie=movie)가 필요하다..!!

```

---

## (4). Serializers.py
- class 안에 class를 넣는 방법이 있지만, 이번에는 하나의 class를 하나 더 생성해주었다.

```python
# 1. 기본틀
class ActorListSerializer(serializers.ModelSerializer):
   class Meta:
     Model = Actor
     fields = ('id','name',)

1. 해당 필드를 출력한다.
2. model = Actor와 같이 class 설정해주고,,

     
# 2. 클래스를 참조할 때, Meta 위에 다음과 같이 설정해준다. 
class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'

# 3. 조건에 맞는 serializer을 하기 위해서 일일이 조정해준다.
class MovieSerializer(serializers.ModelSerializer):
    actors = ActornameSerializer(many=True,read_only=True)
    review_set = ReviewSetSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('id','actors','review_set', 'title','overview','release_date','poster_path',)


```
   






































