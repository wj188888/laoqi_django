function add_column() {
        var index = layer.open({
            type:1,
            skin:"layui-layer-rim",
            area:["400px", "200px"],
            title: "新增栏目",
            content: '<div class="text-center" style="margin-top:20px">
                        <p>请输入新的栏目名称</p>
                        <p>{{column_form.column}}</p>
                      </div>',
            btn:['确定', '取消'],
            yes: function(index, layero){
                column_name = $('#id_column').val();
                $.ajax({
                   url:'{% url "article:article_column" %}',
                   type:'POST',
                   data:{"column": column_name},
                   success:function(e){
                        if(e=="1") {
                            parent.location.reload();
                            layer.msg("good");
                        }else{
                            layer.msg("此栏目已有，请更换名称");
                        }
                   },
                });
            },
            btn2: function(index, layero) {
                layer.close(index);
            }
        });
    }