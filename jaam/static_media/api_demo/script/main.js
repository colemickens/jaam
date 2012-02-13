/* 
 * To make sure the correct structure is in the DOM before 
 * the carousel is created, the script binds a listener to 
 * the focus event of the last project. Then, a focus event 
 * is fired upon creation of each project. When the last project 
 * is created, the focus event triggers the carousel to be created.
 */
//var BASE_URL = "//nickgraef.com:8000";
var BASE_URL = "";
var PHOTO_OPTIONS = {'size': '(220,150)', 'crop': 'true'};
var COLORS = ['crimson', 'gold', 'green'];
var CAROUSEL_OPTIONS = {overflow:'hidden', leftOffset:45, separation:14};

function carousel(){
    $("#projects").carousel(CAROUSEL_OPTIONS);
    addFade();
    $(".loader").fadeOut("fast");
    $("#container").delay(200).fadeIn("slow");
}

function addFade() {
    var left = $("<div>").addClass("fade").addClass("left");
    var right = $("<div>").addClass("fade").addClass("right");
    $("#container").children().first().append(left).append(right);
}

function bindFocus(num_projects){
    $("#proj_"+num_projects).live("focusin", function (){
        carousel();
    });
}

$(document).ready(function (){
    $("#container").hide();
    $.getJSON(BASE_URL+"/api/v1/project/?format=jsonp&callback=?", function (proj_data) {
        var num_projects = proj_data.meta.total_count; //number of projects being loaded
        bindFocus(num_projects);
        $.each(proj_data.objects, function(i, proj) {
            var options = $.extend(PHOTO_OPTIONS, {'project': proj.id});
            $.getJSON(BASE_URL+"/api/v1/photo/?format=jsonp&callback=?", options, function(pic_data) {
                var project_li = $("<li>").addClass("project").attr("id", "proj_"+proj.id).appendTo("#projects");
                project_li.click(function (){
                    if ($(this).hasClass("noclick")){
                        $(this).removeClass("noclick");
                    } else {
                        window.location = "/projects/"+proj.slug;
                    }
                });
                $.each(pic_data.objects, function(j, item){
                    var div = $("<div>").addClass("pic").appendTo(project_li);
                    $("<img/>").attr("src", item.image).appendTo(div);
                });
                var title_box = $("<div>").addClass("title_block").addClass("banner").css("background-color", COLORS[proj.id-1]);
                var title = $("<span>").addClass("title").text(proj.title);
                title.appendTo(title_box);
                title_box.insertAfter(project_li.children()[3] || project_li.children().last());
                project_li.focus();
            });
        });
    });
});

$(document).bind('touchmove', function (e) {
    e.preventDefault();
});