function call_ajax() {
    // 입력 텍스트 상자에서 키보드 입력이 들어왔을 때 호출

    // keyCode 13 - 모든 키에 대해서 처리하는게 아니라 enter key일 경우에만 처리
    if (event.keyCode == 13) {
        // AJAX call을 이용해서 데이터를 받아오는 코드가 나오면 된다.

        // 입력된 key가 enter key이면 이 부분을 수행한다.
        // jQuery로 AJAX 처리를 한다.

        // alert("엔터가 입력되었어요!!")

        // ajax의 인자로 javascript의 객체를 넣어준다.
        // javascript 객체는 => { key : value, key : value, .. }

        // data : 서버 프로그램에게 넘겨줄 데이터들..
        // 초는 밀리세컨드 단위, 3000 = 3초
        $.ajax({
            async: true,    // 비동기 방식의 호출 (default)
            url: "http://ip주소:port번호/bookSearch/search",
            data: {
                keyword: $("input[type=text]").val()
                // keyword: $("[id=myInput]").val()
            },
            // method: "GET",
            type: "GET",
            timeout: 3000,
            dataType: "json",       // 결과 JSON을 JavaScript 객체로 변환
            
            // 서버가 보내준 json 문자열을 JavaScipt 객체로 변환 -> result
            success : function(result) {
                // alert("서버호출 성공!!")

                // alert(result[0].title)  // 저자

                // $("tbody").empty()

                // $("h1").each()

                // $.each(result, function(idx, item) {
                //     var tr = $("<tr></tr>")     // <tr></tr>
                //     var imgTd = $("<td></td>")  // <td></td>
                //     var img = $("<img />").attr("src", item.img)      // <img src=~~>
                //     imgTd.append(img)
                //
                //     var titleTd = $("<td></td>").text(item.title)
                //     var authorTd = $("<td></td>").text(item.author)
                //     var priceTd = $("<td></td>").text(item.price)
                //     var btnTd = $("<td></td>")
                //     var btn = $("<input />").attr("type","button").attr("value", "삭제")
                //
                //     tr.append(imgTd)
                //     tr.append(titleTd)
                //     tr.append(authorTd)
                //     tr.append(priceTd)
                //     tr.append(btnTd)
                //     btnTd.append(btn)
                //
                //     $("tbody").append(tr)
                //
                // })

                /*
                <tr>
                    <td>표지</td>
                    <td>제목</td>
                    <td>저자</td>
                    <td>가격</td>
                    <td>삭제</td>
                    <td>
                        <input type=button value=삭제 onclick=do_delete()>
                    </td>
                </tr>
                */


                for (var i=0; i < result.length; i++) {
                    var tr = $("<tr></tr>")     // <tr></tr>
                    var imgTd = $("<td></td>")  // <td></td>
                    var img = $("<img />").attr("src", result[i].img)      // <img src=~~>
                    imgTd.append(img)

                    var titleTd = $("<td></td>").text(result[i].title)
                    var authorTd = $("<td></td>").text(result[i].author)
                    var priceTd = $("<td></td>").text(result[i].price)

                    var delTd = $("<td></td>")
                    var delBtn = $("<input />").attr("type","button")
                        .attr("value", "삭제")

                    delBtn.on("click", function () {
                        // alert("이 책을 삭제합니다")
                        // 현재 클릭된 버튼에 대한 책 정보를 찾아 화면에서 삭제
                        // this : 현재 이벤트가 발생된 객체를 지칭!
                        $(this).parent().parent().remove()
                    })

                    delTd.append(delBtn)

                    tr.append(imgTd)
                    tr.append(titleTd)
                    tr.append(authorTd)
                    tr.append(priceTd)
                    tr.append(delTd)


                    $("tbody").append(tr)

                }

             },

            error : function(error) {
                alert("서버호출 실패!!")
            }

        })
   
    }
}
