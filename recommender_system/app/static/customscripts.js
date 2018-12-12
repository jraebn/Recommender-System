function searchfunc() {
    console.log($("#search").val().toLowerCase());
    var sdata = {};
    sdata.keyword = $("#search").val().toLowerCase();
    
  $.ajax({
      url:"/api/search",
      method: 'get',
      dataType: 'json',
      contentType: 'application/json',
      data: sdata,
      success: function (data){
          
          var i = 0;
          $("#searchlist").text("");
          while (i < data["books"].length) {
            console.log(data["books"][i]);  
            $("#searchlist").append("<li><a href='/book/"+ data["books"][i]["booktitle"] +"'>" + data["books"][i]["booktitle"] + "</a></li>");
            i = i + 1;
          };
      },
    });
};

function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
};
