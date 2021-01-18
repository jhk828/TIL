function print_text() {
    // 버튼을 눌렀을 때 실행할 코드를 기술해요!!
    // alert("호출되요")

    // .text() - tag 사이의 문자
    console.log($("#apple").text())
    console.log($("#pineapple").text())
    console.log($("ul > li[class]").text())

    // val() - 사용자 입력
    console.log($("input[type=text]").val())

    console.log($("ol > li.myList:first").text())               // 고양이
    // 순번 1번부터
    console.log($("ol > li.myList:nth-child(0)").text())        // 고양이
    console.log($("ol > li.myList:first + li").text())          // 호랑이
    console.log($("ol > li.myList:last").text())                // 강아지
    
    // attr() - 속성 제어 메소드
    $("input[type=text]").attr("size", 10)
    
}

function my_func() {
    // alert("과일이 바뀌었어요!!")
    // select box에서 과일이 바뀌면 실행되요!

    // 1. 선택한 과일이 어떤 과일인지 알아내야 한다.
    var fruit = $("select > option:selected").text()

    var my_list = $("ul > li")
    // my_list.each("람다함수")
    my_list.each(function(idx, item) {
        // console.log($(item).text())
        if($(item).text() == fruit) {
            $(item).css("color", "red")
        } else {
            $(item).css("color", "black")
        }
    })
}