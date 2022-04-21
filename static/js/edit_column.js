function edit_column(the, column_id) {
    var name = $(the).parents("tr").children("td").eq(1).text();
    var index = layer.open({
        type: 1,
        skin: "layui-layer-rim",
        area: ["400px", "200px"],
        title: "编辑栏目",
        content: '<div class="text-center" style="margin-top:20px">
        <p>请编辑的栏目名称</p>
        <p><input type="text" id="new_name" value="+name+"></p></div>',
        btn: ['确定', '取消'],
        yes: function(index, layero) {
            new_name = $("#new_name").val();
            $.ajax({
                url: "{% url 'article:rename_article_column' %}",
                type: "POST",
                data: {
                    "column_id": column_id, "column_name": new_name
                },
                success: function(e) {
                    if(e=="1"){
                        parents.location.reload();
                        layer.msg("good");
                    }else{
                        layer.msg("新的名称没有保存，修改失败。")
                    }
                },
            });
        },
    });
}