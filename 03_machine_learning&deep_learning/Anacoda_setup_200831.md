> 데이터 분석 개발 IDE는 jupyter notebook

> ​					개발환경은 anaconda 가상환경을 만들어서 사용



1. Anacoda 다운

2. Anacoda 설치

3. Anacoda는 무료이고, python과 다수의 유용한 package를 우리가 사용하기 쉽도록 제공해 주는 플랫폼이다.

4. Anacoda Prompt를 관리자 권한으로 실행

5. 제일 먼저 해야 할 작업은 pip를 최신버전으로 upgrade부터 해야 한다

   ```bash
   python -m pip install --upgrade pip
   ```

6. 가상환경을 생성한다.

   ```bash
   conda create -n data_env python=3.7 openssl
   python -V
   # Python 3.7.7
   # tessorflow 2.0을 쓰기 위해 Python 버전을 3.7로 지정
   ```

   

7. 정상적으로 가상환경이 만들어졌는지 확인해보기.

   ```bash
   conda info --envs
   ```

8. 새로운 가상환경으로 전환

   ```bash
   activate data_env
   ```

9. 개발 도구인 IDE를 설치해야 한다.

   => jupyter notebook이라는 web 기반의 개발툴을 이용한다.

10. 현재 data_env 가상환경에서

    ```bash 
    conda install nb_conda
    ```

11. jupyter notebook이 사용할 기본 디렉토리 (working directory)를 설정해야 한다.

    이 작업을 하기 위해, 환경설정파일을 생성하여 기본 디렉터리를 지정해서 사용한다.

    ```bash
     jupyter notebook --generate-config
     
    (data_env) C:\Users\j828h>jupyter notebook --generate-config
    Writing default config to: C:\Users\j828h\.jupyter\jupyter_notebook_config.py
    ```

    - 환경설정 파일이 어디 저장될지 알려준다.

    ```python
    # C:\Users\j828h\.jupyter\jupyter_notebook_config.py
    
    ## The directory to use for notebooks and kernels.
    c.NotebookApp.notebook_dir = 'C:/notebook_dir'
    # 해당 경로에 폴더 생성
    ```

13. IDE를 실행시켜 보자.

    ```bash
    jupyter notebook
    ```

    ![jupyter](markdown-images/jupyter.PNG)



ctrl + enter -> cell 실행

# 개발 환경 구축

### Jupyter Notebook 실행

Anaconda Prompt 관리자 권한으로 실행

```
(base) C:\WINDOWS\system32>activate data_env
(data_env) C:\WINDOWS\system32>jupyter notebook
```



### 칸 하나를 cell이라고 부른다.

-   a key: 현재 cell 위쪽에 새로운 cell을 생성한다.
-   b key : 현재 cell 아래쪽에 새로운 cell을 생성한다.
-   dd key : 현재 cell을 삭제
-   ctrl + enter : 현재 cell을 실행



### Numpy

> Numpy : Numperical Python
> 
> -   수치 계산에 최적화된 Python module
> -   vector, matrix 연산에 특화되어 있다.
> -   Pandas, Matplotlib의 기반이 되는 module
> -   machine learning, deep learning에서 많이 사용된다.



## ndarray의 특징

-   Numpy는 ndarray라고 불리는 n-차원의 배열을 제공한다.
-   python의 list와 상당히 유사하다.
-   python의 list는 다른 데이터 타입을 한 list 안에 저장할 수 있다.
-   Numpy의 ndarray는 모두 같은 데이터 타입을 사용해야 한다.
-   Python의 list보다 메모리 효율이나 실행 속도면에서 우위를 차지한다.



### Numpy module 설치하고 이용하기

```
pip install numpy
conda install numpy
```
