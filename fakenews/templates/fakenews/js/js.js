$(document).ready(function(){

var x=$("#login");
var y=$("#page1");
    $("#login").hide();
    $("#Webpages").hide();
     $("#Voting").hide();
   $("#Manual").hide();
    $("#URL").hide();
    console.log("1");

    $("#page1").click(function(){
x.fadeOut(100);
x=$("#login");
x.fadeIn(500);

y.css('font-size','20px');
y=$("#page1");
 y.animate({'font-size':'30'},500);



    });
    $("#page2").click(function(){
      x.fadeOut(100);
      x=$("#Webpages");
      x.fadeIn(500);
            

      y.css('font-size','20px');
      y=$("#page2");
       y.animate({'font-size':'30'},500);

    });
    $("#page3").click(function(){
      x.fadeOut(100);
      x=$("#Voting");
      x.fadeIn(500);

      y.css('font-size','20px');
      y=$("#page3");
       y.animate({'font-size':'30'},500);
  });

});
