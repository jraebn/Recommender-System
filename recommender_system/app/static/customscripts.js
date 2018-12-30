function searchfunc() {
    
    var sdata = {};
    sdata.keyword = $("#search").val().toLowerCase();
    
  $.ajax({
      url:"/api/search/" + $("#search").val().toLowerCase(),
      method: 'get',
      dataType: 'json',
      contentType: 'application/json',
      data: sdata,
      success: function (data){
          
          var i = 0;
          $("#searchlist").text("");
          while (i < data["books"].length && i < 5) {
              
            $("#searchlist").append("<li><a href='/book/"+ data["books"][i]["ISBN"] +"'>" + data["books"][i]["booktitle"] + "</a></li>");
            i = i + 1;
          };
      },
    });
};

function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
};

function bookdetailer(){
    
    $.ajax({
      url:"/api" + document.location.pathname,
      method: 'get',
      dataType: 'json',
      contentType: 'application/json',
      success: function (data){
          
          $("#img1").attr("src", data["books"][0]["imgurl1"]);
          $("#booktitleheader").append(data["books"][0]["booktitle"]);
          $("#bookdetailspar").append(data["books"][0]["ISBN"]);
          $("#bookauthorheader").append(data["books"][0]["bookauthor"]);
          $("#yrpublishedheader").append(data["books"][0]["yrpublished"]);
          $("#publisherheader").append(data["books"][0]["publisher"]);
          $("#booklink").attr("href", data["books"][0]["imgurl2"]);
      },
    });
    
};
