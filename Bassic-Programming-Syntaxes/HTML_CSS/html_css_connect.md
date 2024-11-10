# HTML, CSS 연결

## 1. Inline stylesheet
> HTML 태그 내부에서 CSS 코드를 작성

```HTML
<p style="color: blue"></p>
```
태그 내부 스타일 속성을 이용해서 CSS를 적용한다.

<br>

## 2. Internal Style Sheet
> HTML 파일 내부에 CSS 코드를 작성
```HTML
<style>
  h1 {
    color: blue;
  }
</style>
```
style태그를 이용해서 HTML파일에 적용되는 CSS 코드를 작성한다.

<br>

## 3. 외부 파일로 연결
> 외부 CSS 파일을 HTML 파일과 연결
```HTML
<link rel="stylesheet" href="css/style.css">
```



