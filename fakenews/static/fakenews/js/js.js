$(document).ready(function(){

var x=$("#login");
var y=$("#page1");
    $("#login").hide();
    $("#Webpages").show();
     $("#Signup").hide();
   var g=$("#Manual");
    var f=$("#URL");
    g.hide();
    f.hide();

    $("#page1").click(function(){
    x.fadeOut(100);
    x=$("#login");
        $("#Webpages").hide();
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
      x=$("#Signup");
      $("#Webpages").hide();
        x.fadeIn(500);
        

      y.css('font-size','20px');
      y=$("#page3");
       y.animate({'font-size':'30'},500);
  });
    $("#url").click(function(){
      $("#URL").fadeIn(500);
        $("#Manual").hide();
      
      
      
      });
      $("#manual").click(function(){
      $("#Manual").fadeIn(500);
        $("#URL").hide();
      
      
      
      });

});
