function searchfunc() {
    console.log($("#search").val().toLowerCase());
    var sdata = {};
    sdata.keyword = $("#search").val().toLowerCase();
    console.log(sdata);
  $.ajax({
      url:"/api/search",
      method: 'get',
      dataType: 'json',
      contentType: 'application/json',
      data: sdata,
      success: function (){
          $("#searchlist").append("<li>gfdag</li>");
      },
    });
};

function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
};
