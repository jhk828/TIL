function call_ajax() {

    if (event.keyCode == 13) {
        var my_str = $("input[type=date]").val().toString().split('-')// 200721 2020-07-16
        var my_date = my_str[0] + my_str[1] + my_str[2]
        console.log(my_date)

        $.ajax({
            async: true,    // 비동기 방식의 호출 (default)
            url: "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=key번호",
            data: {
                targetDt : my_date
            },

            // method: "GET",
            type: "GET",
            timeout: 3000,
            dataType: "json",

            success : function(result) {

                $("tbody").empty()
                var tmp = result["boxOfficeResult"]["dailyBoxOfficeList"]

                $.each( tmp, function(idx, item) {
                    // console.log(item)

                    var tr = $("<tr></tr>")     // <tr></tr>

                    var rnumTd = $("<td></td>").text(item.rnum)

                    var imgTd = $("<td></td>")  // <td></td>


                    /*************************** 다음 검색 API ********************************************/

                    var myurl = ""

                    var img = $("<img />").attr("src",
                        function () {

                            var imgUrl = ""
                            $.ajax({
                                async: false,
                                url: "https://dapi.kakao.com/v2/search/image",

                                data: {
                                    query: item.movieNm.replace(/#/gi, '') + "포스터",
                                    sort: "accuracy"
                                },

                                // method: "GET",
                                type: "GET",
                                timeout: 3000,
                                // dataType: "json",

                                beforeSend : function(xhr){
                                    xhr.setRequestHeader("Authorization", "KakaoAK key번호");
                                },

                                success: function(result) {


                                    if (result.documents[0].thumbnail_url == null) {
                                        myurl = result.documents[0].image_url
                                        console.log("image_url")
                                        imgUrl = myurl

                                    } else {
                                        myurl = result.documents[0].thumbnail_url
                                        console.log("thumbnail_url")
                                        imgUrl = myurl

                                    }


                                    // alert("img 에서 서버 호출 성공!")
                                },

                                error: function(error) {
                                    alert("img 에서 서버 호출 실패!")
                                }

                            }) // end of ajax

                            return imgUrl

                        }

                    ).attr("width", 150)
                    imgTd.append(img)

                 /////////////////////////////////////////////////////////////////////////////////////////////


                    var movieNmTd = $("<td></td>").text(item.movieNm)
                    var salesAccTd = $("<td></td>").text(item.salesAcc)
                    var audiCntTd = $("<td></td>").text(item.audiCnt)

                    var viewTd = $("<td></td>")
                    var viewBtn = $("<input />").attr("type","button").attr("value", "상세보기")


                    viewBtn.on("click", function() {

                        $.ajax({
                            async: true,    // 비동기 방식의 호출 (default)
                            url: "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=key번호",
                            data: {
                                movieCd : item.movieCd
                            },

                            // method: "GET",
                            type: "GET",
                            timeout: 3000,
                            dataType: "json",

                            success: function(result2) {

                                var my_info = "영화제목: " + result2.movieInfoResult.movieInfo.movieNm
                                    + "/ 제작 연도: " + result2.movieInfoResult.movieInfo.prdtYear
                                    + "/ 장르: " + result2.movieInfoResult.movieInfo.genres[0].genreNm
                                    + "/ 감독명:  " + result2.movieInfoResult.movieInfo.directors[0].peopleNm
                                    + "/ 배우명: " + result2.movieInfoResult.movieInfo.actors[0].peopleNm
                                    + ", " + result2.movieInfoResult.movieInfo.actors[1].peopleNm

                                alert(my_info)

                            }, // end of success

                            error: function(error) {
                                alert("서버호출 실패!!")
                            } // end of error

                        }) // end of ajax

                    })  // end of viewBtn

                    viewTd.append(viewBtn)

                    tr.append(rnumTd)

                    tr.append(imgTd)

                    tr.append(movieNmTd)
                    tr.append(salesAccTd)
                    tr.append(audiCntTd)

                    tr.append(viewTd)

                    $("tbody").append(tr)

                })

            }, // end of success

            error : function(error) {
                alert("서버호출 실패!!")
            }

        }) // end of ajax
    } // end of if
}
