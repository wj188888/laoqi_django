function del_column(the, column_id) {
    var name = $(the).parents("tr").children("td").eq(1).text();
    layer.open({
        type: 1,
        skin: "layui-layer-rim",
        area: ["400px", "200px"],
        title: "删除栏目",
        content: '<div class="text-center" style="margin-top:20px">
                  <p>是否确定删除{'+name+'}栏目</p>
                  </div>',
        btn: ['确定', '取消'],
        yes: function() {
            $.ajax({
                url: '{% url "article:del_article_column" %}',
                type: "POST",
                data: {"column_id": column_id},
                success: function(e) {
                    if (e=="1") {
                        parents.location.reload();
                        layer.msg("has been deleted.");
                    }else {
                        layer.msg("删除失败");
                    }
                },
            })
        },
    });
}