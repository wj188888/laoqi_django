function del_article(the, article_id) {
    var article_name = $(the).parents("tr").children("td").eq(1).text();
    layer.open({
        type: 1,
        skin: "layui-layer-rim",
        area: ["400px", "200px"],
        title: "删除文章",
        content: '<div class="text-center" style="margin-top:20px"><p>是否确定删除《'+article_name+'》</p></div>'
        btn: ['确定', '取消'],
        yes: function() {
            $.ajax({
                url: '{% url "article:del_article" %}',
                type: "POST",
                data: {"article_id": article_id},
                success: function(e) {
                    if(e=="1") {
                        parent.location.reload();
                        layer.msg("has been deleted.");
                    }else {
                        layer.msg("删除失败");
                    }
                },
            })
        },
    });
}