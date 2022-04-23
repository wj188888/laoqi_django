function publish_article() {
    var title = $("#id_title").val();
    var column_id = $("#which_column").val();
    var body = $("#id_body").val();
    $.ajax({
        url: "{% url 'article:article_post' %}",
        type: "POST",
        data: {"title": title, "body": body, "column_id": column_id},
        success: function(e) {
            if(e=="1") {
                layer.msg("successful");
                location.href = '{% url 'article:article_list' %}';
            }else if(e=="2") {
                layer.msg("sorry.");
            }else {
                layer.msg("项目，名称必须写， 不能为空");
            }
        },
    });
}