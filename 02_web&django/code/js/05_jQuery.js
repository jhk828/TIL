// jQuery CDN을 이용했기 때문에 jQuery code를 사용할 수 있다.

// 버튼을 클릭하면 아래의 함수가 호출된다.
function my_func() {
    // alert("함수가 호출되요!!!")

    // 0. jQuery를 공부할 때 가장 먼저 배워야 하는건 -> selector

    // 1. 전체 선택자 ( universal selector )
    //      $-jQuery로/ *-모든 element선택해서 /.css() 색 바꾸는 method 실행
    $("*").css("color", "red")

    // 2. 태그 선택자 ( tag selector )
    $("li").remove()

    // 3. 아이디 선택자 ( id selector ) - 기호 # 이용
    $("#haha").text()   // 인자가 없으면 값을 알아오라는 의미
    $("#haha").text("제주") // 인자가 있으면 값을 변경하라는 의미

    // 4. 클래스 선택자 (class selector)
    $(".region").css("background-color", "yellow")

    // 5. 구조 선택자 (자식 선택자 혹은 후손 선택자)
    //      ol의 자식 모두
    $("ol > *")
    //      ol의 자식 중 li 모두
    $("ol > li").css("color", "steelblue")  // > 자식 선택자
    $("div > li").css("color", "pink")

    // 6. 구조 선택자 ( 형제 선택자)
    //   #haha 바로 다음 li
    $("#haha + li").remove()
    //   # #haha 다음에 있는 모든 li
    $("#hong ~ li").remove()

    // 7. 속성 선택자
    $("[id]").css("color", "yellow")
    $("[id=haha]").css("color", "yellow")

    // 이 7가지를 조합하면 웬만한 element는 지정하는게 가능!
}