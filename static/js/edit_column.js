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
            $
        }
    })
}